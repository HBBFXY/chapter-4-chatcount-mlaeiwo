# 初始化各类字符的计数变量
letter = 0
digit = 0
space = 0
other = 0

# 获取键盘输入的一行字符
s = input("请输入一行字符：")

# 遍历输入的每一个字符
for c in s:
    if c.isalpha():  # 判断是否为英文字符（字母）
        letter += 1
    elif c.isdigit():  # 判断是否为数字
        digit += 1
    elif c.isspace():  # 判断是否为空格
        space += 1
    else:  # 其余的为其他字符
        other += 1

# 按照格式输出统计结果
print(f"英文字符: {letter}")
print(f"数字: {digit}")
print(f"空格: {space}")
print(f"其他字符: {other}")# 这个文件用于编写代码
