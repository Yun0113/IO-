# -*- coding: utf-8 -*-

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