#百度网盘
# -*- coding:utf-8 -*-

import io
import werobot
import random
import linecache
robot = werobot.WeRoBot(token='xxxx')

@robot.handler
def articles(message):
    text = message.content
    movie = ""
    movies = open('movie.txt')
    sum = 0
    for x in movies:
        if(text in x):
            sum += 1
            name,link,code = x.split('  ')
            movie = movie + name + '\n' + link + '\n' + code + '\n'
            if(sum>5):
                break 
    #print(movie)
    if(movie == ""):
        return "哎....\n没有你要的资源，请留言资源\n\n或检查输入的电影是否正确"
    return movie
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
