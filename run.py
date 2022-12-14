# coding=utf-8

'''2022, A.S.C Team
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
print('2022, A.S.C Team.')
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
print('Made by A.S.C Team, power by A.S.C')
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

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
try:
    import Packages.BuildTools as BT
except:
    messagebox.showerror('')
import os

print()
print('当前程序运行目录为:',os.getcwd())
print()

if __name__ == '__main__':
    time.sleep(1)
    print('Starting...')
    time.sleep(1)
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
                messagebox.showwarning("str->intERROR","Cannot turn a,b,c(str) to int")
            else:
                pass
            finally:
                pass  
            if a >= 10000 or b >= 10000:  
                if messagebox.askquestion('Warning!','图片过大，处理时可能会导致内存溢出，确定要继续吗？') == 'yes':
                    
                    f = open(os.getcwd()+'\\'+"text.txt","r",encoding='utf-8')
                    #messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                    try:
                        BT.wordcloud_make.wordcloud_c(f.read(),a,b,path_,c)
                    except OSError:
                        messagebox.showerror('OSError','请选择正确的操作系统')
                    except ValueError:
                        messagebox.showerror('ValueError','输入正常的数字')
                    
                    finally:
                        f.close()
            else:
                f = open(os.getcwd()+'\\'+"text.txt","r",encoding='utf-8')
                #messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                try:
                    BT.wordcloud_make.wordcloud_c(f.read(),a,b,path_,c)
                except OSError:
                    messagebox.showerror('OSError','请选择正确的操作系统')
                except ValueError:
                    messagebox.showerror('ValueError','输入正常的数字')
                finally:
                    f.close()
        messagebox.showinfo('操作结果:','操作已完成！词云保存在了当前Python程序运行的目录')


    butt = Button(text='生成词云图',command=run)
    butt.place(x=160,y=180)

    def run2():
        if messagebox.askquestion("提示","在点击按钮的同时，请确认以准备好了以下数据:\ntext文件（确保以重命名为text.txt）\n若已经准备好了，请按“是”，否则，请按“否”。") == 'yes':
            f2 = open(os.getcwd()+'\\'+"text.txt",'r',encoding='utf-8')
            #messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
            try:
                BT.wordcloud_make.wordcloud_m(f2.read())
            except FileNotFoundError:
                messagebox.showerror('文件未找到！','FileNotFoundError!')
    butts = Button(text="生成扇形统计图",command=run2)
    butts.place(x=160,y=220)
    messagebox.showinfo('操作结果:','操作已完成！词云保存在了当前Python程序运行的目录')

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
                    f = open(os.getcwd()+'\\'+"text.txt","r",encoding='utf-8')
                    #messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                    try:
                        BT.wordcloud_make.wordcloud_cm(f.read(),a,b,path_,c)
                    except OSError:
                        messagebox.showerror('OSError','请选择正确的操作系统')
                    except ValueError:
                        messagebox.showerror('ValueError','输入正常的数字')
                    finally:
                        f.close()
            else:
                f = open(os.getcwd()+'\\'+"text.txt","r",encoding='utf-8')
                #messagebox.showerror('FileNotFoundError!','未找到文件,确保txt文件在和运行的Python文件在同一目录下，并重命名为text.txt')
                try:
                    BT.wordcloud_make.wordcloud_cm(f.read(),a,b,path_,c)
                except OSError:
                    messagebox.showerror('OSError','请选择正确的操作系统')
                except ValueError:
                    messagebox.showerror('ValueError','输入正常的数字')
                finally:
                    f.close()
    messagebox.showinfo('操作结果:','操作已完成！词云保存在了当前Python程序运行的目录')
    butts3 = Button(window,text='生成以上两者',command=run3)
    butts3.place(x=160,y=260)
    
    window.mainloop()