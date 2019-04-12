from conans import ConanFile, CMake

class XlntConan(ConanFile):
    name = "xlnt"
    version = "1.3.0"
    license = "MIT license"
    description = "xlnt is a modern C++ library for manipulating spreadsheets in memory and reading/writing them from/to XLSX files"
    url = "https://github.com/tfussell/xlnt"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/tfussell/xlnt.git")
        self.run("cd xlnt")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="xlnt")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include/xlnt",src="xlnt/include/xlnt")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="/usr/lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["xlnt"]

