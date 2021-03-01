# FE_Font_tiles_generator
A generator for generating the font tiles of gba FE according to font bitmap.

## 用法

1.把从字库生成的位图放到这几个脚本下面，默认位图中单个字是16x16，位图长11504，宽160.因为gbk2312中汉字大概就这么多。

2.`pip install opencv-python` 建议用powershell。不知道是不是我manjaro半年没更新，在那下面用cv2生成的tiles调色板不是256，后面处理调色板会出问题。

3.`python 处理.py`

## 说明
程序挺简单的，有点浪费算力，是为了写的时候省事。影响不大，处理完会稍微慢点。
几个脚本也可以单独使用，位图切块和改色，加阴影，移除多余白块，改调色板。主要针对对话字模，道具字模需要改一下调色板参数(主要是缺小字的点阵字库)。
