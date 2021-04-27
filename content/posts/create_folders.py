astr = """- Code | 代码
  - Python
    - Flask
    - Pandas
    - Packages
    - Notes
  - Go
    - Basic
  - JavaScript
  - Vue
- Server | 服务器
- Life | 生活
  - Notes | 日常记录
  - Entertainment  | 娱乐相关
- Work | 工作
  - Conferences | 参考文档
  - Diary | 工作日志
- Collections | 收集箱"""

import io
import os

# 把上面的MD层级变成目录list
def get_dirs(s):
    """
    :param s: MD 写法的字符串 或者直接从md里读取解析(readlines返回的list)
    :return : 返回目录list
    """
    parents = []
    dirs = []
    if isinstance(s, str):
        lines = s.splitlines()
    elif isinstance(s, list):
        lines = s
    else:
        lines = None
        raise Exception("无法解析")
    for index, line in enumerate(lines):
        spaces, name = line.split("- ")
        name = name.split(" | ")[0]

        level = len(spaces) // 2
        name = name.strip()
        if not name:
            continue
        # print(level, name)

        # if level == 0:
        #     parents.append(name)
        # 级别比parents集合小，
        if level < len(parents):
            dirs.append(os.path.join('.', *parents))
            while level < len(parents):
                parents.pop()
            parents.append(name)
            # continue
        elif level >= len(parents):
            parents.append(name)
            # continue
        else:
            # dirs.append(os.path.join())
            print('something miss')
        if index == len(lines) - 1:
            dirs.append(os.path.join('.', *parents))
            parents.pop()
    return dirs


def create_floders(dirs, root):
    """
    创建文件夹
    """
    os.chdir(root)
    for _dir in dirs:
        # print(_dir)
        if not os.path.exists(_dir):
            print("新增了目录: ", _dir)
            os.makedirs(_dir)


def read_from_md(path):
    """
    从md文件里面读取lines, 去掉head
    """
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    
    lines = list(filter(lambda x: ('#' not in x) and (x != '\n'), lines))
    return lines

# test_folders = r"E:\我的坚果云\MarkDown"
# create_floders(get_dirs(astr), test_folders)

# test_files = r"E:\我的坚果云\MarkDown\Map.md"

directory = os.getcwd()
# if 'MarkDown' not in directory:
#     raise Exception ("当前目录不是MarkDown" + "----" + directory)

map_file = os.path.join(directory, 'Map.md')

create_floders(get_dirs(read_from_md(map_file)), directory)
