# Description：项目编译脚本

import os
import argparse

platform = 'x86'
is_unitest = False
is_need_gcov = False

current_file_path = os.path.abspath(__file__)
current_folder_path = os.path.dirname(current_file_path)

def unitest(is_need_gcov=False):
    os.system('mkdir -p ' + current_folder_path + '/build')
    cmd = 'cmake -S . -B build -DUNIT_TEST=1 '
    if platform == 'x86':
        cmd += '-DCMAKE_TOOLCHAIN_FILE= ./x86Compile.cmake '

    if is_need_gcov == True:
        cmd += '-DGCOV_ENABLED=1 '
    os.system(cmd)
    os.system('cmake --build build')
    os.system('build/unitest/unit_tests')

    os.system('mkdir -p ' + current_folder_path + '/output')

    if is_need_gcov == True:
        os.chdir('./build/src')
        os.system('lcov -c -d . -o test.info --rc lcov_branch_coverage=1')
        os.system('genhtml --branch-coverage -o gcov_result test.info')
        os.system('mv gcov_result ' + current_folder_path + '/output')
    return 0

def execute_by_args(args):
    global is_unitest
    global is_need_gcov

    if args.unitest:
        is_unitest = True

    if args.gcov:
        is_need_gcov = True

    if is_unitest:
        unitest(is_need_gcov)
    else:
        print('to do')

    return 0

if __name__ == "__main__":
    # 1. 定义命令行解析器对象
    parser = argparse.ArgumentParser(description='构建仓构建脚本')

    # 2. 添加命令行参数
    parser.add_argument('-t', '--unitest', action="store_true", help='UniTest: 用gtest进行单元测试')
    parser.add_argument('-g', '--gcov', action="store_true", help='Gcov: 是否增加覆盖率统计选项')

    parser.add_argument('-p', '--platform', type=str, choices = ['x86', 'arm'], help='Platform: 平台配置，交叉编译指定arm平台')

    # 3. 从命令行中结构化解析参数
    args = parser.parse_args()

    # 4. 根据传入参数进行命令执行
    if execute_by_args(args) == 0:
        exit(0)
    else:
        exit(1)