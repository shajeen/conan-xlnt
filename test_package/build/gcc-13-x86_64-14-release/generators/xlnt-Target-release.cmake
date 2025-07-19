# Avoid multiple calls to find_package to append duplicated properties to the targets
include_guard()########### VARIABLES #######################################################################
#############################################################################################
set(xlnt_FRAMEWORKS_FOUND_RELEASE "") # Will be filled later
conan_find_apple_frameworks(xlnt_FRAMEWORKS_FOUND_RELEASE "${xlnt_FRAMEWORKS_RELEASE}" "${xlnt_FRAMEWORK_DIRS_RELEASE}")

set(xlnt_LIBRARIES_TARGETS "") # Will be filled later


######## Create an interface target to contain all the dependencies (frameworks, system and conan deps)
if(NOT TARGET xlnt_DEPS_TARGET)
    add_library(xlnt_DEPS_TARGET INTERFACE IMPORTED)
endif()

set_property(TARGET xlnt_DEPS_TARGET
             APPEND PROPERTY INTERFACE_LINK_LIBRARIES
             $<$<CONFIG:Release>:${xlnt_FRAMEWORKS_FOUND_RELEASE}>
             $<$<CONFIG:Release>:${xlnt_SYSTEM_LIBS_RELEASE}>
             $<$<CONFIG:Release>:>)

####### Find the libraries declared in cpp_info.libs, create an IMPORTED target for each one and link the
####### xlnt_DEPS_TARGET to all of them
conan_package_library_targets("${xlnt_LIBS_RELEASE}"    # libraries
                              "${xlnt_LIB_DIRS_RELEASE}" # package_libdir
                              "${xlnt_BIN_DIRS_RELEASE}" # package_bindir
                              "${xlnt_LIBRARY_TYPE_RELEASE}"
                              "${xlnt_IS_HOST_WINDOWS_RELEASE}"
                              xlnt_DEPS_TARGET
                              xlnt_LIBRARIES_TARGETS  # out_libraries_targets
                              "_RELEASE"
                              "xlnt"    # package_name
                              "${xlnt_NO_SONAME_MODE_RELEASE}")  # soname

# FIXME: What is the result of this for multi-config? All configs adding themselves to path?
set(CMAKE_MODULE_PATH ${xlnt_BUILD_DIRS_RELEASE} ${CMAKE_MODULE_PATH})

########## GLOBAL TARGET PROPERTIES Release ########################################
    set_property(TARGET xlnt::xlnt
                 APPEND PROPERTY INTERFACE_LINK_LIBRARIES
                 $<$<CONFIG:Release>:${xlnt_OBJECTS_RELEASE}>
                 $<$<CONFIG:Release>:${xlnt_LIBRARIES_TARGETS}>
                 )

    if("${xlnt_LIBS_RELEASE}" STREQUAL "")
        # If the package is not declaring any "cpp_info.libs" the package deps, system libs,
        # frameworks etc are not linked to the imported targets and we need to do it to the
        # global target
        set_property(TARGET xlnt::xlnt
                     APPEND PROPERTY INTERFACE_LINK_LIBRARIES
                     xlnt_DEPS_TARGET)
    endif()

    set_property(TARGET xlnt::xlnt
                 APPEND PROPERTY INTERFACE_LINK_OPTIONS
                 $<$<CONFIG:Release>:${xlnt_LINKER_FLAGS_RELEASE}>)
    set_property(TARGET xlnt::xlnt
                 APPEND PROPERTY INTERFACE_INCLUDE_DIRECTORIES
                 $<$<CONFIG:Release>:${xlnt_INCLUDE_DIRS_RELEASE}>)
    # Necessary to find LINK shared libraries in Linux
    set_property(TARGET xlnt::xlnt
                 APPEND PROPERTY INTERFACE_LINK_DIRECTORIES
                 $<$<CONFIG:Release>:${xlnt_LIB_DIRS_RELEASE}>)
    set_property(TARGET xlnt::xlnt
                 APPEND PROPERTY INTERFACE_COMPILE_DEFINITIONS
                 $<$<CONFIG:Release>:${xlnt_COMPILE_DEFINITIONS_RELEASE}>)
    set_property(TARGET xlnt::xlnt
                 APPEND PROPERTY INTERFACE_COMPILE_OPTIONS
                 $<$<CONFIG:Release>:${xlnt_COMPILE_OPTIONS_RELEASE}>)

########## For the modules (FindXXX)
set(xlnt_LIBRARIES_RELEASE xlnt::xlnt)
