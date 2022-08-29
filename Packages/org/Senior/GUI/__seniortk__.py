
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import *
import __future__

try:
    import FontsList
except ImportError:    
    import Packages.org.Senior.GUI.FontsList as FontsList

STRING = 0
bvar = 'random'
fvar = 'random'
fontlist = FontsList.listy
fontvarc = '黑体'
fontvar = 'simhei.ttf'

def currect():
    global bvar
    global fvar
    bvar = bgcb.get()
    fvar = fcb.get()
    print(bvar,fvar)
    messagebox.showinfo('finish!','保存成功!')
    savebgcbe.delete(0,END)
    savefcbe.delete(0,END)
    savebgcbe.insert(STRING,bvar)
    savefcbe.insert(STRING,fvar)

def save():
    global fontvar,fontvarc
    fontvar = fontlist[fontsbox.get()]
    fontvarc = fontsbox.get()
    savefont.delete(0,END)
    savefont.insert(STRING,fontsbox.get())
    
    global bvar
    global fvar
    bvar = bgcb.get()
    fvar = fcb.get()
    print(bvar,fvar)
    messagebox.showinfo('finish!','保存成功!')
    savebgcbe.delete(0,END)
    savefcbe.delete(0,END)
    savebgcbe.insert(STRING,bvar)
    savefcbe.insert(STRING,fvar)

def main():
    global se
    global bgcb
    global fcb
    global savebgcbe,savefcbe,fontsbox,savefont


    se = Tk()

    se.title('wordcloud-高级')
    se.geometry('550x400')

    titlelabel = Label(se,text='高级',font=('微软雅黑',20))
    titlelabel.place(x=229,y=0)# Why not x = 250 ???

    twcs = Label(se,text='词云颜色设置:',font=('微软雅黑',15)) # twcs = TitleofWordCloudSet
    twcs.place(x=10,y=25)

    titlebgcb = Label(se,text='背景颜色:')
    titlebgcb.place(x=10,y=60)

    bgcb = Combobox(se) # bgcb = BackGroudcolorComboBox
    bgcb.place(x=10,y=80)
    bgcb['value'] = ('random','black','white','brown','blue','pink','gold')
    bgcb.current(0)

    titlefcb = Label(se,text='字体颜色:') 
    titlefcb.place(x=10,y=120)

    fcb = Combobox(se) # fcb = FontComboBox(WordCloud)
    fcb.place(x=10,y=140)
    fcb['value'] = ('random','gnuplot','plasma','prism','hsv','rainbow','Blues')
    fcb.current(0)

    titlefont = Label(se,text='词云字体设置:',font=('微软雅黑',15))
    titlefont.place(x=10,y=240)

    titlefontsbox = Label(se,text='词云字体:')
    titlefontsbox.place(x=10,y=280)

    savebuttonfont = Button(se,text='保存',command=save)
    savebuttonfont.place(x=10,y=340)

    fontsbox = Combobox(se)
    fontsbox.place(x=10,y=300)
    fontsbox['value'] = FontsList.liste
    fontsbox.current(1)

    savetitlefont = Label(se,text='词云字体:')
    savetitlefont.place(x=350,y=280)

    savefont = Entry(se,width=20)
    savefont.place(x=350,y=300)
    savefont.insert(STRING,fontvarc)

    #buttsave = Button(se,text='保存',command=currect)
    #buttsave.place(x=10,y=180)

    titlesaveLabel = Label(se,text='保存的设置:',font=('微软雅黑',15))
    titlesaveLabel.place(x=350,y=25)

    savebgcb = Label(se,text='背景颜色:')
    savebgcb.place(x=350,y=60)

    savefcb = Label(se,text='字体颜色:')
    savefcb.place(x=350,y=120)

    savebgcbe = Entry(se,width=20)
    savebgcbe.place(x=350,y=80)
    savebgcbe.insert(STRING,bvar)

    savefcbe = Entry(se,width=20)
    savefcbe.place(x=350,y=140)
    savefcbe.insert(STRING,fvar)

#------------only--use--in--debug--mode--!------------
#   |#textbutton = Button(se,text='测试',command=text)||
#   |#textbutton.place(x=300,y=300)                   |
#-----------------------------------------------------

    se.mainloop()

if __name__ == '__main__':
    main()