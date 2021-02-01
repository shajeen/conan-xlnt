import os
import shutil
from conans import ConanFile, CMake, tools

class XlntConan(ConanFile):
    name = "xlnt"
    version = "1.5.0"
    license = "MIT license"
    description = "xlnt is a modern C++ library for manipulating spreadsheets in memory and reading/writing them from/to XLSX files"
    url = "https://github.com/tfussell/xlnt"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = '''shared=False'''
    generators = "cmake"

    def source(self):
        zip_name = "xlnt.zip"
        zip_url = "https://github.com/tfussell/xlnt/archive/v%s.zip" % self.version
        tools.download(zip_url, zip_name)
        tools.unzip(zip_name)
        shutil.move("xlnt-%s" % self.version, "xlnt")
        os.unlink(zip_name)


    def build(self):
        cmake = CMake(self)
        if self.settings.build_type == "Debug": 
            cmake.definitions["CUSTOM_DEBUG_POSTFIX"] = self.settings.build_type
        cmake.definitions["CMAKE_CXX_FLAGS"] = "-D_GLIBCXX_USE_CXX11_ABI=1"
        for option_name in self.options.values.fields:
            activated = getattr(self.options, option_name)
            if option_name == "shared":
                cmake.definitions["STATIC"] = "OFF" if activated else "ON"
        self.output.info(cmake.definitions)
        cmake.configure(source_folder="xlnt")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include/xlnt",src="xlnt/include/xlnt")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["xlnt" if self.settings.build_type == "Release" else "xlntd"]
