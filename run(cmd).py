# -*- coding:utf-8 -*-

import sys
import Packages.BuildTools as BT
import os

print('Wordcloud Make Tool, Version:1.0')
print('Get more help, Goto (url)')
while True:
    name_object = input('$')
    if 'wordcloud' in name_object:
        if '-c' in name_object:
            f = open(os.getcwd()+'\\'+'text.txt','r',encoding='utf-8')
            widths = input('$width')
            heights = input('$height')
            os_path = input('$os_path')
            max_words = input('$max_words')
            widths = int(widths)
            heights = int(heights)
            max_words = int(max_words)
            BT.wordcloud_make.wordcloud_c(f.read(),widths,heights,os_path,max_words)
            f.close()
        elif '-cm' in name_object:
            f = open(os.getcwd()+'\\'+'text.txt','r',encoding='utf-8')
            widths = input('$width')
            heights = input('$height')
            os_path = input('$os_path')
            max_words = input('$max_words')
            widths = int(widths)
            heights = int(heights)
            max_words = int(max_words)
            BT.wordcloud_make.wordcloud_cm(f.read(),widths,heights,os_path,max_words)
            f.close()
        elif '-e' in name_object:
            f = open(os.getcwd()+'\\'+'text.txt','r',encoding='utf-8')
            widths = input('$width')
            heights = input('$height')
            max_words = input('$max_words')
            widths = int(widths)
            heights = int(heights)
            max_words = int(max_words)
            BT.wordcloud_make.wordcloud_e(f.read(),widths,heights,max_words)
            f.close()
        elif '-m' in name_object:
            f = open(os.getcwd()+'\\'+'text.txt','r',encoding='utf-8')
            BT.wordcloud_make.wordcloud_m(f.read())
            f.close()
    elif name_object == 'exit':
        break
