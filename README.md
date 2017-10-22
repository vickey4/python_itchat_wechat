# python-wechat-itchat
# 环境：python3.6+pycharm
- pip install itchat
- pip install jieba
- pip install pillow
- pip install wordcloud

# 本文资料来源
itchat教程
http://itchat.readthedocs.io/zh/latest/tutorial/tutorial0/#0

用Python玩微信
http://www.bubuko.com/infodetail-2104779.html

itchat+pillow实现微信好友头像爬取和拼接（github地址）
https://github.com/gzm1997/wxImage

# 实现效果
##wxImage.py  拼接微信好友头像
![](https://github.com/vickey4/python_itchat_wechat/raw/master/user1.jpg)  
## 注意：

```python
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
```

## auto_reply.py 自动回复

## signature_cloud.py  好友个性签名词云（词云那里可以换成小黄人图片(指定图片)）
![](https://github.com/vickey4/python_itchat_wechat/raw/master/wechat_cloud.png)  
![](https://github.com/vickey4/python_itchat_wechat/raw/master/wechat_cloud1.png)  

## wechat_fri_sexual.py微信好友男女性别比例

## tuling——robot.py 图灵机器人自动回复功能
![](http://7xrip4.com1.z0.glb.clouddn.com/shiyanlou/itchat/2/demo.png?imageView/2/h/400/)
