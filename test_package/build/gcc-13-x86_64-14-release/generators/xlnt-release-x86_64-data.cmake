########### AGGREGATED COMPONENTS AND DEPENDENCIES FOR THE MULTI CONFIG #####################
#############################################################################################

set(xlnt_COMPONENT_NAMES "")
if(DEFINED xlnt_FIND_DEPENDENCY_NAMES)
  list(APPEND xlnt_FIND_DEPENDENCY_NAMES )
  list(REMOVE_DUPLICATES xlnt_FIND_DEPENDENCY_NAMES)
else()
  set(xlnt_FIND_DEPENDENCY_NAMES )
endif()

########### VARIABLES #######################################################################
#############################################################################################
set(xlnt_PACKAGE_FOLDER_RELEASE "/home/ahamed/.conan2/p/b/xlnt7e40637f5a145/p")
set(xlnt_BUILD_MODULES_PATHS_RELEASE )


set(xlnt_INCLUDE_DIRS_RELEASE "${xlnt_PACKAGE_FOLDER_RELEASE}/include")
set(xlnt_RES_DIRS_RELEASE )
set(xlnt_DEFINITIONS_RELEASE )
set(xlnt_SHARED_LINK_FLAGS_RELEASE )
set(xlnt_EXE_LINK_FLAGS_RELEASE )
set(xlnt_OBJECTS_RELEASE )
set(xlnt_COMPILE_DEFINITIONS_RELEASE )
set(xlnt_COMPILE_OPTIONS_C_RELEASE )
set(xlnt_COMPILE_OPTIONS_CXX_RELEASE )
set(xlnt_LIB_DIRS_RELEASE "${xlnt_PACKAGE_FOLDER_RELEASE}/lib")
set(xlnt_BIN_DIRS_RELEASE )
set(xlnt_LIBRARY_TYPE_RELEASE STATIC)
set(xlnt_IS_HOST_WINDOWS_RELEASE 0)
set(xlnt_LIBS_RELEASE xlnt)
set(xlnt_SYSTEM_LIBS_RELEASE )
set(xlnt_FRAMEWORK_DIRS_RELEASE )
set(xlnt_FRAMEWORKS_RELEASE )
set(xlnt_BUILD_DIRS_RELEASE )
set(xlnt_NO_SONAME_MODE_RELEASE FALSE)


# COMPOUND VARIABLES
set(xlnt_COMPILE_OPTIONS_RELEASE
    "$<$<COMPILE_LANGUAGE:CXX>:${xlnt_COMPILE_OPTIONS_CXX_RELEASE}>"
    "$<$<COMPILE_LANGUAGE:C>:${xlnt_COMPILE_OPTIONS_C_RELEASE}>")
set(xlnt_LINKER_FLAGS_RELEASE
    "$<$<STREQUAL:$<TARGET_PROPERTY:TYPE>,SHARED_LIBRARY>:${xlnt_SHARED_LINK_FLAGS_RELEASE}>"
    "$<$<STREQUAL:$<TARGET_PROPERTY:TYPE>,MODULE_LIBRARY>:${xlnt_SHARED_LINK_FLAGS_RELEASE}>"
    "$<$<STREQUAL:$<TARGET_PROPERTY:TYPE>,EXECUTABLE>:${xlnt_EXE_LINK_FLAGS_RELEASE}>")


set(xlnt_COMPONENTS_RELEASE )