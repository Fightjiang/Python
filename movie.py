import requests
import re
import time

def get_url(url):
    ip = {'http':'167.99.156.71:8080'}
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url,headers=headers,proxies = ip,timeout=500)
    #print(response)
    response = response.text
    pattern = re.compile(r'<p class="image".*?href="(.*?)".*?'
                         r'data-original="(.*?)".*?alt="(.*?)".*?</p>',re.S)
   # print(response)
    #pattern = re.compile(r'<p class="image"(.*?)</p>',re.S)
    movies = re.findall(pattern,response)
    #print(movies)
    time.sleep(1)
    for movie in movies:
        with open('C:/Users/lec/Desktop/movie.txt','a') as f:
            url = 'http://nlook3.cn' + movie[0]
            f.write("{},,{},{}\n".format(movie[2],movie[1],url))
            #print(movie[0],movie[1],movie[2])


def main():
    # http://nlook3.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-hits-p-1.html
    url1 = 'http://nlook3.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-hits-p-'
    url2 = '.html'
    for i in range(1,146):
        url = url1+str(i) + url2
        print(url)
        get_url(url)



if __name__ == '__main__':
    main()
