# FE_Font_tiles_generator
A generator for generating the font tiles of gba FE according to font bitmap.

## 用法

1.用字库生成位图([参阅这里](https://github.com/hmgle/dot_matrix_font_to_bmp))，把位图对印的汉字放在`gbk2312.txt`中，所有字放在第一行。

2.这几个脚本所在目录新建一个文件夹`mkdir font_tiles&&cd font_tiles`，把字库生成的位图和`gbk2312.txt`放这个文件夹,(默认位图中单个字是16x16.)

3.安装opencv `pip install opencv-python` 

4.`python ../处理.py` 处理完毕后位图和`gbk2312.txt`会移动到脚本所在位置。

## 说明
程序挺简单的，有点浪费算力，是为了写的时候省事。影响不大，处理完会稍微慢点。
几个脚本也可以单独使用，位图切块和改色，生成适合FEbuilder_GBA批量导入的文本，加阴影，改调色板。主要针对对话字模，道具字模需要改一下调色板参数(主要是缺小字的点阵字库)。
