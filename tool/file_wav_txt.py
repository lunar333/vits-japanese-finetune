import os

input_folder = 'path-to-your-folder'  # 包含.txt文件的输入文件夹
output_file = 'path-to-your/.txt'  # 输出结果的文件

# 遍历输入文件夹中的所有文件
with open(output_file, 'w', encoding='utf-8') as output_file:
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            txt_path = os.path.join(input_folder, filename)
            wav_path = txt_path.replace('.txt', '.wav')  # 用.txt路径生成对应的.wav路径
            
            # 读取.txt文件内容
            with open(txt_path, 'r', encoding='utf-8') as txt_file:
                txt_content = txt_file.read().strip()
            
            # 构建输出内容
            output_content = f"{wav_path}|0|{txt_content}\n"
            
            # 将输出内容追加到文件中
            output_file.write(output_content)
            
            print(f"处理文件 {filename} 完成，结果已追加到 {output_file}")

print("全部处理完成，结果已保存到 train.txt")
