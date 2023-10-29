# Description：项目编译脚本

import os
import argparse

def unitest():
    os.system('mkdir -p build')
    os.system('cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE= ./x86Compile.cmake -DUNIT_TEST=1')
    os.system('cmake --build build')
    os.system('build/unitest/unit_tests')
    return 0

def execute_by_args(args):
    if args.unitest:
        return unitest()

    return -1

if __name__ == "__main__":
    # 1. 定义命令行解析器对象
    parser = argparse.ArgumentParser(description='构建仓构建脚本')

    # 2. 添加命令行参数
    parser.add_argument('-t', '--unitest', action="store_true", help='UniTest: 用gtest进行单元测试')

    parser.add_argument('-p', '--platform', type=str, choices = ['x86', 'arm'], help='Platform: 平台配置，交叉编译指定arm平台')

    # 3. 从命令行中结构化解析参数
    args = parser.parse_args()

    # 4. 根据传入参数进行命令执行
    if execute_by_args(args) == 0:
        print("Build Success!")
        exit(0)
    else:
        print("Build Failed!")
        exit(1)