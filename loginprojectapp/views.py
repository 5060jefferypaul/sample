import os
from django.shortcuts import render,redirect
from .models import itemDetails
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#HOME

def Home(request):
    return render(request,'Home.html')

#TEACHER

def signup(request):
    return render(request,'Signup T.html')

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('loginpage')
    else:
        return render(request,'Signup T.html')

def loginpage(request):
    return render(request,'Login T.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'WELCOME {username}')
			return redirect('Student')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('loginpage')
	else:
		#messages.info(request, 'Oops, Something went wrong.')
		return redirect('loginpage')

def about(request):
    return render(request,'About T.html') 

def logout(request):
	auth.logout(request)
	return redirect('Home')



#STUDENT

def Student(request):
    return render(request,'Student Form.html')

def student_details(request):
    if request.method == 'POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        aage=request.POST['age']
        dob=request.POST['date_of_birth']
        gen=request.POST['gender']
        quali=request.POST['qualifications']
        image=request.FILES.get('file')
        register=itemDetails(first_name=fname,last_name=lname,age=aage,date_of_birth=dob,gender=gen,qualifications=quali,image=image)
        print("Save data...")
        register.save()
        return redirect('student_showpage')
    
def student_showpage(request):
    showstudents=itemDetails.objects.all()
    return render(request,'Student Show Details.html',{'register':showstudents})

def student_editpage(request,pk):
    pr=itemDetails.objects.get(id=pk)
    return render(request,'Student Edit.html',{'register':pr})

def edit_student_details(request,pk):
    if request.method=='POST':
        pr=itemDetails.objects.get(id=pk)     
        pr.first_name=request.POST.get('first_name')
        pr.last_name=request.POST.get('last_name')
        pr.age= float(request.POST.get('age'))
        pr.date_of_birth= (request.POST.get('date_of_birth'))
        pr.gender=request.POST.get('gender')
        pr.qualifications=request.POST.get('qualifications')
        old=pr.image
        new=request.FILES.get('file')
        if old !=None and new==None:
            pr.image=old
        else:
            pr.image=new  
        pr.save()
        return redirect(student_showpage)
    return render(request,'Student Edit.html')

def deletepage(request,pk):
    Studentdetails=itemDetails.objects.get(id=pk)
    Studentdetails.delete()
    return redirect ('student_showpage')




# Create your views here.
