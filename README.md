# conan-xlnt

![build](https://github.com/CodeAvailable/conan-xlnt/workflows/Python%20application/badge.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Conan wrapper for the `xlnt` library, providing a convenient way to integrate `xlnt` into your C++ projects.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation & Usage](#installation--usage)
  - [Using in Your Project](#using-in-your-project)
  - [Building Locally](#building-locally)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Introduction

`conan-xlnt` simplifies the process of using `xlnt` (a modern C++ library for manipulating spreadsheets in memory and reading/writing them from/to XLSX files) within projects managed by Conan. This repository provides the necessary Conan recipe to build and consume `xlnt` as a Conan package, ensuring consistent builds across different environments.

## Features

-   **Easy Integration:** Seamlessly integrate `xlnt` into your Conan-based C++ projects.
-   **Cross-Platform:** Build and use `xlnt` across various operating systems and compilers supported by Conan.
-   **Dependency Management:** Conan handles `xlnt` and its transitive dependencies, simplifying your build process.

## Installation & Usage

### Using in Your Project

To use `xlnt` in your Conan-enabled C++ project, add it to your `conanfile.txt` or `conanfile.py`:

**conanfile.txt:**

```
[requires]
xlnt/1.5.0
```

**conanfile.py:**

```python
from conan import ConanFile

class MyProjectConan(ConanFile):
    requires = "xlnt/1.5.0"
    generators = "CMakeDeps", "CMakeToolchain" # Or other generators as needed
```

Then, install the dependencies:

```bash
conan install . --output-folder=build --build=missing
```

And link against `xlnt` in your `CMakeLists.txt` (if using CMake):

```cmake
find_package(xlnt REQUIRED)
target_link_libraries(your_target_name xlnt::xlnt)
```

### Building Locally

To build the `xlnt` Conan package from this repository locally, navigate to the root of this repository and run:

```bash
conan create . --build=missing
```

This command will build the package and place it in your local Conan cache.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests, report bugs, and suggest features.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Support

If you encounter any issues or have questions, please open an issue on our [GitHub Issues page](https://github.com/CodeAvailable/conan-xlnt/issues).
