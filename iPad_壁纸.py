
# -*- coding:utf-8 -*-
import atx
import sys
import wda
import time
from atx.ext.report import Report # report lib
from subprocess import call 
reload(sys)
sys.setdefaultencoding('utf8')
d = atx.connect('http://192.168.228.207:8100', platform='ios')
print d.status()
d.start_app('com.gao7.wallpaper.pid37ch03')
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


def fn():     
     
    if d(label="星星好评",name="星星好评",class_name="StaticText").exists:
        d(label="以后吧", name="以后吧", className="Button").click()

#---------------
def diybz():  
    print "搜索"
try:
    
    d(class_name="Cell").click()
    d.delay(1)
    d(class_name="Button",label="下载").click()
    d.delay(1)
    d(class_name="Button",label="DIY").click()
    d(class_name="Button",label="个性贴纸").click()
 
    d(class_name="Button",label="3").click()
   
    d(class_name="Button",label="保存").click()
    #d(class_name="Button",label="分享").click()
    #d.click(80,124)
    d.click_image("close.2048x1536.png")
    d(class_name="Button",label="取消").click()
    print "第1个步骤执行完成"
except Exception:
    fn()   
finally:   
    print "done"
#------------------------------------------
try:

    d(class_name="Button",label="DIY").click()
    d(class_name="Button",label="心情水印").click()
   
    d(class_name="Button",label="btn diy 0").click()
    
    d(class_name="Button",label="btn diy black").click()
   
    d(class_name="Button",label="保存").click()
    d.click_image("close.2048x1536.png")
    print "第2个步骤执行完成"
except Exception:
    fn()   
finally:
    
    print "done"

#------------------------------------------
try:

    d(class_name="Button",label="btn diy 1").click()
    d.delay(0.5)
    d(class_name="Button",label="btn diy black").click()
    d.delay(0.5)
    d(class_name="Button",label="保存").click()
    d.delay(0.5)
    d.click_image("close.2048x1536.png")
    print "第3个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#------------------------------------------
try:

    d(class_name="Button",label="btn diy 2").click()
  
    d(class_name="Button",label="btn diy black").click()
    
    d(class_name="Button",label="保存").click()
    d.delay(0.5)
    #d.click_image("x.2048x1536.png")
    d.click_image("close.2048x1536.png")
    d.delay(0.5)
    d(class_name="Button",label="取消").click()
    print "第4个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#------------------------------------------
try:

    d(class_name="Button",label="DIY").click()
    d(class_name="Button",label="日历水印").click()
   
    d(class_name="Button",label="btn diy black").click()
    
    d(class_name="Button",label="保存").click()
    d.delay(0.5)
    d.click_image("close.2048x1536.png")
    d(class_name="Button",label="取消").click()
    print "第5个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#------------------------------------------
try:
    d(class_name="Button",label="DIY").click()
    d(class_name="Button",label="滤镜特效").click()
    d.delay(0.5)
    #d.click_image("lvjing.2048x1536.png")
    d.click_image("yese.2048x1536.png")
    
  
    Slider=d(class_name="Slider")
    #for i in range(0, 8):
       # Slider.click()
     
        
    d(class_name="Button",label="保存").click()
    d.delay(1)
    d.click_image("close.2048x1536.png")
    d.delay(0.5)
    d(class_name="Button",label="取消").click()
    print "第6个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#------------------------------------------
try:
    d(class_name="Button",label="DIY").click()
    d(class_name="Button",label="制作大头").click()
    
    Slider=d(class_name="Slider")
    #for i in range(0, 8):
     #   Slider.click()
    d(class_name="Button",label="wp bighead save").click()
    d.click_image("close.2048x1536.png")
    d(class_name="Button",label="wp diy back").click()
    print "第7个步骤执行完成"
except Exception:
    fn()   
finally:
    #fn()
    print "done"
#------------------------------------------
try:

    d(class_name="Button",label="预览").click()
    d(class_name="Button",label="桌面预览").click()
    d.delay(1)


    d.click(80,124)
    d(class_name="Button",label="预览").click()
    d(class_name="Button",label="锁屏预览").click()
    d.click(80,124)
    d.delay(1)
    d(class_name="Button",label="信息",name="信息").click()
    d(class_name="Button",label="返回",name="返回").click()
    
    print "第8个步骤执行完成"
    #锁屏预览
