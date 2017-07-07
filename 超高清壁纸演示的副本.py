
# -*- coding:utf-8 -*-
import atx
import sys
import wda
import time
from atx.ext.report import Report # report lib
reload(sys)
sys.setdefaultencoding('utf8')
d = atx.connect('http://192.168.228.50:8100', platform='ios')
print d.status()
d.start_app('com.gao7.wallpaper.pid37ch03')
rp = Report(d, save_dir='report')

rp.patch_uiautomator() # for android UI test record (optional)
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

print "1.下滑操作"

#---------------------------------------


def test_bzd():
    
    print "下滑5次"


try:
    for i in range(1,6):
        swipeUp(0.1)
        print "向下滑动第",i,"次"
except Exception:
    fn()   
finally:
    print "done"
def test_top():
    print "1.验证置顶按钮"
try:
    buttotop= d(class_name="Button", name="list go top", label="list go top")
    rp.assert_ui_exists(d(name='list go top'), desc='顶部按钮出现' ,screenshot=True, safe=True)
    buttotop.click()
except Exception:
    fn()   
finally:
    print "done"



print "2、下载图片"
def test_down():
    print "验证下载图片"
try:
    d(className="Cell").click()
    rp.assert_ui_exists(d(className="Cell"), desc='需要下载的图' ,screenshot=True, safe=True)
    d.delay(3)
    d(class_name="Button", name="下载", label="下载").click()
    d(class_name="Button", name="wp img back", label="wp img back").click()
    d(class_name="Button", name="nav user", label="nav user").click()
    d(class_name="Button", name="我的壁纸", label="我的壁纸").click()
    rp.assert_ui_exists(d(name='我的下载'), desc='实际下载的图' ,screenshot=True, safe=True)
    d(class_name="Button", name="wp upload delete on", label="wp upload delete on").click()
    d(className="StaticText")[1].click()
    d(class_name="Button", name="删除", label="删除").click()
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
    d(class_name="Button", name="wp nav back white", label="wp nav back white").click()
except Exception:
    fn()   
finally:
    print "done"
def test_share():
    print "1.xxxxx"
try:
    d.delay(1)
    d(className="Cell").click()
    d(class_name="Button", name="img detail share up", label="img detail share up").click()
    
    d(class_name="Button", name="share weixin session", label="share weixin session").click()
    d(class_name="StaticText", name="创建新的聊天", label="创建新的聊天").click()
    d(class_name="StaticText", name="壁纸君(耀哥)", label="壁纸君(耀哥)").click()
    d(class_name="Button", name="确定(1)", label="确定(1)").click()
    d(class_name="Button", name="发送", label="发送").click()
    d(class_name="Button",label="返回壁纸-改变从壁纸开始").click()
except Exception:
    fn()   
finally:
    print "done"

#-----------------------------------------------------------
try:
    d(class_name="Button", name="img detail share up", label="img detail share up").click()
    d(class_name="Button", name="share weixin timeline", label="share weixin timeline").click()
    d.delay(1)
    d(class_name="Button",label="发送").click()
    d.delay(1)
    
except Exception:
    fn()   
finally:    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button", name="img detail share up", label="img detail share up").click()
    d(class_name="Button", name="share sina", label="share sina").click()
    d.delay(1)
    d(class_name="Button",label="发送").click()
    d.delay(1)
    
except Exception:
    fn()   
finally:
    print "done"
#---------------------------------------
try:
    d(class_name="Button", name="img detail share up", label="img detail share up").click()
    d(class_name="Button", name="share tencent qq", label="share tencent qq").click()
    d.delay(1)
    d(class_name="StaticText",name="陈冷耀-天志股份",label="陈冷耀-天志股份").click()
    d.delay(2)
    d(class_name="Button",label="发送").click()
    d.delay(2)
    d(class_name="StaticText",label="返回壁纸").click()
    d.delay(1)
    
except Exception:
    fn()   
finally:    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button", name="img detail share up", label="img detail share up").click()
    d(class_name="Button", name="share tencent space", label="share tencent space").click()
    d.delay(1)
    d(class_name="Button",label="发表").click()
    d.delay(1)
    print "第20个步骤执行完成"
except Exception:
    fn()   
finally:
    print "done"
#---------------------------------------
print "3、预览图片"
def test_look():
    print "点击桌面预览"
try:
    
    
    d(class_name="Button", name="预览", label="预览").click()
    rp.assert_ui_exists(d(name="桌面预览"), desc='桌面预览存在',screenshot=True, safe=True)
    d(class_name="Button", name="桌面预览", label="桌面预览").click()
    d.click(132, 568)
