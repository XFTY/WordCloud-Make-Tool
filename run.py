# coding=utf-8

'''2022, 
(WMT) Wordcloud Make Tool, 2022, version:"1.4"
(PGS) PythonGUIsupport version:"1.12.84"

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
                        

'''
import time
print('2022,.')
print('Product coding:utf-8')
print()
print('Kernel and technical support:')
print('+==============================================================+')
print('|           Wordcloud Make Tools 2022(Plan: B)                 |')
print('|             Version:1.4, Alpha Edition.                      |')
print('|                  ---====++====----                           |')
print('| WARNING!:Alpha Edition can not run perfect in your computer. |')
print('+==============================================================+')
time.sleep(0.5)
print()
print('Chinese and GUI Support:')
print('+=====================================+')
print('|        Python中文图形用户界面         ')
print('|      版本:1.12.84,Alpha Edition      ')
print('|        基于Tkinter技术构建            ')
print('|          ---===++===---              ')
print('|     警告！功能未完善，请妥善使用。      ')
print('+=====================================+')
time.sleep(0.5)
print()
print('Chinese and CMD support:')
print()
print('$ about')
print('CMD Chinese support:')
print('')
print('2022,A.S.C Team.')
time.sleep(0.5)
print()
print('Install dependencies:')
print('+=============================================+')
print('|   [Additional python modules are required]  |')
print('|                    jieba                    |')
print('|                  wordcloud                  |')
print('|               alive_progress                |')
print('+=============================================+')



from tkinter import messagebox
import os
import sys
#from PIL import Image
import random
from matplotlib import pyplot
from tkinter import *
try:
    from tkinter.ttk import *
except:
    print()
    print('无法导入tkinter.ttk,建议使用最新版本的python')

try:
    import jieba
    import wordcloud
    from alive_progress import alive_bar
except:
    if messagebox.askquestion('Warning!','检测到此电脑未安装第三方依赖库，是否需要安装？') == 'yes':
        print('正在安装中文分词库...')
        os.system('pip3 install jieba')
        print('正在安装词云库...')
        os.system('pip3 install wordcloud')
        print('正在安装动态进度条...')
        os.system('pip3 install alive_progress')
        messagebox.askquestion('Finish',"安装完成！")
        sys.exit()
    else:
        sys.exit()
finally:
    print('第三方依赖库设置完成!')

s = {'的','而','地','得','眼','着','像','也','眼','了','都','里','在','叫','是起来','我','你','他','她','它',',','.','起来','有','和','刚','闹','呀','吗','啦','跟','风','人','唱','手','脚','脚皮','各','些','闭','多','二','看','说','恼','躺平','摆烂','是','花'}

try:
    pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']
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


