# 从键盘输入一行字符
text = input("请输入一行字符: ")

# 初始化计数器
letters = 0
digits = 0
spaces = 0
others = 0

# 遍历字符串中的每个字符
for char in text:
    if char.isalpha():  # 检查是否为英文字符
        letters += 1
    elif char.isdigit():  # 检查是否为数字
        digits += 1
    elif char.isspace():  # 检查是否为空格
        spaces += 1
    else:  # 其他字符
        others += 1

# 输出统计结果
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")