except Exception:
    fn()   
finally:
    print "done"

def test_lock():
    print "点击锁屏预览"
try:
    d(class_name="Button", name="预览", label="预览").click()
    rp.assert_ui_exists(d(name="锁屏预览"), desc='锁屏预览存在',screenshot=True, safe=True)
    d(class_name="Button", name="锁屏预览", label="锁屏预览").click()
    d.click(132, 568)
except Exception:
    fn()   
finally:
    print "done"
def test_jb():
    print "举报图片"
try:   
    d(class_name="Button", name="img detail info up", label="img detail info up").click()
    d(class_name="Button", name="举报", label="举报").click()
    rp.assert_ui_exists(d(name='图片缺失、错误'), desc='图片缺失、错误存在' ,screenshot=True, safe=True)
    d(class_name="Button", name="图片缺失、错误", label="图片缺失、错误").click()
    d(class_name="Button", name="img detail info up", label="img detail info up").click()
    d.delay(1)
    d(class_name="Button", name="wp img back", label="wp img back").click()
except Exception:
    fn()   
finally:
    print "done"

print "4、diy图片"
def test_diy():
    print "diy贴纸"
try:
    d.delay(1)
    d(class_name="Button", name="img detail diy", label="img detail diy").click()
    d(class_name="Button", name="贴纸", label="贴纸").click()
    d(class_name="Button", name="3", label="3").click()
    rp.assert_ui_exists(d(name="3"), desc='需要自制的图' ,screenshot=True, safe=True)
    d(class_name="Button", name="保存", label="保存").click()
    #d.click(254,123)
    #buttonexit=d(className="Button")[26]
    d(class_name="Button", name="分享", label="分享").click()
    d(class_name="Button", name="share close", label="share close").click()
    d(class_name="Button", name="取消", label="取消").click()
    d(class_name="Button", name="wp img back", label="wp img back").click()
    d(class_name="Button", name="nav user", label="nav user").click()
    d(class_name="Button", name="自制壁纸", label="自制壁纸").click()
    rp.assert_ui_exists(d(name='自制壁纸'), desc='实际自制的图' ,screenshot=True, safe=True)
    d(class_name="Button", name="wp upload delete on", label="wp upload delete on").click()
    d(class_name="Button")[6].click()
    d(class_name="Button", name="删除", label="删除").click()
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
    d(class_name="Button", name="wp nav back white", label="wp nav back white").click()
except Exception:
    fn()   
finally:
    print "done"


print "5、举报图片"


print "6、点击livephoto"
def test_lvphoto():
    print "预览livephoto"
try:
    d(class_name="StaticText", name="LivePhoto", label="LivePhoto").click()
    d(className="Cell").click()

    lvphotodowns = d(class_name="StaticText", name="- 长按体验LIVE PHOTO -", label="- 长按体验LIVE PHOTO -")

    d.delay(6)

    lvphotodowns.tap_hold(10)
    #d.swipe(m, n1, m,n2, 4)


    d(class_name="Button", name="wp img back", label="wp img back").click()
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
except Exception:
    fn()   
finally:
    print "done"

def test_ss():
    print "返回出去"
try:

    d(label="nav search", name="nav search", className="Button").click()

    cy=d(class_name="TextField")[0]
    cy.set_text(u"城市")
    d.type("\n")    
    d.delay(3)
    d(class_name="Button", name="网络图片",label="网络图片").click()
    rp.assert_ui_exists(d(text="城市"), desc='需要搜索的关键字' ,screenshot=True, safe=True)
    d.delay(1)
    d(class_name="Button", name="wp nav back",label="wp nav back").click()
    d(class_name="Button", name="取消",label="取消").click()
except Exception:
    fn()   
finally:
    print "done"

print "7 、进入用户个人中心页面"
def test_login():
    print "登录"
try:
    d(class_name="Button", name="nav user", label="nav user").click()
    d(label="img mine user").click()
    d.delay(2)
    btnname = d(class_name="TextField")
    btnname.set_text("lengyao")
    btnpass = d(class_name="SecureTextField")
    btnpass.set_text("lengyao")
    d(class_name="Button", name="登录", label="登录").click()
    rp.assert_ui_exists(d(text='登录成功'), desc='登录成功存在' ,screenshot=True, safe=True)
    d.delay(2)
except Exception:
    fn()   
finally:
    print "done"

print "8、上传壁纸"
def test_upload():
    print "上传壁纸"
