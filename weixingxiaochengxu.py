
# -*- coding:utf-8 -*-
import atx
import sys
import wda
import time
from atx.ext.report import Report # report lib
from subprocess import call 
reload(sys)
sys.setdefaultencoding('utf8')
d = atx.connect('http://192.168.228.125:8100', platform='ios')
print d.status()
#d.start_app('com.gao7.wallpaper.pid37ch03')
#rp = Report(d, save_dir='report')
rp = Report(d)
rp.patch_wda()
#rp.patch_uiautomator() # for android UI test record (optional)
#rp.info("Test started") # or rp.info("Test started", screenshot=d.screenshot())
#rp.error("Oh no.", screenshot=d.screenshot())
dis = d.display
m= dis.width * 0.5
n1= dis.height  * 0.75
n2= dis.height  * 0.25
#获得机器屏幕大小x,y
def getSize():
    x = dis.width
    y =dis.height
    return (x, y)
#屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    d.swipe(x1, y1, x1, y2,t)
#屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    d.swipe(x1, y1, x1, y2,t)
#屏幕向左滑动
def swipLeft(t):
    l=getSize()
    x1=int(l[0] /5 *4)
    y1=int(l[1]/ 2)
    x2=int(l[0]/ 4)
    y1=int(l[1] / 2)
    d.swipe(x1,y1,x2,y1,t)

#屏幕向右滑动
def swipRight(t):
    l=getSize()
    x1=int(l[0]/ 4)
    y1=int(l[1]/ 2)
    x2=int(l[0] /5 *4)
    y1=int(l[1] / 2)
    d.swipe(x1,y1,x2,y1,t)
    d.session.alert.accept()

num1 = time.strftime('%d/%m月/%Y')  
num=time.strftime('%m')
numday=time.strftime('%d')
numyaer=time.strftime('/%Y')

numold = int(numday)- 1
numolds=str(numold)

if num == '01':            # 判断num的值
    numm='/一月'
elif num == '02':
     numm= '/二月' 
elif num == '03':
     numm= '/三月' 
elif num == '04':
     numm= '/四月' 
elif num == '05':
     numm= '/五月' 
          
elif num == '06':
    numm= '/六月' 
elif num == '07':
     numm='/七月' 
elif num == '08':
     numm= '/八月' 
elif num == '09':
     numm='/九月' 
elif num == 10:
     numm='/十月' 
elif num == 11:
     numm= '/十一月'

elif num == 12:
     numm= '/十二月' 

else:
    print 'roadman'     # 条件均不成立时输出
dated=numday.replace(' ', '') 
datem=numm.replace(' ', '') 
datey=numyaer.replace(' ', '') 
dv=dated+datem+datey
dvold=numolds.replace(' ', '') 
old=dvold+datem+datey



print "壁纸小程序"
def test_caozuo():
    print "壁纸小程序"
d.delay(2)


d(class_name="Icon",label="微信",name="微信").click()
d.delay(1)
d(class_name="Button",label="发现",name="发现").click()
d(class_name="StaticText",label="小程序",name="小程序").click()
d(class_name="StaticText",label="壁纸精选",name="壁纸精选").click()
d(class_name="StaticText",label="翘起你的小木鱼叩叩叩",name="翘起你的小木鱼叩叩叩").click()
d(class_name="Button",label="返回",name="返回").click()
d(class_name="StaticText",label="搜索你想要的壁纸",name="搜索你想要的壁纸").click()
d(class_name="StaticText",label="小程序推荐",name="小程序推荐").click()
d(class_name="Button",label="返回",name="返回").click()
d(class_name="StaticText",label="取消",name="取消").click()
d(class_name="StaticText",label="小程序推荐",name="小程序推荐").click()
d(class_name="Button",label="返回",name="返回").click()
d(class_name="Button",label="我的",name="我的").click()
d(class_name="StaticText",label="易念佛小木鱼",name="易念佛小木鱼").click()
d(class_name="Button",label="返回",name="返回").click()








    
#d.stop_app()
rp.close()

