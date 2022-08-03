# coding=utf-8
import os
import sys
import random
import time
from tkinter import messagebox
from tkinter.ttk import *
try:
    from alive_progress import alive_bar
    import jieba
    import wordcloud
    from matplotlib import pyplot
except:
    if messagebox.askquestion('Warning!','检测到此电脑未安装第三方依赖库，是否需要安装？') == 'yes':
        print('正在安装中文分词库...')
        os.system('pip3 install jieba')
        print('正在安装词云库...')
        os.system('pip3 install wordcloud')
        print('正在安装动态进度条...')
        os.system('pip3 install alive_progress')
        print('正在安装matplotlib...')
        os.system('pip install matplotlib')
        messagebox.showinfo('Finish',"安装完成！")
        sys.exit()
    else:
        sys.exit()
finally:
    print('第三方依赖库设置完成!')

s = {'的','而','地','得','眼','着','像','也','眼','了','都','里','在','叫','是起来','我','你','他','她','它',',','.','起来','有','和','刚','闹','呀','吗','啦','跟','风','人','唱','手','脚','脚皮','各','些','闭','多','二','看','说','恼','躺平','摆烂','是','花'}

try:
    pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']
    #-[Chinese-Mode]----[local]---------------[MacOS]---------[Windows]
except:
    print('pyplot:无法导入中文字体，显示中文可能会出错。')

background_color = ['black','white','brown','blue','pink','gold']
colormap = ['gnuplot','plasma','prism','hsv','rainbow','Blues']

class wordcloud_make():
    def wordcloud_c(text,widths,heights,os_font_path,m_wors):
        '''生成词云图片（中文模式）'''
        with alive_bar(len(range(4)),title=f'Running txt->wordcloud.png') as bar:
            lst = jieba.lcut(text)
            m = ' '.join(lst)
            print('running...')
            print("中文分词成功完成")
            bar()
            #mac = 'PingFang.ttc'
            #win = 'simhei.ttf'
            if os_font_path == 'win' or os_font_path == 'windows':
                os_font_path = 'simhei.ttf'
            elif os_font_path == 'mac' or os_font_path == 'macintosh':
                os_font_path = 'PingFang.ttc'
                print('OS write finish')
            bar()
            random.shuffle(background_color)
            random.shuffle(colormap)
            w = wordcloud.WordCloud(
                width=widths,
                height=heights,
                font_path=os_font_path,
                stopwords=s,
                background_color=background_color[0],
                colormap=colormap[0],
                max_words=m_wors
            )
            print('准备生成词云文件')
            #print('读文件：text.txt')
            time.sleep(3)
            print('请稍后......Please wait.......')
            w.generate(m)
            print('即将完成...')
            bar()
            time.sleep(4)
            w.to_file('词云.png')
            bar()
            print('词云图片已生成!')
            print('词云保存在了./词云.png')
            print('==================================================================================')

            #p = Image.open('词云.png')
            #p.show()
        print()
        print()
        print('--------------------------------------------------------------------------------------')
        with alive_bar(100,title='正在处理......') as t:
            for item in range(100):
                t()
                time.sleep(0.001)
        messagebox.showinfo('操作结果:','操作已完成！词云保存在了当前Python程序运行的目录')

    
    def wordcloud_e(text,widths,heights,m_words):
        '''生成词云图片(English)'''
        random.shuffle(background_color)
        random.shuffle(colormap)
        we = wordcloud.WordCloud(
            width=widths,
            height=heights,
            background_color=background_color[0],
            colormap=colormap[0],
            max_words=m_words
        )

        we.generate(text)
        we.to_file('wordcloud.png')

        #pe = Image.open('wordcloud.png')
        #pe.show()
        messagebox.showinfo('操作结果:','操作已完成！词云保存在了当前Python程序运行的目录')

    def wordcloud_cm(text,widths,heights,os_font_path,m_wors):
        with alive_bar(len(range(10)),title=f'Running text -> Wordcloud.png/~[?:?]') as bar:
            start = time.time()
            print('Start Running......')
            bar()
            '''生成词云图片（中文模式+扇形统计图）'''
            lst = jieba.lcut(text)
            m = ' '.join(lst)
            print('中文分词成功完成')
            bar()
            resoult = {}
            for l in m:
                resoult[l] = m.count(l)
            mlibf = []
            mlibs = []
            for k in resoult:
                mlibf.append(k)
                mlibs.append(resoult[k])
            print('分词封装成功完成')
            bar()
            del resoult
            #mac = 'PingFang.ttc'
            #win = 'simhei.ttf'
            if os_font_path == 'win' or os_font_path == 'windows':
                os_font_path = 'simhei.ttf'
            elif os_font_path == 'mac' or os_font_path == 'macintosh':
                os_font_path = 'PingFang.ttc'
            print('字体选择成功完成')
            bar()
            random.shuffle(background_color)
            random.shuffle(colormap)
            bar()
            w = wordcloud.WordCloud(
                width=widths,
                height=heights,
                font_path=os_font_path,
                stopwords=s,
                background_color=background_color[0],
                colormap=colormap[0],
                max_words=m_wors
            )
            print('初始设置成功完成')
            bar()
            print('开始绘制词云图，请稍后......')
            w.generate(m)
            bar()
            print('即将完成')
            time.sleep(3)
            w.to_file('词云.png')
            print('词云成功保存')
            bar()
            #p = Image.open('词云.png')
            #p.show()
            print('正在绘制扇形统计图......')
            pyplot.pie(mlibs,labels=mlibf, autopct='%.1f%%')
            end = time.time()

            print('词云图片已生成!')
            print('扇形统计图以生成')
            print('本次程序执行完成，用时',end-start,'s')
            print('词云保存在了./词云.png')
            bar()
            bar()
            mlibf.clear()
            mlibs.clear()
        with alive_bar(100,title='正在处理......') as t:
            for item in range(100):
                t()
                time.sleep(0.001)
        messagebox.showinfo('操作结果:','操作已完成！词云保存在了当前Python程序运行的目录')
        pyplot.show()
    def wordcloud_m(text):
        start = time.time()
        '''生成扇形统计图'''
        lst = jieba.lcut(text)
        m = ' '.join(lst)
        resoult = {}
        for l in m:
            resoult[l] = m.count(l)
        mlibf = []
        mlibs = []
        for k in resoult:
            mlibf.append(k)
            mlibs.append(resoult[k])
        del resoult
        #mlibc = mlibs[:6]
        pyplot.pie(mlibs,labels=mlibf, autopct='%.1f%%')
        end = time.time()
        print('扇形统计图以生成')
        print('本次程序执行完成，用时',end-start,'s')
        mlibf.clear()
        mlibs.clear()
        with alive_bar(100,title='正在处理......') as t:
            for item in range(100):
                t()
                time.sleep(0.001)
        pyplot.show()