# 欢迎使用词云生成工具！  
## 简介:
(WMT)WordCloud Make Tools 可以帮助你快速了解文章信息的一种工具。

## 目录：
0.运行文件  
1.Python Wordcloud Make Tools 命令手册：  
2.关于变量"s"(stopwords)的使用说明  
3.统计图生成说明  
4.操作系统Python解释器要求  
5.部分异常处理  

----

## 0.如何运行文件？
克隆这个存储库后，解压文件，双击run.py

---

## 1.Python Wordcloud Make Tools 命令手册：
详见[wiki:函数说明](https://github.com/XFTY/WordCloud-Make-Tool/wiki/%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%E3%80%8A%E4%B9%A6%E3%80%8B)
## 2.关于变量"s"(stopwords)的使用说明
在run.py文件的第122行，有一个变量s，这里存储了一些文字，这里的文字在词云中是不可见的，如“之”“也”等字。大家可以根据自己的需要修改。
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
