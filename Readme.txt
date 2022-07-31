2022, A.S.C Team
(WMT) Wordcloud Make Tool, 2022, version:"1.4"(Beta-Version)
(PGS) PythonGUIsupport version:"1.12.84"(Alpha-Version)

zh-CN
Python Wordcloud Make Tools 中文命令手册：
这里对部分命令进行简单说明：
1. wordcloud_make.wordcloud_c(text,widths,heights,os_font_path,m_words)
    text:即一段文本，以字符串(str)的形式导入到该函数中
    widths:图片宽度，取值范围：1~10000，单位：像素，以整数(int)的形式导入到该函数中。
    heights:图片长度，取值范围：1~10000，单位：像素，以整数(int)的形式导入到该函数中。
    os_font_path:操作系统型号，由于Python WordCloud不支持直接的中文字体输出，需要从操作系统中选择自带的字体。目前支持Microsoft Windows 和 Apple MacOS, 暂不支持Linux和其他Linux发行版。
                 以字符串(str)(win或mac)的形式导入到该函数中.                                                      [simhei.ttf]    [PingFang.ttc]                    
    m_words:即max_words,最大字数，如果是制作生日贺卡等，数值越小越好(当然不是0)，如果是阅读书本大概信息或制作大量信息获取，数值越大越好（当然不是无限大），以整数(int)的形式导入到该函数中。
   wordcloud_make.wordcloud_m(text)
        ext:即一段文本，以字符串(str)的形式导入到该函数中
2.stopwords:停用词，在这里输入你不想在词云中看到的词。这个变量存储在import的下面，名字是's'.
3.统计图生成说明：
    该产品使用的是matplotlib的pyplot.
    中文显示说明：
        Python matplotlib->pyplot默认是无法加载中文字体的，因此需要使用系统上的中文字体，该产品默认使用['font.sans-serif'] = ['Arial Unicode MS', 'simhei'],自动识别，无需选择。暂不支持Linux和其他Linux发行版。
                                                                                                       [local]               [MacOS]       [Windows]                         
4.系统运行要求：
    操作系统：在Microsoft Windows下，需要Windows7及以上的操作系统，推荐在Windows10/11上运行。
             在Apple MacOS下，需要MacOS 10.15.2 "Catalina" 即以上操作系统.   
    Python解释器：
                Python解释器，版本3.6+, 适配的Python版本：3.10.4 64-bit（注意！这个版本不再支持Windows7,如果要在Windows7上使用，请安装Python3.8）
    电脑配置要求：
                处理器：Intel Pentium core2 duo及以上的处理器
                内存要求：
                        4GB DDR3 或 2x2GB DDR3
5.异常处理:
        1.无法运行文件？
            解决方案：
                    检查Python解释器是否正确安装.
        2.在提示成功安装第三方库后，仍然提示未安装第三方库？
            解决方案：
                    检查Python解释器是否添加到了系统环境变量中。
                    尝试手动安装Python第三方库：
                        在cmd(Windows)/bash(MacOS,not Linux)中依次输入：
                            pip3 install jieba
                            pip3 install wordcloud
                            pip3 install alive_progress
                        
6.团队：
        貌似......只有一个人。
看不懂吗？说实话，我自己都不知道我在写什么。
