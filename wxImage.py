#coding:utf8
import itchat
import os

#import PIL.Image as Image
from PIL import Image
from os import listdir
import math

itchat.login()

friends = itchat.get_friends(update=True)[0:]

user = friends[0]["UserName"]

print(user)
#创建目录userimg，用来保存好友头像
os.mkdir('userimg')

num = 0
#爬取好友图像
for i in friends:
	img = itchat.get_head_img(userName=i["UserName"])
	fileImage = open('userimg' + "/" + str(num) + ".jpg",'wb')
	fileImage.write(img)
	fileImage.close()
	num += 1
#获得该路径下的图像文件名
pics = os.listdir('./userimg/')

numPic = len(pics)

print(numPic)

eachsize = int(math.sqrt(float(640 * 640) / numPic))

print(eachsize)

numline = int(640 / eachsize)

toImage = Image.new('RGBA', (640, 640))


print(numline)

x = 0
y = 0

'''#输出好友图像的文件名
for filename in os.listdir('./userimg/'):
    print(filename)
'''

for i in pics:
	try:
		#打开图片
		#img1 = Image.open('./userimg/' + '0.jpg')
		#//img1.show()
		img = Image.open('./userimg/'+ i)
		#有时候你的微信爬取好友图片会出现有的好友头像不存在，就会报错，目录不存在，这个时候你就根据console的错误提示，更新掉那张图片，然后再屏蔽掉爬取图片的那段代码即可
	except IOError:
		print("Error: 没有找到文件或读取文件失败")
	else:
		#缩小图片
		img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * eachsize, y * eachsize))
		x += 1
		if x == numline:
			x = 0
			y += 1

#合并的图像可能为RGBA形式，而jpg只有rgb形式，故需要转化，否则会报错
if len(toImage.split()) == 4:
    #prevent IOError: cannot write mode RGBA as BMP
    r, g, b, a = toImage.split()
    img = Image.merge("RGB", (r, g, b))
    img.save('user.jpg')
else:
	toImage.save('user.jpg')

itchat.send_image( "user.jpg", 'filehelper')


