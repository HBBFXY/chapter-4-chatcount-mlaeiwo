letter = 0
digit = 0
space = 0
other = 0
s = input("请输入一行字符：")
for c in s:
    if c.isalpha():
        letter += 1
    elif c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    else:
        other += 1
print(f"英文字符: {letter}")
print(f"数字: {digit}")
print(f"空格: {space}")
print(f"其他字符: {other}")
