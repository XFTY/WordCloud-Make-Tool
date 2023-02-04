# 欢迎使用词云生成工具！  
## 简介:  
(WMT)WordCloud Make Tools 可以帮助你快速了解文章信息的一种工具。  
目前暂时性停止维护.
---
## 更新(最新版本)  
新增：  
Packages/Packages.py  
Packages/__init__.py  
修复:  
修复了已知问题和bug。  
优化:  
优化用户体验。  
最新版本：  
Kernel:v1.4.35(Alpha)  
GUI:v1.12.85(Alpha)  
## 目录：
0.[如何运行文件](https://github.com/XFTY/WordCloud-Make-Tool#0%E5%A6%82%E4%BD%95%E8%BF%90%E8%A1%8C%E6%96%87%E4%BB%B6)  
1.[Python Wordcloud Make Tools 命令手册：](https://github.com/XFTY/WordCloud-Make-Tool#1python-wordcloud-make-tools-%E5%91%BD%E4%BB%A4%E6%89%8B%E5%86%8C)    
2.[关于变量"s"(stopwords)的使用说明](https://github.com/XFTY/WordCloud-Make-Tool#2%E5%85%B3%E4%BA%8E%E5%8F%98%E9%87%8Fsstopwords%E7%9A%84%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)   
3.[统计图生成说明](https://github.com/XFTY/WordCloud-Make-Tool#3%E7%BB%9F%E8%AE%A1%E5%9B%BE%E7%94%9F%E6%88%90%E8%AF%B4%E6%98%8E)    
4.[操作系统Python解释器要求](https://github.com/XFTY/WordCloud-Make-Tool#4%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%92%8Cpython%E8%A7%A3%E9%87%8A%E5%99%A8%E8%A6%81%E6%B1%82)    
5.[部分异常处理](https://github.com/XFTY/WordCloud-Make-Tool#5%E9%83%A8%E5%88%86%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86)   
6.[使用命令行版本的wordcloud-make-tool](https://github.com/XFTY/WordCloud-Make-Tool#6%E4%BD%BF%E7%94%A8%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%89%88%E6%9C%AC%E7%9A%84wordcloud-make-tool)

----

## 0.如何运行文件？
克隆这个存储库后，解压文件，双击run.py

---
## 1.Python Wordcloud Make Tools 命令手册：  
详见[wiki:函数的使用说明](https://github.com/XFTY/WordCloud-Make-Tool/wiki/%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)

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
在cmd(Windows)/bash(MacOS)中依次输入：

    pip3 install jieba
    pip3 install wordcloud
    pip3 install alive_progress

## 6.使用命令行版本的wordcloud-make-tool
如果你的电脑无法显示GUI界面，使用命令行版本可以解决这个命令，只需要一行代码、收集一些数据后，即可快速生成。  
详见[wiki:如何使用命令行版本的wordcloud-make-tool](https://github.com/XFTY/WordCloud-Make-Tool/wiki/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%89%88%E6%9C%AC%E7%9A%84%E8%AF%8D%E4%BA%91%E7%94%9F%E6%88%90%E5%99%A8)
