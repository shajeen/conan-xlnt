import os
import shutil
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import download, unzip, copy, rmdir, replace_in_file
from conan.tools.env import Environment
from conan.tools.scm import Git

class XlntConan(ConanFile):
    name = "xlnt"
    license = "MIT license"
    description = "xlnt is a modern C++ library for manipulating spreadsheets in memory and reading/writing them from/to XLSX files"
    url = "https://github.com/tfussell/xlnt"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "CMakeDeps", "CMakeToolchain"

    def set_version(self):
        if not hasattr(self, 'version') or not self.version:
            git = Git(self, folder=self.recipe_folder)
            try:
                # Try to get version from git tag
                tag = git.run("describe --tags --exact-match HEAD").strip()
                if tag.startswith('v'):
                    self.version = tag[1:]  # Remove 'v' prefix
                else:
                    self.version = tag
            except RuntimeError:
                # Fallback to default version if no tag found
                self.version = "1.5.0"

    def layout(self):
        cmake_layout(self)

    def source(self):
        zip_name = "xlnt.zip"
        zip_url = f"https://github.com/tfussell/xlnt/archive/v{self.version}.zip"
        download(self, zip_url, zip_name)
        unzip(self, zip_name, destination=self.source_folder, strip_root=True)
        os.unlink(zip_name)


    def generate(self):
        # Set platform-specific compiler flags
        env = Environment()
        if self.settings.compiler == "gcc" and self.settings.compiler.libcxx == "libstdc++11":
            env.define("CXXFLAGS", "-D_GLIBCXX_USE_CXX11_ABI=1")
        
        # Add compiler flags to ensure standard headers are available globally
        # This addresses missing uint32_t, int32_t, numeric_limits etc. in xlnt source without modifying upstream files
        env.append("CXXFLAGS", "-include cstdint")
        env.append("CXXFLAGS", "-include limits")
        
        # Disable specific warnings that cause build failures in xlnt source
        env.append("CXXFLAGS", "-Wno-dangling-reference")
        env.append("CXXFLAGS", "-Wno-error=dangling-reference")
        env.vars(self).save_script("conanenv")

    def build(self):
        cmake = CMake(self)
        static_flag = "ON" if not self.options.shared else "OFF"
        variables = {"STATIC": static_flag}
        if self.settings.build_type == "Debug": 
            variables["CUSTOM_DEBUG_POSTFIX"] = "d"
        cmake.configure(variables=variables)
        cmake.build()

    def package(self):
        copy(self, "*.hpp", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.source_folder, "include"))
        copy(self, "*.lib", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
        copy(self, "*.dll", dst=os.path.join(self.package_folder, "bin"), src=self.build_folder, keep_path=False)
        copy(self, "*.so", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
        copy(self, "*.dylib", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
        copy(self, "*.a", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["xlnt" if self.settings.build_type == "Release" else "xlntd"]
        self.cpp_info.set_property("cmake_file_name", "xlnt")
        self.cpp_info.set_property("cmake_target_name", "xlnt::xlnt")
