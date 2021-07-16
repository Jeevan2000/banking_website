from django.core.checks.messages import Error
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import NewCustomer,TransactionHistory
from django.contrib import messages
from datetime import date, datetime
# Create your views here.
def home(request):
    return render(request,'home.html')

def customers(request):
    
    cust=NewCustomer.objects.all()
    return render(request,'customer.html',{'custs':cust})

def transactionhistory(request):
    tran=TransactionHistory.objects.all()
    return render(request,'transaction.html',{'hist':tran})

def custinfo(request,id):
    data=NewCustomer.objects.filter(id=id)
    #print(data)
    
       

    if request.method == 'GET':
        return render(request,'custinfo.html',{'info':data}) 

    if request.method == 'POST':
        acno=int(request.POST['acno'])
        recename=request.POST['receiptname']
        amount=request.POST['amount']
        flag=0
        sender=NewCustomer.objects.get(id=id)
        sender_id=int(sender.id)
        sender_name=str(sender.name)
        x3=sender.balance
        try:
            check_acno=NewCustomer.objects.get(id=acno)
        except:
            return render(request,'custinfo.html',{'customer':sender,'invalid_account_num':1,'cur_cust_id':acno,'info':data})

            
        #check_name=Customer.objects.get(name=recename)
        x1=check_acno.id
        x2=check_acno.name
        
        
        
        if (str(x1)==str(acno)) and (str(x2)==str(recename)):
            pass
        else: 
            return render(request,'custinfo.html',{'customer':sender,'invalid_account_name':1,'cur_cust_id':acno,'info':data})
        
        if int(amount)<=0:
            return render(request,'custinfo.html',{'customer':sender,'lessthanzero':1,'curr_cust_id':acno,'info':data})
        if int(amount)>int(x3):
            return render(request,'custinfo.html',{'customer':sender,'insufficientbalance':1,'curr_cust_id':acno,'info':data})  

        
        sender.balance=sender.balance -int(amount)
        sender.save()
        check_acno.balance=check_acno.balance+int(amount)
        check_acno.save()
        
        now=datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        #print("date and time =", dt_string)
        TransactionHistory(sender_id=sender_id, sender_name=sender_name, receiver_id=int(acno), receiver_name=str(recename), 
        amount_fee=int(amount), time=dt_string).save()

        return render(request,'custinfo.html',{'customer':sender,'successful':1,'curr_id':acno,'info':data})      
        

