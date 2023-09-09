# How to use
(Suggestion) Python == 3.8

## Clone this repository
```sh
git clone https://github.com/lunar333/vits-japanese-fintune.git
```
## Install requirements
```sh
pip install -r requirements.txt
```

## 数据集制作工具

1.重采样一个文件夹，变为22k
tool文件夹下的resample.py，修改为你的文件夹路径

2.识别切分好的音频，tool文件夹下的whisper_reco.py，修改为你的文件夹路径
1.wav 会出现 1.txt ，里面放的识别文本

3.人工筛选出能用的音频，把不能用的wav和txt都删除

4.使用file_wav_txt.py自动生成vits支持的txt格式

5.使用validate.py,修改路径，生成验证集txt

6.使用delete_number.py，修改路径，删除含有阿拉伯数字的文本

7.python preprocess.py --text_index 2 --filelists path/to/filelist_train.txt path/to/filelist_val.txt

8.修改fine_tune.json,将training_files,validation_files改为你的txt路径

## Build monotonic alignment search
```sh
cd monotonic_align
python setup.py build_ext --inplace
cd ..
```
## Train

# Mutiple speakers
python train_ms.py -c <config> -m <folder>

使用上面命令之后，使用ctrl+c取消，然后把G_0.pth和D_0.pth删除，把下面链接的预训练模型放入，重新开始训练

链接: https://pan.baidu.com/s/1fegilp6XVW6hllmsY7kF5g 提取码: qrie 
--来自百度网盘超级会员v6的分享

## Inference
### Online
See [inference.ipynb](inference.ipynb)



