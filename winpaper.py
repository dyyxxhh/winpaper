from tkinter import *
import ctypes
import os
import time
import sys
# 定义常量和函数
SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02

def set_wallpaper_api(image_path):
    """通过Windows API设置壁纸"""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"图片路径不存在: {image_path}")
    
    # 转换为绝对路径并处理斜杠
    abs_path = os.path.abspath(image_path)
    success = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        abs_path,
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )
    return bool(success)
while 1:
    i=0
    with open("cofig.txt", "r", encoding="utf-8") as file:
        for line in file:
            i+=1
            st=line.strip()
            if i%2==1:
                image_path=st
                set_wallpaper_api(image_path)
            else:
                if int(st)>0:
                    time.sleep(int(st))
                elif int(st)==-1:
                    sys.exit()
    
