def contains_digit(s):
    return 1 if any(char.isdigit() for char in s) else 0

# 先读取所有行
with open('your_txt', 'r') as f:  #修改为你的文件路径
    lines = f.readlines()

# 过滤掉包含数字的行
filtered_lines = []
for line in lines:
    line_stripped = line.strip()
    last_field = line_stripped.split('|')[-1]
    if not contains_digit(last_field):
        filtered_lines.append(line)

# 写回过滤后的结果                   #修改为你的保存文件路径
with open('your_txt', 'w') as f:
    f.writelines(filtered_lines)
