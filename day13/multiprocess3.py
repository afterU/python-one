
import subprocess
import sys

def main():
    if len(sys.argv) > 1:
        for index in range(1, len(sys.argv)):
            try:
                status = subprocess.call(sys.argv[index])
            except FileNotFoundError:
                print('不能执行%s命令' % sys.argv[index])
    else:
        print('请使用命令行参数指定要执行的进程')

if __name__ == '__main__':
    main()