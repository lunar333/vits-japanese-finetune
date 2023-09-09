import os
import librosa
import soundfile

def change_sample_rate(path, new_sample_rate=22050):
    signal, sr = librosa.load(path, sr=None)      # 调用librosa载入音频
    new_signal = librosa.resample(signal, sr, new_sample_rate)      # 调用librosa进行音频采样率转换
    print(f"Resampling: {path}")
    soundfile.write(path, new_signal, new_sample_rate)      # 保存覆盖原音频

def process_directory(original_path):
    for root, dirs, files in os.walk(original_path):
        for file_name in files:
            if file_name.endswith(('.wav')):       # 仅处理.wav文件
                file_path = os.path.join(root, file_name)
                change_sample_rate(file_path, new_sample_rate=22050)

if __name__ == '__main__':
    original_path = "path-to-your-folder"      # 指定原音频文件夹路径
    process_directory(original_path)