if __name__ == '__main__':
    time.sleep(1)
    print('Starting...')
    time.sleep(3)
    '''
    +=====================================+
    |        Python图形用户界面            
    |      版本:1.12.84,Alpha Edition     
    |        基于Tkinter技术构建           
    |          ---===++===---             
    |这个文件可以单独运行，也可以作为一个模块  
    +=====================================+
    '''
    window = Tk()
    selected = IntVar()

    window.title('Wordcloud')
    window.geometry('256x360')

    text_read_title = Label(window,text='WordCloud Tool',font=("Arial Bold",20))
    text_read_title.place(x=10,y=0)

    text_ = Label(window,text='导出->')
    text_.place(x=100,y=200)

    text_read = Label(window,text='文件读取:')
    text_read.place(x=10,y=40)

    text_read = Label(window,text='只需将txt文件重命名为text.txt即可')
    text_read.place(x=10,y=60)

    text_read_3 = Label(window,text='选择目标操作系统:')
    text_read_3.place(x=10,y=80)

    rad1 = Radiobutton(window,text='Win',value=1,variable=selected)
    rad2 = Radiobutton(window,text='Mac',value=2,variable=selected)
    rad1.place(x=10,y=100)
    rad2.place(x=100,y=100)

    text_read_2 = Label(window,text='图片长度:')
    text_read_2.place(x=10,y=160)

    txt_text = Entry(window,width=10)
    txt_text.place(x=10,y=180)

    txt_text_4 = Label(window,text='图片宽度:')
    txt_text_4.place(x=10,y=220)

    txt_text_2 = Entry(window,width=10)
    txt_text_2.place(x=10,y=240)

    text_read_4 = Label(window,text='最大字数:')
    text_read_4.place(x=10,y=270)

    txt_text_5 = Entry(window,width=10)
    txt_text_5.place(x=10,y=290)

    text_vaule = Label(window,text='图片导出设置')
    text_vaule.place(x=10,y=130)

    text_vaule_place = Label(window,text='------------')
    text_vaule_place.place(x=90,y=330)

    def run():
        #butt.configure(text='生成中...')
        if messagebox.askquestion("提示","在点击按钮的同时，请确认以准备好了以下数据:\ntext文件（确保以重命名为text.txt）\n已选择的目标操作系统\n图片长度，图片宽度，最大字数（一定要是数字！）\n若已经准备好了，请按“是”，否则，请按“否”。") == 'yes':
            if selected.get() == 1:
                path_ = 'win'
            if selected.get() == 2:
                path_ = 'mac'
            try:
                a = int(txt_text.get())
                b = int(txt_text_2.get())
                c = int(txt_text_5.get())
            except:
                messagebox.showwarning("Exception in Tkinter callback","Traceback (most recent call last):\nInputError: txt.get must be a number,txt.get can not be others or empty!")
            else:
                pass
            finally:
                pass  
            if a >= 10000 or b >= 10000:  
                if messagebox.askquestion('Warning!','图片过大，处理时可能会导致内存溢出，确定要继续吗？') == 'yes':
                    try:
                        f = open("text.txt","r",encoding='utf-8')
                    except FileNotFoundError:
                        messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                    try:
                        wordcloud_make.wordcloud_c(f.read(),a,b,path_,c)
                    except OSError:
                        messagebox.showerror('OSError','请选择正确的操作系统')
                    except ValueError:
                        messagebox.showerror('ValueError','输入正常的数字')
                    
                    finally:
                        f.close()
            else:
                try:
                    f = open("text.txt","r",encoding='utf-8')
                except FileNotFoundError:
                    messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                try:
                    wordcloud_make.wordcloud_c(f.read(),a,b,path_,c)
                except OSError:
                    messagebox.showerror('OSError','请选择正确的操作系统')
                except ValueError:
                    messagebox.showerror('ValueError','输入正常的数字')
                finally:
                    f.close()


    butt = Button(text='生成词云图',command=run)
    butt.place(x=160,y=180)

    def run2():
        if messagebox.askquestion("提示","在点击按钮的同时，请确认以准备好了以下数据:\ntext文件（确保以重命名为text.txt）\n若已经准备好了，请按“是”，否则，请按“否”。") == 'yes':
            try:
                f2 = open("text.txt",'r',encoding='utf-8')
            except FileNotFoundError:
                messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
            try:
                wordcloud_make.wordcloud_m(f2.read())
            except FileNotFoundError:
                messagebox.showerror('文件未找到！','FileNotFoundError!')
    butts = Button(text="生成扇形统计图",command=run2)
    butts.place(x=160,y=220)

    def run3():
        if messagebox.askquestion("提示","在点击按钮的同时，请确认以准备好了以下数据:\ntext文件（确保以重命名为text.txt）\n已选择的目标操作系统\n图片长度，图片宽度，最大字数（一定要是数字！）\n若已经准备好了，请按“是”，否则，请按“否”。") == 'yes':
            if selected.get() == 1:
                path_ = 'win'
            if selected.get() == 2:
                path_ = 'mac'
            try:
                a = int(txt_text.get())
                b = int(txt_text_2.get())
                c = int(txt_text_5.get())
            except:
                messagebox.showwarning("Exception in Tkinter callback","Traceback (most recent call last):\nInputError: txt.get must be a number,txt.get can not be others or empty!")
            else:
                pass
            finally:
                pass  
            if a >= 10000 or b >= 10000:  
                if messagebox.askquestion('Warning!','图片过大，处理时可能会导致内存溢出，确定要继续吗？') == 'yes':
                    try:
                        f = open("text.txt","r",encoding='utf-8')
                    except FileNotFoundError:
                        messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                    try:
                        wordcloud_make.wordcloud_cm(f.read(),a,b,path_,c)
                    except OSError:
                        messagebox.showerror('OSError','请选择正确的操作系统')
                    except ValueError:
                        messagebox.showerror('ValueError','输入正常的数字')
                    finally:
                        f.close()
            else:
                try:
                    f = open("text.txt","r",encoding='utf-8')
                except FileNotFoundError:
                    messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                try:
                    wordcloud_make.wordcloud_cm(f.read(),a,b,path_,c)
                except OSError:
                    messagebox.showerror('OSError','请选择正确的操作系统')
                except ValueError:
                    messagebox.showerror('ValueError','输入正常的数字')
                finally:
                    f.close()
    butts3 = Button(window,text='生成以上两者',command=run3)
    butts3.place(x=160,y=260)
    
    window.mainloop()
