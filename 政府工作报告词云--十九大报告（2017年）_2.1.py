
# --------------------- 政府工作报告词云 --------------------- #
# V2版----

import jieba
import wordcloud
import imageio 

# 词云形状:
 
mask = imageio.imread( "biglogo.png" )     
excludes = {}

f = open("D:\文档\Python文件\新时代中国特色社会主义.txt", 'r', encoding='utf-8')
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud(    font_path = "msyh.ttc", mask = mask ,\
    width = 1000, height = 700, background_color = "white", \
        )
w.generate(txt)
w.to_file( "十九大报告-新时代中国特色社会主义-2.1.png" )

