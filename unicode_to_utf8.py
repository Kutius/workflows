import sys

# 获取从 curl 命令输出的 Unicode 编码的响应
unicode_text = sys.stdin.read()

# 将 Unicode 编码的文本转换为 UTF-8 编码
utf8_text = unicode_text.encode('utf-8').decode('unicode_escape')

# 打印转换后的 UTF-8 文本
print(utf8_text)
