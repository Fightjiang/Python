# -*- coding:utf-8 -*-
import requests
import time
from lxml import etree
import xlwt

def get_url(url):
    ip = {'http': '203.93.125.238:31566'}

   # 110.189.152.86:34975
   # 203.93.125.238:31566

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url, headers=headers, proxies=ip, timeout=500)
    response.encoding = 'utf-8'
    html = response.text
    result = etree.HTML(html)
    name = result.xpath('//*[@id="poiDetail"]/div/div/div[2]/div/div[1]/div[1]/span')
    address = result.xpath('//*[@id="poiDetail"]/div/div/div[2]/div/div[1]/div[2]/span')
    tell = result.xpath('//*[@id="poiDetail"]/div/div/div[2]/div/div[2]/ul/li[2]/div[2]')
    data = []
    data.append(name[0].text)
    data.append(address[0].text)
    data.append(tell[0].text)

    print(name)
    print(address[0].text)
    print(tell[0].text)

    return data


def save(urls):

    myfile = xlwt.Workbook()
    sheet = myfile.add_sheet("sheet1", cell_overwrite_ok=True)
    sheet.write(0, 0, "名称")
    sheet.write(0, 1, '地址')
    sheet.write(0, 2, '电话号码')
    num = 1
    for url in urls:
        print(url)
        data = get_url(url)
        for i in range(3):
            sheet.write(num,i,data[i])
            print(data[i])
        print()
        num = num + 1

    myfile.save("C:/Users/lec/Desktop/data1.xls")

def main():

    url = 'https://hotel.meituan.com/2132572/#info'
    f = open('/Users/lec/Desktop/4567.txt','r')
    urls = []
    for line in f:
        #line = f.readline()
        urls.append(line.strip('\n'))
        #print(line.strip('\n'))

    f.close()
    save(urls)

if __name__ == '__main__':
    main()