try:
    d.delay(2)
    d(class_name="Button", name="上传壁纸",label="上传壁纸").click()
    d(class_name="Button", name="wp upload on", label="wp upload on").click()
    d(class_name="Button")[3].click()
    txtname = d(class_name="TextField")[0]
    txtname.set_text(u"壁纸上传测试")
    d(class_name="Button", name="发布", label="发布").click()
    d(class_name="Button", name="我同意以上条款", label="我同意以上条款").click()
    d(class_name="Button", name="我知道了", label="我知道了").click()
    d(class_name="Button", name="发布", label="发布").click()
except Exception:
    fn()   
finally:
    print "done"


print "9.返回出去"
def test_bk():
    print "返回出去"
try:
    d.delay(4)
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
    d.delay(2)
    #d(class_name="Button", name="wp nav back", label="wp nav back").click()
    #d.delay(1)
    #d(class_name="Button", name="wp nav back", label="wp nav back").click()
    
except Exception:
    fn()   
finally:
    print "done"

print "12、退出登录"
def test_esc():
    print "退出"
try:
   
    d(class_name="Button", name="img mine set", label="img mine set").click()
    swipeUp(0.2)
    d.delay(1)
    d(class_name="Button", name="退出登录", label="退出登录").click()
    d(class_name="Button", name="退出登录", label="退出登录").click()
    rp.assert_ui_exists(d(name='登出成功'), desc='登出成功存在' ,screenshot=True, safe=True)
    d.delay(3)
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
except Exception:
    fn()   
finally:
    print "done"

try:
    d(class_name="Button", name="img mine user", label="img mine user").click()

    d.delay(1)
    d(class_name="Button",label="腾讯QQ").click()
    d.delay(2)
    d(class_name="Button", name="img mine set", label="img mine set").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
    d.delay(1)
except Exception:
    fn()   
finally:
    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button", name="img mine user", label="img mine user").click()
    d.delay(1)
    d(class_name="Button",label="新浪微博").click()
    d.delay(2)
    d(class_name="Button", name="img mine set", label="img mine set").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
    print "第14个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"
#-----------------------------------------------------------
try:
    d(class_name="Button", name="img mine user", label="img mine user").click()
    d.delay(1)
    d(class_name="Button",label="微信").click()
    d.delay(2)
    d(class_name="Button",label="确认登录").click()
    d.delay(2)
    d(class_name="Button", name="img mine set", label="img mine set").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button",label="退出登录").click()
    d.delay(1)
    d(class_name="Button", name="wp nav back", label="wp nav back").click()
    d.delay(1)
    d.stop_app('com.gao7.wallpaper.pid37ch03')
    print "第15个步骤执行完成"
except Exception:
    fn()   
finally:    
    print "done"


def test_start():
    print "启动"
#d.start_app('com.iwall.pid67ch1')


   

# print "1、查看每日精选"
# def test_day():
#     print "每日精选"
# try:
#     d(class_name="Button",label="每日精选",name="每日精选").click()

#     stnow=d(class_name="StaticText",label=dv,name=dv)
#     rp.assert_ui_exists(d(name=dv), desc='日期符合:'+dv ,screenshot=True, safe=True)
    
#     for i in range(1, 13):
#         swipeUp(0.1)
#         print "向上滑动第", i, "次",   
#         numold = int(numday)- 1
#         numolds=str(numold)
#         old=numolds+datem+datey    
#         stnow1=d(class_name="StaticText",label=old,name=old)

#     rp.assert_ui_exists(d(name=old), desc='日期符合:'+old ,screenshot=True, safe=True)
#     print old
# except Exception:
#     fn()   
# finally:
#     print "done"

# print "2、选择图片"
# def test_bzd():

#     print "1、选择图片"
# try:
#     btnbk=d(label="nav back", name="nav back", className="Button")

#     btnbk.click()
#     d(label="星星好评")
#     d(label="分类").click()

#     d(label="我的关注",name="我的关注",class_name="StaticText").click()


#     buttond= d(class_name="Button")[15]
#     d(className="Button")[2].click()
#     #buttond= d(class_name="Button", name="阴阳师", label="阴阳师")
#     buttond.click()

#     for i in range(1, 2):
#         swipLeft(0.1)
#         d.delay(1)   
#         d(className="Button")[2].click()
#         d.delay(1)
#         print "向左滑动第", i, "次"
#     d(label="nav back").click()

# except Exception:
#     fn()   
# finally:
#     print "done"


# d.stop_app('com.iwall.pid67ch1')
rp.close()

