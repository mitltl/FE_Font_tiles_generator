import os
old=open("old.txt",encoding='utf-8')
new=open("filename.txt",encoding='utf-8')
o=old.readlines()
n=new.readlines()
if len(o) == len(n):
	for i in range (0,len(o)):
		os.rename(o[i].strip(),n[i].strip())
else:
	print("两文件长度不一致,abort")
os.system("rm filename.txt")
os.system("rm old.txt")
os.system("mv *.txt ./..")
os.system("mv *.bmp ../")
