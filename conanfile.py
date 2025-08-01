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
            conan_version = os.environ.get("CONAN_VERSION")
            if conan_version:
                if conan_version.startswith('v'):
                    self.version = conan_version[1:]  # Remove 'v' prefix
                else:
                    self.version = conan_version
            else:
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
        env = Environment()
        if self.settings.compiler == "gcc" and self.settings.compiler.libcxx == "libstdc++11":
            env.define("CXXFLAGS", "-D_GLIBCXX_USE_CXX11_ABI=1")
        env.append("CXXFLAGS", "-include cstdint")
        env.append("CXXFLAGS", "-include limits")
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
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["xlnt" if self.settings.build_type == "Release" else "xlntd"]
        self.cpp_info.set_property("cmake_file_name", "xlnt")
        self.cpp_info.set_property("cmake_target_name", "xlnt::xlnt")
