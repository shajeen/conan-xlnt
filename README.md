![Reference (15)](https://user-images.githubusercontent.com/2623563/144739311-5bea6de1-ba4b-4194-9d5d-6cf880220268.png)
![build](https://github.com/CodeAvailable/conan-xlnt/workflows/Python%20application/badge.svg?branch=master)

A conan wrapper for xlnt from https://github.com/tfussell/xlnt

### Build Instructions

Build the package locally:
```bash
conan create . --build=missing
```

Use in your project by adding to conanfile.txt:
```
[requires]
xlnt/1.5.0
```

Or install directly:
```bash
conan install --requires=xlnt/1.5.0 --build=missing
```

### Reference
| Tag  |    conan referance   | 
|:-----|:--------------------:|
| [v1.3.0](https://github.com/CodeAvailable/conan-xlnt/releases/tag/v1.3.0) | xlnt/1.3.0@master/release |
| [v1.4.0](https://github.com/CodeAvailable/conan-xlnt/releases/tag/v1.4.0) | xlnt/1.4.0@master/release |
| [v1.5.0](https://github.com/CodeAvailable/conan-xlnt/releases/tag/v1.5.0) | xlnt/1.5.0@master/release |


### Bug report

if you face any issue or need any kind of other help. Please raise a issue.

### Contributing

Please read the [CONTRIBUTING](https://github.com/shajeen/conan-xlnt/blob/master/CONTRIBUTING.md) before raising the PR.


#### Build and package locally using Conan 2.x
