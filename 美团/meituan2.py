# -*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def get_url(url):
    '''
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--proxy-server=http://203.93.125.238:31566")
    driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe", chrome_options=chromeOptions)  # 打开浏览器
    '''
    driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe") # 打开浏览器
    driver.get("http://hotel.meituan.com/hefei")

    def clicks(times):
        for i in range(times):
            result_raw = driver.page_source  # 获取网页的源代码。
            result_soup = BeautifulSoup(result_raw, 'html.parser')  # 使用 Beautiful 进行网页解析
            hotles = result_soup.find_all("a", class_="poi-title")  # href
            address = '/Users/lec/Desktop/45679.txt'
            with open(address, 'a', encoding=('utf-8')) as f:  # 将评论保存在本地文件中
                for link in hotles:
                    print(link.get('href'))
                    f.write('{}\n'.format(link.get('href')))

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滑动到浏览器底部
            button = driver.find_element_by_xpath("//*[@id='app']/section/div/div[1]/div[2]/div/ul/li[10]/a")  # 模拟人工点击加载更多的评论
            button.click()  # 点击操作
            time.sleep(20)  # 等待评论加载
    clicks(50)
    # 退出，清除浏览器缓存
    driver.quit()


def main():
    url = 'https://hotel.meituan.com/hefei/'
    get_url(url)

if __name__ == '__main__':
    main()