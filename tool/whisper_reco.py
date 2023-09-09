import os
import whisper

def transcribe_folder(input_folder):
    # 加载模型
    model = whisper.load_model("large-v2")  #根据你的需要选择，如果显存较小，可以选择small

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 只处理音频文件
        if filename.endswith('.mp3') or filename.endswith('.wav') or filename.endswith('.flac'):
            input_path = os.path.join(input_folder, filename)
            
            # 使用 whisper 进行语音识别
            result = model.transcribe(input_path)
            text = result["text"]
            print(text)
            # 准备输出文件名
            output_filename = os.path.splitext(filename)[0] + '.txt'
            output_path = os.path.join(input_folder, output_filename)

            # 将识别的文本保存到输出文件夹中
            with open(output_path, 'w') as f:
                f.write(text)

if __name__ == '__main__':
    input_folder = 'path-to-your-folder'
    transcribe_folder(input_folder)