except Exception:
    fn()   
finally:
    
    print "done"
#--------------------------------------------------
try:
    #d(class_name="Cell").click()
    d.delay(2)
    d(class_name="Button",label="分享",name="分享").click()
    d.delay(1)
    d.click_image("wxhy.2048x1536.png")

    d(class_name="StaticText",label="创建新的聊天").click()
    d.delay(1)
    d(class_name="StaticText",label="loneyao").click()
    d.delay(1)
    d(class_name="Button",label="确定(1)").click()
    d.delay(1)
    d(class_name="Button",label="发送").click()
    d.delay(1)
    d(class_name="Button",label="返回壁纸-改变从壁纸开始").click()
    d.delay(1)
    print "第18个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button",label="分享",name="分享").click()
    d.delay(1)
    d.click_image("wxpyq.2048x1536.png")   
    d.delay(1)
    d(class_name="Button",label="发送").click()
    d.delay(1)
    print "第19个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button",label="分享",name="分享").click()
    d.delay(1)
    d.click_image("xlwb.2048x1536.png")
    d.delay(1)
    d(class_name="Button",label="发送",name="发送").click()
    d.delay(1)
    print "第20个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button",label="分享").click()
    d.delay(1)
    d.click_image("txqq.2048x1536.png")
    d.delay(1)#d(class_name="Button",label="好友").click()
    #d.delay(1)
    #d(class_name="StaticText",label="我的好友").click()
    #d.delay(1)

   
   
    
    #d.click_image("cly.2048x1536.png")
    d(class_name="StaticText",name="陈冷耀-天志股份",label="陈冷耀-天志股份")[1].click()
    d.delay(2)
    d(class_name="Button",label="发送").click()
    d.delay(2)
    d(class_name="Button",label="返回壁纸").click()
    d.delay(2)
    #swipeDown(0.1)
    d(label="返回", name="返回", class_name="Button")[1].click()
    print "第21个步骤执行完成"
except Exception:
    fn()   
finally:   
    print "done"
#-------------------------------------------------------

def test_down():
    print "个人中心"
try:
    d(class_name="Button",label="ipad nav mine",name="ipad nav mine").click()
    d.delay(2)
    d(class_name="Button",index=4).click()
    d.delay(2)
    #rp.assert_equal("nsnsdhx.2048x1536.png", "xhdsnsn.2048x1536.png", desc="图片下载成功", screenshot=True, safe=True)
    d(class_name="Button",label="wp upload delete on").click()
    d(class_name="Cell").click()
    d(class_name="Button",label="删除").click()
    d(class_name="Button",label="wp nav back").click()
    print "第9个步骤执行完成"

except Exception:
    fn()   
finally:
    
    print "done"

#--------------------------------------------------------------------------
try:
    d.delay(1)
    d(class_name="Button")[6].click()
    d.delay(1)
    d(class_name="Button",label="wp upload delete on").click()
    d(class_name="Cell").click()
    d(class_name="Button",label="删除").click()
    d.delay(1)
    print "第10个步骤执行完成"
except Exception:
    fn()   
finally:
    print "done"
#--------------------------------------------------------------------------
try:
    d(class_name="Button",label="wp upload add").click()
    d(class_name="Button",label="从相册获取").click()
    xjjj=d(class_name="StaticText",label="相机胶卷")
    syzp=d(class_name="StaticText",label="所有照片")
    d.delay(2)
    if xjjj.exists:
        xjjj.click()
    if syzp.exists:
        syzp.click()
    #d(class_name="StaticText",label="所有照片").click()
    d.delay(1)    
    d(className="Image")[9].click()
    #d(className="Cell", index=9).click()
    d.delay(1)
    d(class_name="Button",label="GHD button confirm").click()
    d.delay(1)
    d(class_name="Button",label="DIY").click()
    d(class_name="Button",label="日历水印").click()
    d.delay(1)
    d(class_name="Button",label="btn diy black").click()
    d.delay(1)
    d(class_name="Button",label="保存").click()
    d.click_image("close.2048x1536.png")
    d(class_name="Button",label="取消").click()
    d(class_name="Button",label="返回").click()
    print "第11个步骤执行完成"
except Exception:
    fn()   
finally:
    
    print "done"
