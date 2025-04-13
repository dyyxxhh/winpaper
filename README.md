## winpaper
一个简单易用、开源无毒无广、可以自定义壁纸切换时间以及顺序的壁纸切换工具

**使用说明**

If you want to read in English,please read README_en.md

1.从Releases下载编译好的exe（windows）或从仓库下载winpaper.py手动编译

2.在同目录下创建cofig.txt  (编码为utf-8) 格式为 ：

  奇数行写图片路径（可以为绝对路径，也可以为相对路径）

  偶数行写设置图片后的等待时间（s）（为-1则退出程序）
  
  例如（cofig.txt）：
  
    a.png
    1
    b.png
    2
    c.png
    3
    
这个样例的意思就是设置 a.png 为桌面背景，然后等待一秒再设置 b.png 为桌面背景，再等待两秒，再设置 c.png 为桌面背景，再等待3秒，然后再设置 a.png 为背景，再等待一秒再设置 b 点 png 为桌面背景，再等待两秒，再设置 c 点 png 为桌面背景，再等待3秒，然后再设置 a 点 png 为背景，  再等待一秒(循环执行)

如果此时在 c.png，后边的3秒改为-1秒 那么就会在第一遍执行设置完 c.png 之后直接退出程序
