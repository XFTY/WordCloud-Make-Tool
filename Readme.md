# 欢迎使用词云生成工具！  
## 简介:
(WMT)WordCloud Make Tools 可以帮助你快速了解文章信息的一种工具。
---
## 更新  
新增：  
Packages/Packages.py  
Packages/__init__.py  
修复:  
修复了已知问题和bug。  
优化:  
更新用户体验。  
最新版本：  
Kernel:v1.4.35(Alpha)  
GUI:v1.12.85(Alpha)  
## 目录：  
1.[Python Wordcloud Make Tools 命令手册：](https://github.com/XFTY/WordCloud-Make-Tool/blob/main/Readme.md#1python-wordcloud-make-tools-%E5%91%BD%E4%BB%A4%E6%89%8B%E5%86%8C)    
2.[关于变量"s"(stopwords)的使用说明](https://github.com/XFTY/WordCloud-Make-Tool/blob/main/Readme.md#2%E5%85%B3%E4%BA%8E%E5%8F%98%E9%87%8Fsstopwords%E7%9A%84%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)   
3.[统计图生成说明](https://github.com/XFTY/WordCloud-Make-Tool/blob/main/Readme.md#3%E7%BB%9F%E8%AE%A1%E5%9B%BE%E7%94%9F%E6%88%90%E8%AF%B4%E6%98%8E)    
4.[操作系统Python解释器要求](https://github.com/XFTY/WordCloud-Make-Tool/blob/main/Readme.md#4%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%92%8Cpython%E8%A7%A3%E9%87%8A%E5%99%A8%E8%A6%81%E6%B1%82)    
5.[部分异常处理](https://github.com/XFTY/WordCloud-Make-Tool/blob/main/Readme.md#5%E9%83%A8%E5%88%86%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86)    

---
## 1.Python Wordcloud Make Tools 命令手册：
    wordcloud_make.wordcloud_c(text,widths,heights,os_font_path,m_wors) -->Wordcloud.png
### 生成词云图片(中文模式)
|参数|功能|可填入的参数(类型)|默认值|
|:---:|:---:|:---:|:---:|
|text|文本接收，在这里输入需要分析的文本。|Any (str)|None|
|widths|导出图片宽度设置。|1~10000 (int)|None|
|heights|导出图片高度设置。|1~10000 (int)|None|
|os_font_path|选择操作系统|win或mac(str)|None|
|m_wors|词云图片中可以出现的最大字数。|大于1的数字(int)|None|
---
  
    wordcloud_make.wordcloud_e(text,widths,heights,m_words) -->Wordcloud.png
### 生成词云图片(英文模式)
|参数|功能|可填入的参数(类型)|默认值|
|:---:|:---:|:---:|:---:|
|text|文本接收，在这里输入需要分析的文本。|Any (str)|None|
|widths|导出图片宽度设置。|1~10000 (int)|None|
|heights|导出图片高度设置。|1~10000 (int)|None|
|m_wors|词云图片中可以出现的最大字数。|大于1的数字(int)|None|
---
    wordcloud_make.wordcloud_m(text) -->pie
### 生成扇形统计图
|参数|功能|可填入的参数(类型)|默认值|
|:---:|:---:|:---:|:---:|
|text|文本接收，在这里输入需要分析的文本。|Any (str)|None|
---
    wordcloud_make.wordcloud_cm(text,widths,heights,os_font_path,m_wors) -->Wordcloud.png/pie
### 生成词云图片（中文模式+扇形统计图）
|参数|功能|可填入的参数(类型)|默认值|
|:---:|:---:|:---:|:---:|
|text|文本接收，在这里输入需要分析的文本。|Any (str)|None|
|widths|导出图片宽度设置。|1~10000 (int)|None|
|heights|导出图片高度设置。|1~10000 (int)|None|
|os_font_path|选择操作系统|win或mac(str)|None|
|m_wors|词云图片中可以出现的最大字数。|大于1的数字(int)|None|
---
## 2.关于变量"s"(stopwords)的使用说明
在run.py文件的第122行，有一个变量s，这里存储者一些文字，这里的文字在词云中是不可见的，如“之”“也”等字。大家可以根据自己的需要修改。
## 3.统计图生成说明  
Python matplotlib->pyplot默认是无法加载中文字体的，因此需要使用系统上的中文字体，该产品默认使用Windows和MacOS系统自带字体,自动识别，无需选择。暂不支持Linux和其他Linux发行版。
## 4.操作系统和Python解释器要求：
### 1.操作系统
在Microsoft Windows环境下，需要Windows7及以上操作系统。  
在Apple MacOS环境下，需要MacOS 10.15.4"Catalina"及以上操作系统。  
关于Python解释器，需要Python3.8及以上版本。
## 5.部分异常处理
### 1.无法运行文件？  
解决方案：
检查Python解释器是否正确安装.  
### 2.在提示成功安装第三方库后，仍然提示未安装第三方库？
解决方案：  
1.检查Python解释器是否添加到了系统环境变量中。  
2.尝试手动安装Python第三方库：  
在cmd(Windows)/bash(MacOS,not Linux)中依次输入：

    pip3 install jieba
    pip3 install wordcloud
    pip3 install alive_progress
