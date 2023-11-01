cmake_minimum_required(VERSION 3.4 FATAL_ERROR)

project(baseproject)
add_subdirectory(src)

if(UNIT_TEST)
    add_subdirectory(unitest)
else()
    message("Not unitest")
endif()

## 针对所有编译器，开启编译警告 (包括C、C++编译器)
add_compile_options("-Wall -Werror")
