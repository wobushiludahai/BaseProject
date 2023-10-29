cmake_minimum_required(VERSION 3.4 FATAL_ERROR)

project(baseproject)
add_subdirectory(src)

if(UNIT_TEST)
    add_subdirectory(unitest)
else()
    message("Not unitest")
endif()

if(GCOV_ENABLED)
    message("use gcov")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
	SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -O0 -fprofile-arcs -ftest-coverage")
else()
    message("Not gcov")
endif()

if(CMAKE_COMPILER_IS_GNUCXX)
    message("use gcov")
    set(CMAKE_EXE_LINKER_FLAGS "-lgcov")
endif()

set(CMAKE_BINARY_DIR ${PROJECT_SOURCE_DIR}/output)

add_custom_target(gcov
    COMMAND gcov --object-directory ${CMAKE_BINARY_DIR}
)

## 针对所有编译器，开启编译警告 (包括C、C++编译器)
add_compile_options("-Wall -Werror")
