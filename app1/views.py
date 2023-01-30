from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import SignupForm,LoginForm,UpdateForm,ChangePasswordForm,ImageUploadForm
from . models import Signup,Image
from django.contrib.auth import logout as logouts


# Create your views here.
def hello(request):
    return HttpResponse('Welcome to dj')

def index(request):
    name='nikhil k'
    return render(request,'index.html',{'data':name})

# def signup(request):
#     form=SignupForm()
#     return render(request,'signup.html',{'form':form})

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'User already exists')
                return redirect('/signup')
            elif password!=confirmpassword:
                messages.warning(request,'password mismath')
                return redirect('/signup')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,'Account created succesfully')
                return redirect('/')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Signup.objects.get(Email=email)
                if not user:
                    messages.warning(request,'User does not exists')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'password incorrect')
                    return redirect('/login')
                else:
                    messages.success(request,'Login succesfull')
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,'Email or Password Incorrect')
                return redirect('/login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def home(request,id):
    user=Signup.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def showusers(request):
    users=Signup.objects.all()
    return render(request,'showusers.html',{'users':users})

def delete(request,id):
    User=Signup.objects.get(id=id)
    User.delete()
    messages.success(request,"User Deleted")
    return redirect('/showusers')

def update(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Update Succesful')
            return redirect('/showusers')
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form})

def changepassword(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmnewpassword=form.cleaned_data['ConfirmNewPassword']
            if oldpassword!=user.Password:
                messages.warning(request,'Old Password incorrect')
                return redirect('/changepassword/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,'New Password Matches The Old Password')
                return redirect('/changepassword/%s' % user.id)
            elif newpassword!=confirmnewpassword:
                messages.warning(request,'New Password And Confirm Password Does Not Match')
                return redirect('/changepassword/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,'Password Change Succesful')
                return redirect('/home/%s' % user.id)
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'user':user})

def logout(request):
    logouts(request)
    messages.success(request,'Logout Succesful')
    return redirect('/')

def uploadimage(request):
    if request.method=='POST':
        form=SignupForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Upload Succesul')
            return redirect('/')
    else:
        form=ImageUploadForm()
    return render(request,'uploadimage.html',{'form':form})

def showimage(request):
    images=Image.objects.all()
    return render(request,'showimage.html',{'images':images})
    