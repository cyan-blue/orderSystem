#coding:utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from systemofdingh.models import orderModel, User, orderDetailModel
from django.template import RequestContext
from systemofdingh.forms import orderForm, orderModelForm, UserForm, orderDetailForm
import datetime, json
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

def login(request):
    username=""
    print checkIsLogin(request)
    if checkIsLogin(request):
        response = HttpResponseRedirect('/order/home')
        return response
    elif request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username, password__exact = password)
            print user,username,password
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/order/home')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/order/login')
    else:
        uf = UserForm()
    return render_to_response('systemofdingh/login.html', {'uf': uf}, context_instance= RequestContext(request))

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('systemofdingh/register.html', {'uf': uf}, context_instance=RequestContext(req))

def home(request):
    # html = ""
    # username = request.COOKIES.get('username', '')
    # if checkIsLogin(request):
    #     # all_orders = orderModel.objects.all().order_by('staffName')[:5]
    #     all_orders = orderModel.objects.filter(staffName=username)
    #     context = {"all_orders": all_orders, "username": username}
    #     return render(request, "systemofdingh/home.html", context)
    # else:
    #     context = {"error_message": "Please login first"}
    #     return HttpResponseRedirect('/order/login')
    html = ""
    username = request.COOKIES.get('username', '')
    if checkIsLogin(request):
        # all_orders = orderModel.objects.all().order_by('staffName')[:5]
        all_orders = orderModel.objects.filter(staffName=username)
        paginator = Paginator(all_orders, 5)
        page = request.GET.get('page')
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)
        return render(request, "systemofdingh/home.html",  { "orders": orders, "username": username})
    else:
        context = {"error_message": "Please login first"}
        return HttpResponseRedirect('/order/login')


def modify(request, modify_id):
    ModifyorderModel=get_object_or_404(orderModel, pk=int(modify_id))
    return render(request, "systemofdingh/modify.html", {"context": ModifyorderModel})

def update(request, modify_id):
    orderModify=get_object_or_404(orderModel, pk=int(modify_id))
    if request.method == "POST":
        form=orderModelForm(request.POST, instance=orderModify)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/order/home')
    return render_to_response('systemofdingh/modify.html', {'form': orderModelForm(instance=orderModify)},
                              context_instance=RequestContext(request))

def delorder(request,del_id):
    print("del_id", str(del_id))
    orderdel=get_object_or_404(orderModel, orderID=str(del_id))
    orderdel.delete()
    return HttpResponseRedirect('/order/home')

@csrf_exempt
def add(request):
    username = request.COOKIES.get('username', '')
    if checkIsLogin(request):
        if request.method == 'POST':
            post = request.POST
            orderID = post['orderID']
            orderTitle = post['orderTitle']
            consigneeName = post['consigneeName']
            supplierId = post['supplierId']
            print supplierId
            storehouseId = post['storehouseId']
            purchaseType = post['purchaseType']
            businessDate = datetime.datetime.now()
            remarks = post['remarks']
            orderModel.objects.get_or_create(staffName=username, orderID=orderID, orderTitle=orderTitle, consigneeName=consigneeName,
                                             supplierId=supplierId, storehouseId=storehouseId, purchaseType=purchaseType,
                                             businessDate=businessDate, remarks=remarks, orderStatus="审核")
            return render(request, 'systemofdingh/addorderItem.html', {'orderID': orderID},
                          context_instance=RequestContext(request))
        else:
            form = orderForm()
        return render(request, 'systemofdingh/add.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/order/login')

@csrf_exempt
def addorderitem(request, order_id):
    username = request.COOKIES.get('username', '')
    if checkIsLogin(request):
        if request.method == 'POST':
            post = request.POST
            print request.POST['purchaseGoodID']
            purchaseGoodID = post['purchaseGoodID']
            purchaseGoodName = post['purchaseGoodName']
            standardID = post['standardID']
            standardName = post['standardName']
            unitPrice = post['unitPrice']
            quantityGoods = post['quantityGoods']
            totalPrice = int(unitPrice)*int(quantityGoods)
            print totalPrice
            print purchaseGoodID , purchaseGoodName
            orderDetailModel.objects.get_or_create(purchaseGoodID=purchaseGoodID, purchaseGoodName=purchaseGoodName,
                                                  standardID=standardID, standardName=standardName,
                                                  unitPrice=unitPrice, quantityGoods=quantityGoods,
                                                  orderID_id=order_id, totalPrice=str(totalPrice))
            return render(request, 'systemofdingh/addorderItem.html', {'orderID': order_id},
                          context_instance=RequestContext(request))


        return render(request, 'systemofdingh/addorderItem.html', {'orderID': order_id}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/order/login')


def add2(request):
    if request.method == "POST":
        form=orderModelForm(request.POST)
        if form.is_valid():
            print form.save()

            return HttpResponseRedirect('/order/home')
    return render_to_response('systemofdingh/add.html', {'form': orderModelForm()},context_instance=RequestContext(request))


#退出
def logout(request):
    print "here is logout"
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#检查是否登录
def checkIsLogin(request):
    username = request.COOKIES.get('username', '')
    print "checkIsLogin " + username
    if "username" in request.COOKIES:
        name=request.COOKIES["username"]
        html = "用户%s 的Cookies 没有超时" % name
        islogin = True
    else:
        dt = datetime.datetime.now() + datetime.timedelta(hours = int(1))
        name ="loker"
        html ="用户的Cookies 已经超时\n设置用户%s为登录回话,过去时间：%s" % (name,str(dt))
        response = HttpResponse(html)
        response.set_cookie("username", name, expires=dt)
        islogin = False
    return islogin

def detail(request, detail_id):
    orderdetail = orderDetailModel.objects.filter(orderID_id=detail_id)
    orderM = orderModel.objects.get(orderID=detail_id)
    orderStatus = orderM.orderStatus
    context = {"orderdetail": orderdetail, "detail_id": detail_id, "orderStatus": orderStatus}
    return render(request, "systemofdingh/details.html", context)


def CheckOrderExist(request):
    print request.is_ajax()
    response=HttpResponse()
    response['Content-Type']="text/javascript"
    # orderID1 = request.GET.get("orderID","")
    # orderM = orderModel.objects.get(orderID = "1")
    # print "orderID1" , orderID1
    # if request.GET.has_key("orderID"):
    orderIDFrompage = request.GET.get("orderID", "")
    result = {}
    print "orderIDFrompage ", orderIDFrompage
    orderM = orderModel.objects.filter(orderID = orderIDFrompage)
    print orderM
    if orderM:
        result = """{"result":true}"""
    else:
        result = """{"result":false}"""
    return HttpResponse(result)


def ajax_index(request):
    return render(request, 'testAjax.html')

def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')

def test(request):
    return render(request, "systemofdingh/testLayer.html")