#-------------------------------------------------------------------
try:
    d.delay(1)
    d(class_name="Button",label="wp upload add").click()
    d(class_name="Button",label="拍照").click()
    d.delay(1)
    d(class_name="Button",label="拍照").click()
    d.delay(1)
    d(class_name="Button",label="编辑").click()
    d(class_name="Button",label="DIY").click()
    d(class_name="Button",label="日历水印").click()
    d.delay(1)
    d(class_name="Button",label="保存").click()
    d.delay(1)
    d.click_image("close.2048x1536.png")
    d.delay(1)
    d(class_name="Button",label="取消").click()
    d.delay(1)
    d(class_name="Button",label="返回").click()
    d(class_name="Button",label="个人中心").click()
    print "第12个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"


#----------------------------------------------------------
try:
    d(class_name="Button",index=7).click()
    d.delay(1)

    #rp.assert_equal("nsnsdhx.2048x1536.png", "xhdsnsn.2048x1536.png", desc="图片下载成功", screenshot=True, safe=True)
    d(class_name="StaticText",label="可爱表情").click()
    d.delay(1)
    d(class_name="Button",label="立即下载").click()
    d.delay(1)
    d(class_name="Button",label="ipad stickers close").click()
    d.delay(1)
    d(class_name="Button",label="wp nav back").click()
    d.delay(1)
    d(class_name="Button",index=6).click()
    d.delay(1)
    d(class_name="Cell").click()
    d.delay(1)
    d(class_name="Button",label="DIY").click()
    d.delay(1)
    d(class_name="Button",label="个性贴纸").click()
    d.delay(1)
    d(class_name="StaticText",label="可爱表情").click()
    d.delay(1)
    rp.assert_ui_exists(d(text='可爱表情'), desc='贴纸下载成功')
    d(class_name="Button",label="取消").click()
    d.delay(1)
    d(class_name="Button",label="返回").click()
    d.delay(1)
    d(class_name="Button",label="wp nav back").click()
    d.delay(1)
    d(class_name="Button",index=7).click()
    d.delay(1)
    d(class_name="StaticText",label="可爱表情").click()
    d.delay(1)
    d(class_name="Button",label="删除").click()
    d(class_name="Button",label="ipad stickers close").click()
    d(class_name="Button",label="wp nav back").click()
    print "第13个步骤执行完成"
except Exception:
    fn()   
finally:
    #fn()
    print "done"
def test_favico():
        print "222"
try:
    d(class_name="Button",label="ipad mine bg").click()
    d.delay(1)
    d(class_name="Button",label="腾讯QQ").click()
    d.delay(2)
    d.click_image("shezhi.2048x1536.png")
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="ipad nav close").click()
    d.delay(1)
except Exception:
    fn()   
finally:
    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button",label="ipad mine bg").click()
    d.delay(1)
    d(class_name="Button",label="新浪微博").click()
    d.delay(2)
    d.click_image("shezhi.2048x1536.png")
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="ipad nav close").click()
    print "第14个步骤执行完成"
except Exception:
    fn()   
finally:
    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button",label="ipad mine bg").click()
    d.delay(1)
    d(class_name="Button",label="微信").click()
    d.delay(2)
    d(class_name="Button",label="确认登录").click()
    d.delay(2)
    d.click_image("shezhi.2048x1536.png")
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="ipad nav close").click()
    d.delay(1)
    print "第15个步骤执行完成"
except Exception:
    fn()   
finally:
    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button",label="ipad mine bg").click()
    d(class_name="TextField").click()
    d.type("lengyao1")
    d(class_name="SecureTextField").click()
    d.type("lengyao")
    d.type("\n")
    d.delay(2)
    #d(class_name="Button",name="Go").click()
    #d(class_name="Button",lable="登录").click()


    #d.delay(3)

    d.click_image("shezhi.2048x1536.png")
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="ipad nav close").click()
    d.delay(1)
    d(class_name="Button",label="wp nav back").click()
    d.delay(1)
    print "第16个步骤执行完成"
except Exception:
    fn()   
finally:
    
    print "done"
#-----------------------------------------------------------
try:
    
    d(class_name="Button",label="ipad nav search bg").click()
    d.type(u"城市")
    d.type("\n")
    d(class_name="Button",label="wp nav back").click()
    d(class_name="Button",label="返回").click()
    print "第17个步骤执行完成"
except Exception:
    fn()   
finally:
    
    print "done"
#-----------------------------------------------------------



    
d.stop_app()
rp.close()



