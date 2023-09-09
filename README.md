# How to use
(Suggestion) Python == 3.7
## Clone this repository
```sh
git clone https://github.com/lunar333/vits-japanese-fintune.git
```
## Install requirements
```sh
pip install -r requirements.txt
```
## Create datasets
### Single speaker
"n_speakers" should be 0 in config.json
```
path/to/XXX.wav|transcript
```
- Example
```
dataset/001.wav|こんにちは。
```
### Mutiple speakers
Speaker id should start from 0 
```
path/to/XXX.wav|speaker id|transcript
```
- Example
```
dataset/001.wav|0|こんにちは。
```
## Preprocess
If you have done this, set "cleaned_text" to true in config.json
```sh
# Single speaker
python preprocess.py --text_index 1 --filelists path/to/filelist_train.txt path/to/filelist_val.txt

# Mutiple speakers
python preprocess.py --text_index 2 --filelists path/to/filelist_train.txt path/to/filelist_val.txt
```
## Build monotonic alignment search
```sh
cd monotonic_align
python setup.py build_ext --inplace
cd ..
```
## Train

# Mutiple speakers
python train_ms.py -c <config> -m <folder>

使用上面命令之后，使用ctrl+c取消，然后把G_0.pth和D.pth删除，把下面链接的预训练模型放入，重新开始训练

## Inference
### Online
See [inference.ipynb](inference.ipynb)



