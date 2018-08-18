# -*- coding: utf-8 -*-
import requests
import re
from PIL import Image

def get_image(url_image): # 获取相应的验证码
    image = requests.get(url_image).content
    with open('/Users/lec/Desktop/img.jpg', 'wb') as f:  # 保存图片到本地
        f.write(image)
    image = Image.open('/Users/lec/Desktop/img.jpg')
    image.show()
def get_post_data():
    data = {
        'useDogCode':'',
        'dlfl': '0',
        'USERNAME':'',
        'PASSWORD':'',
        'RANDOMCODE':'',
        'x':'0',
        'y':'0'
    }
    data['USERNAME'] = input("请输入学号\n")
    data['PASSWORD'] = input("请输入密码\n")
    data['RANDOMCODE'] = input("请输入验证码\n")
    return data
def login(url,data):
    s = requests.Session()
    s.post(url=url,data=data)
    return s

def main():
    url_image = 'http://kdjw.hnust.edu.cn/kdjw/verifycode.servlet?0.8285445546734822'
    url = 'http://kdjw.hnust.edu.cn/kdjw/Logon.do?method=logon'
    get_image(url_image)
    data = get_post_data()
    print(data)
    brow = login(url,data)
    response = brow.get('http://kdjw.hnust.edu.cn/kdjw/framework/main.jsp').text
    # print(response)<span style="color: red;" id="errorinfo">该帐号不存在或密码错误,请联系管理员!</span>
    print(response)
    sss = re.findall(r'.*?id="errorinfo">(.*?)</span>', response)
    print(sss)
    try:
        name = re.findall(r'<P class=p1 id=KjFsBt1>(.*?)</P>', response)
    except:
        name = '登陆失败'
    print(name)
if __name__ == '__main__':
    main()
