# 添加库的源文件
file(GLOB SOURCES demo/*.c)

add_library(${PROJECT_NAME} STATIC ${SOURCES})

target_include_directories( ${PROJECT_NAME}
    PUBLIC ${PROJECT_SOURCE_DIR}/include
)