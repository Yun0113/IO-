# -*- coding: utf-8 -*-
#1.用requests库下载图片https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png

import requests
 
def download_image():
 
    url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
    response = requests.get(url, stream = True)
 
    # 这里打开一个空的png文件，相当于创建一个空的txt文件,wb表示写文件
    with open('C:/Users/Administrator/Documents/test.jpg', 'wb') as file:
            file.write(response.content)
 
    print('下载完成')
 
if __name__ == '__main__':
    download_image()
    
    
#2.用PIL库以流的方式读取此图片的内容
from PIL import Image
im = Image.open('C:/Users/Administrator/Documents/test.jpg')
im.show()

#3.用matplotlib中的matplotlib.pyplot.imshow函数显示该图片

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
lena = mpimg.imread('C:/Users/Administrator/Documents/test.jpg') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
plt.imshow(lena) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
