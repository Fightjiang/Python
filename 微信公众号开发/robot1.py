# -*- coding:utf-8 -*-

import io
import werobot
import random
import linecache
robot = werobot.WeRoBot(token='y11g')

@robot.handler
def articles(message):
	z = []
	reply = ""
	reply = "[ 在线观看 ]" + " 《 " + message.content + "》," + "点击图片在线观看," + "http://img.jandan.net/news/2017/07/25de36e68cecf9c1cfe7878c2b74a88e.jpg," + "http://nlook3.cn/index.php?s=/vod-search-wd-" + message.content + ".html"
	# print(reply)
	reply = reply.split(',')
	z.append(reply)
	return z

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
