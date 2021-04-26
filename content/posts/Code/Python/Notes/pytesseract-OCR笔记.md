---
title: pytesseract-OCR笔记
date: 2021-02-11T18:08:57+08:00
toc: true
images:
tags:
  - Python
  - pytesseract
---

## 安装

- 软件依赖包
  - `pip install pillow`
  - `pip install pytesseract`
- 下载识别程序安装包
  - [tesseract-ocr.exe](https://digi.bib.uni-mannheim.de/tesseract/)
- 安装时候选择语言包（Additional language data）![中文简体语言包](https://storage.deabal.cn/md/2019052909324790.png)

### 语言包

[官方语言包下载地址](https://tesseract-ocr.github.io/tessdoc/Data-Files)



### 配置脚本的程序地址

pip安装的tesseract对应的目录下，找到`pytesseract.py` 修改里面的`tesseract_cmd` 地址为exe安装的目录下的`tesseract.exe`



## 遇到的问题

1. *tesseract is not installed or it's not in your path*

   没有安装`tesseract-ORC.exe`软件，主识别程序没有安装

2. *TesseractError: (3221225477, '')*

   安装新版本可以解决
   
3. `1, 'Error opening data file D:\\Program Files (x86)\\Tesseract-OCR\\chi_sim.traineddata Please make sure the TESSDATA_PREFIX environment variable is set to your "tessdata" directory. Failed loading language \'chi_sim\' Tesseract couldn\'t load any languages! Could not initialize tesseract.'`

   这是因为路径不正确，5.x版本，需要直接丢 .traineddata 到exe的目录下



## 使用

```python
import pytesseract
from PIL import Image
path = "xxx"
img = Image(path)
res = pytesseract.image_to_string(img, lang="chi_sim")
print(res)

```

