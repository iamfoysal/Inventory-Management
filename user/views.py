from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom, UserForm 
from django.contrib import messages


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password= password)

        if user is not None:
            login (request, user)
            messages.success(request, "login successfully complete!!")
            return redirect('index')
        else:
            messages.error(request, "Password or User name is Wrong! Please try Again")
    return render(request, 'user/login.html')



def register(request):
    form = UserRegisterFrom ()
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created .")
            return redirect("signin")
    return render(request, 'user/register.html',{'form':form} )

@login_required
def profile_update(request):
    # profile = request.user.profile
    # form = UserForm(instance=profile)
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'Profile updated successfully.')
    else:
        form = UserForm(instance=request.user)
                
    context = {'form':form}
    return render(request, 'user/update-profile.html', context)

def signout(request):
    logout(request)
    messages.success(request, "logout Successfully Complete.")
    return redirect("signin")