from django.shortcuts import render, redirect
from .models import Companyreg, Add_Agent
from .models import Add_Company
from .models import Customer_Registration
from .models import Shares_Add
from .models import Feedback
from .models import Suggesstion
# Create your views here.
def companyregi(request):
    email=request.POST['id']
    password=request.POST['password']
    Companyreg(email=email,password=password).save()
    return render(request,'company.html',{'message':'registered successfully'})


def companylogin(request):
    dd = request.POST['id']
    password = request.POST['password']
    qs=Companyreg.objects.filter(userid=dd,password=password)
    cr=Customer_Registration.objects.filter(name=dd,password=password)
    co=Add_Company.objects.filter(name=dd,password=password)
    ag=Add_Agent.objects.filter(name=dd,password=password )
    if qs:
        return render(request, "admin_login.html")
   # return render(request,"index.html",{"msg":"invalid details"})
    elif co :
        return render(request, "company_login.html")
    elif cr:
        return render(request, "customer_login.html")
    elif ag:
        return render(request, "agent_login.html")
    else:
        return render(request, "index.html", {"msg": "invalid details"})

def add_company(request):


    name=request.POST['name']
    symbol=request.POST['symbol']
    password=request.POST['password']
    email=request.POST['email']
    address=request.POST['address']
    phonenumber=request.POST['phonenumber']
    select=request.POST['select']
    image=request.FILES['image']

    qs = Add_Company(name=name,symbol=symbol,password=password,email=email,address=address,phonenumber=phonenumber,select=select,image=image)
    qs.save()

    return render(request, "add_company.html",{'msg':'details inserted'})


def openupdatecompany(request):
    id = request.GET.get('id')
    qs = Add_Company.objects.get(id=id)
    return render(request,'update_change.html',{'qs':qs})

def update_Comp(request):
    id = request.GET.get('id')
    name = request.POST.get("name")
    symbol = request.POST.get('symbol')
    password = request.POST.get('password')
    email = request.POST.get('email')
    address = request.POST.get('address')
    phonenumber = request.POST('phonenumber')
    select = request.POST.get('select')
    image = request.FILES['image']
    Add_Company.objects.get(id=id).update(name=name,symbol=symbol,password=password,email=email,address=address,phonenumber=phonenumber,select=select,image=image)
    qs=Add_Company.objects.all()
    return render(request, 'view_companies.html', {'qs': qs})


def add_agent(request):
    id=request.POST['id']
    name=request.POST['name']
    password=request.POST['password']
    email=request.POST['email']
    address=request.POST['address']
    phonenumber=request.POST['phonenumber']
    image=request.FILES['image']

    qs = Add_Agent(id=id,name=name,password=password,email=email,address=address,phonenumber=phonenumber,image=image)
    qs.save()

    return render(request, "add_agent.html",{'msg':'details inserted'})


def openupdateagent(request):
    id=request.GET['id']
    qs =Add_Agent.objects.get(id=id)
    return render(request,'updateagent_change.html',{'qs':qs})


def delete_comp(request):

    qs = Add_Company.objects.all()
    if qs:
        return render(request,'delete_company.html',{'data':qs})
    else:
        return render(request,'delete_company.html',{'msg':'No data '})


def delete(request):
    id = request.GET['id']
    qs = Add_Company.objects.get(id=id).delete()

    qs1=Add_Company.objects.all()
    if qs:
        return render(request,'delete_company.html',{'msg':'Company Deleted','data':qs1})
    else:
        return render(request,'delete_company.html',{'qs':qs})

def delete_agent(request):

    qs = Add_Agent.objects.all()
    if qs:
        return render(request,'delete_agent.html',{'data':qs})
    else:
        return render(request,'delete_agent.html',{'msg':'No data '})


def deleteagent(request):
    id = request.GET['id']
    qs = Add_Agent.objects.get(id=id).delete()

    qs1=Add_Agent.objects.all()
    if qs:
        return render(request,'delete_agent.html',{'msg':'Agent Deleted','data':qs1})
    else:
        return render(request,'delete_agent.html',{'qs':qs})


def customereg(request):


    id=request.POST['id']
    name = request.POST['name']
    # symbol = request.POST['symbol']
    password = request.POST['password']
    email = request.POST['email']
    address = request.POST['address']
    phonenumber = request.POST['phonenumber']

    image = request.FILES['image']

    qs = Customer_Registration(id=id,name=name, password=password, email=email, address=address, phonenumber=phonenumber,
                      image=image)
    qs.save()

    return render(request, "customer_reg.html", {'msg': 'details inserted'})


