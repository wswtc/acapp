from django.http import HttpResponse
def index(resquest):
    line1 = '<h1 style="text-align: center">我的第一个网页</h1>'
    line2 = '<img src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1698Xv.img?w=1920&h=1080&q=60&m=2&f=jpg">'
    line3 = '<hr>'
    line4 =' <a href="/play/">"进入游戏界面"</a>'
    return HttpResponse(line1+line2+line3+line4)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line2 = '<img src="https://th.bing.com/th/id/OIP.6t-noBxmJGGScMNSMbSX0gHaEK?pid=ImgDet&rs=1">'
    return HttpResponse(line1+line2)
# Create your views here.
