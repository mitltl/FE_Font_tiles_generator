import os
f1=open("gbk2312.txt",encoding='utf-8') #必须把你位图的字摆成一行，放在gabk2312.txt这个文档。
f2=open("gbk2312.txt",encoding='utf-8')#最好文档设置成utf-8，防止出现其他问题
f3=open("gbk2312.txt",encoding='utf-8')
n="TEXT.fontall.txt"
filename="filename.txt"
#length=len(f1.read()) #用这个貌似一样会导致下面的bug
with open(filename,"w",encoding='utf-8') as file:
    f3.read(1)
    for i in range (0,int(input("处理的字模数目/gbk2312.txt文档中的字数？(下面回答和这个相同)"))):#6763):#这里用变量替代下面就出毛病，input或者预先给定数字没问题，不知道为什么。
        file.write(f3.read(1)+".png"+"\n")
with open(n,"w",encoding='utf-8') as file:
    f1.read(1)
    f2.read(1)
    for i in range (0,int(input("长度"))):#6763):#这里用变量替代就出毛病，input或者预先给定数字没问题，不知道为什么。
        file.write(f1.read(1)+"\t"+"text"+"\t"+"14"+"\t"+f2.read(1)+".png"+"\n") #不可都用f1.read()或者f2.read()
