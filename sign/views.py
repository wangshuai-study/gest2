from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
#写django功能的处理逻辑

# 首页
def index(request):
    # return HttpResponse("aaaaaaaaaaaaaaaaaaa")
    # return HttpResponse("")
    return render(request,"index.html")


# 登录处理
def login_action(request):
    print(request.method)
    if request.method == "POST":
        # 获取前端提交参数
        # login_username = request.GET.get("username")
        login_username = request.POST.get("username")
        # login_password = request.GET.get("username")
        login_password = request.POST.get("password")
        print(login_username)
        print(login_password)
        if login_username == "" or login_password == "":
            return render(request,"index.html",{"error":"username or password is null"})
        else:
            user = auth.authenticate(username = login_username,password = login_password)
            if user is not None:
                auth.login(request,user) #验证登录
            # elif  login_username== 'admin' and login_password == '123':
                # HttpResponseRedirect 跳转
                # return HttpResponseRedirect("/event_manage/")
                response = HttpResponseRedirect("/event_manage/")
                # 设置cookie   时效时间 10s
                # response.set_cookie("user",login_username,10)
                request.session["user"] = login_username #将session 信息记录到服务器
                return response
            # return HttpResponse("evemt_manage.html========logout success")
            # return render(request,"event_manage.html")
            else:
                return render(request,"index.html",{"error":"username or password error"})
    elif request.method == "GET":
        return render(request, "index.html")

#跳转页
#发布会管理
@login_required
def event_manage(request):
    # return HttpResponse("跳转到event_manage")

    # 读取浏览器cookie
    username = request.COOKIES.get("user","")

    # 读取浏览器session
    username = request.session.get("user","")

    return render(request,"event_manage.html",{"user":username})
# 退出
@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect("/index/")
    return response
    # return render (request,"index.html",{"退出"})