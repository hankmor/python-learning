"""
在命令行程序中，经常需要获取命令行参数。Python内置的sys.argv保存了完整的参数列表，我们可以从中解析出需要的参数:
sys.argv[1]、sys.argv[2] 等等

但是，如果太复杂的参数，使用 sys.argv 获取就非常不方便，而内置的 argparse 库会极大的减少工作量
"""
import argparse


# 假设我们想编写一个备份MySQL数据库的命令行程序，需要输入的参数如下：
#
# host参数：表示MySQL主机名或IP，不输入则默认为localhost；
# port参数：表示MySQL的端口号，int类型，不输入则默认为3306；
# user参数：表示登录MySQL的用户名，必须输入；
# password参数：表示登录MySQL的口令，必须输入；
# gz参数：表示是否压缩备份文件，不输入则默认为False；
# outfile参数：表示备份文件保存在哪，必须输入。


def main():
    # 定义一个ArgumentParser实例
    parser = argparse.ArgumentParser(
        prog='backup',  # 程序名
        description='Backup MySQL database.',  # 描述
        epilog='Copyright(r), 2023'  # 说明信息
    )
    # 定义位置参数:
    parser.add_argument('outfile')
    # 定义关键字参数:
    parser.add_argument('--host', default='localhost')
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)
    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    # 解析参数:
    args = parser.parse_args()

    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')


if __name__ == '__main__':
    main()

# 控制台输入命令执行： python3 argparse_sample.py -u root -p hello --database testdb backup.sql
# parsed args:
# outfile = backup.sql
# host = localhost
# port = 3306
# user = root
# password = hello
# database = testdb
# gzcompress = False
#
#
# argparse 会自动为们生成帮助信息，可以执行: python3 argparse_sample.py -h
# usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile
#
# Backup MySQL database.
#
# positional arguments:
#   outfile
#
# options:
#   -h, --help            show this help message and exit
#   --host HOST
#   --port PORT
#   -u USER, --user USER
#   -p PASSWORD, --password PASSWORD
#   --database DATABASE
#   -gz, --gzcompress     Compress backup files by gz.
#
# Copyright(r), 2023
