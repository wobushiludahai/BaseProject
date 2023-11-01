cmake_minimum_required(VERSION 3.13)

if(NOT CYGWIN AND NOT MSYS AND NOT ${CMAKE_SYSTEM_NAME} STREQUAL QNX)
  set(CMAKE_CXX_EXTENSIONS OFF)
endif()

add_subdirectory(googletest-1.14.0)

file(GLOB TEST_SOURCES demo/*.cpp)

if(GCOV_ENABLED)
    message("use gcov")
    # 启用代码覆盖率测试
    set(CMAKE_BUILD_TYPE "Coverage")

    # 设置编译选项
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -fprofile-arcs -ftest-coverage")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -O0 -fprofile-arcs -ftest-coverage")

    # 设置链接选项
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fprofile-arcs -ftest-coverage")
else()
    message("Not gcov")
endif()

add_executable(
  unit_tests
  ${TEST_SOURCES}
  test_main.cpp
)

target_link_libraries(
  unit_tests LINK_PUBLIC
  ${PROJECT_NAME}
  GTest::gtest_main
  GTest::gmock_main
)

target_include_directories(unit_tests
    PUBLIC ${PROJECT_SOURCE_DIR}/include
)

include(GoogleTest)
gtest_discover_tests(unit_tests)