def updatedcompant(request):
    name = request.POST['name']
    symbol = request.POST['symbol']
    password = request.POST['password']
    email = request.POST['email']
    address = request.POST['address']
    phonenumber = request.POST['phonenumber']
    select = request.POST['select']
    image = request.FILES['image']

    qs = Add_Company(name=name, symbol=symbol, password=password, email=email, address=address, phonenumber=phonenumber,
                     select=select, image=image)
    qs.save()

    return redirect('/update_company/')

def updatedagnt(request):
    name = request.POST['id']
    name = request.POST['name']
    symbol = request.POST['symbol']
    password = request.POST['password']
    email = request.POST['email']
    address = request.POST['address']
    phonenumber = request.POST['phonenumber']
    select = request.POST['select']
    image = request.FILES['image']

    qs = Add_Agent(id=id, name=name, symbol=symbol, password=password, email=email, address=address, phonenumber=phonenumber,
                     select=select, image=image)
    qs.save()

    return redirect('/update_agent/')




def openudatedcustomer(request):
    id = request.GET['id']
    qs = Customer_Registration.objects.get(id=id)
    return render(request, 'update_changecustomer.html', {'qs': qs})


#company

def add_share(request):
    id = request.POST['id']
    name = request.POST['name']
    symbol = request.POST['symbol']
    price=request.POST['price']
    select=request.POST['select']
    qs = Shares_Add(id=id, name=name, symbol=symbol, price=price, select=select)
    qs.save()

    return render(request, "add_share.html", {'msg': 'Shares Added'})


def updatedshares(request):
    id = request.POST['id']
    name = request.POST['name']
    symbol = request.POST['symbol']
    email = request.POST['email']
    price = request.POST['price']
    select = request.POST['select']

    qs = Shares_Add(id=id, name=name, symbol=symbol, price=price, select=select,)
    qs.save()

    return redirect('/update_shares/')


def openupdatedshares(request):
    id = request.GET['id']
    qs = Shares_Add.objects.get(id=id)
    return render(request, 'update_sharechange.html', {'qs': qs})

def delete_shar(request):

    qs = Shares_Add.objects.all()
    if qs:
        return render(request,'delete_shares.html',{'data':qs})
    else:
        return render(request,'delete_shares.html',{'msg':'No data '})


def deleteshare(request):
    id = request.GET['id']
    qs = Shares_Add.objects.get(id=id).delete()

    qs1=Shares_Add.objects.all()
    if qs:
        return render(request,'delete_shares.html',{'msg':'Company Deleted','data':qs1})
    else:
        return render(request,'delete_shares.html',{'qs':qs})

def feedbacksave(request):
    email=request.POST.get('email')
    name=request.POST.get('name')
    feedback=request.POST.get('feedback')
    Feedback(email=email, name=name, feedback=feedback).save()
    return render(request,'feedback.html',{'msg':'feedback submitted'})


def deletefeedback(request):
    email=request.GET.get('name')
    Feedback.objects.get(email=email).delete()
    qs=Feedback.objects.all()
    return render(request,'adminfeedback..html',{'msg':'Feedback Deleted',"object_list":qs})


def suggessionsave(request):
    email=request.POST.get('email')
    name=request.POST.get('name')
    suggestion=request.POST.get('suggesstion')
    Suggesstion(email=email,name=name,suggession=suggestion).save()
    return render(request,'suggession.html',{'msg':'suggession submitted'})

def deletesuggession(request):
    email = request.GET.get('name')
    Suggesstion.objects.get(email=email).delete()
    qs = Suggesstion.objects.all()
    return render(request, 'adminsuggession.html', {'msg': 'suggession Deleted', "object_list": qs})


def searchcompanies(request):
    search=request.POST.get('search')
    sc=Add_Company.objects.filter(name=search)
    return render(request, 'searchcompany.html',{'data':sc})


def addshare_customer(request):
    id = request.POST['id']
    name = request.POST['name']
    price= request.POST['price']
    quantity=request.POST['quantity']
    Shares_Add(id=id, name=name,price=price,quantity=quantity).save()
    return render(request,'buy.html',{'msg':'shares bought'})


def sellshare_customer(request):
    id = request.POST['id']
    name = request.POST['name']
    price = request.POST['price']
    quantity = request.POST['quantity']
    Shares_Add(id=id, name=name, price=price, quantity=quantity).save()
    return render(request, 'sell.html', {'msg': 'shares sold'})


