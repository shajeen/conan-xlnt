########## MACROS ###########################################################################
#############################################################################################

# Requires CMake > 3.15
if(${CMAKE_VERSION} VERSION_LESS "3.15")
    message(FATAL_ERROR "The 'CMakeDeps' generator only works with CMake >= 3.15")
endif()

if(xlnt_FIND_QUIETLY)
    set(xlnt_MESSAGE_MODE VERBOSE)
else()
    set(xlnt_MESSAGE_MODE STATUS)
endif()

include(${CMAKE_CURRENT_LIST_DIR}/cmakedeps_macros.cmake)
include(${CMAKE_CURRENT_LIST_DIR}/xlntTargets.cmake)
include(CMakeFindDependencyMacro)

check_build_type_defined()

foreach(_DEPENDENCY ${xlnt_FIND_DEPENDENCY_NAMES} )
    # Check that we have not already called a find_package with the transitive dependency
    if(NOT ${_DEPENDENCY}_FOUND)
        find_dependency(${_DEPENDENCY} REQUIRED ${${_DEPENDENCY}_FIND_MODE})
    endif()
endforeach()

set(xlnt_VERSION_STRING "1.5.0")
set(xlnt_INCLUDE_DIRS ${xlnt_INCLUDE_DIRS_RELEASE} )
set(xlnt_INCLUDE_DIR ${xlnt_INCLUDE_DIRS_RELEASE} )
set(xlnt_LIBRARIES ${xlnt_LIBRARIES_RELEASE} )
set(xlnt_DEFINITIONS ${xlnt_DEFINITIONS_RELEASE} )


# Only the last installed configuration BUILD_MODULES are included to avoid the collision
foreach(_BUILD_MODULE ${xlnt_BUILD_MODULES_PATHS_RELEASE} )
    message(${xlnt_MESSAGE_MODE} "Conan: Including build module from '${_BUILD_MODULE}'")
    include(${_BUILD_MODULE})
endforeach()


