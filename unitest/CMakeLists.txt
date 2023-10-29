cmake_minimum_required(VERSION 3.13)

if(NOT CYGWIN AND NOT MSYS AND NOT ${CMAKE_SYSTEM_NAME} STREQUAL QNX)
  set(CMAKE_CXX_EXTENSIONS OFF)
endif()

add_subdirectory(googletest-1.14.0)

file(GLOB TEST_SOURCES demo/*.cpp)

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
