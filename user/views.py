from django.shortcuts import render,redirect,get_object_or_404
from.forms import User_form
from.models import User
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = User_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            print(form.errors)
    else:
        form = User_form()
    return render(request,'create.html',{'form':form})

# def read(request):
#     users = User.objects.all()
#     return render(request,'list.html',{'users':users})

def details(request,pk):
    user = get_object_or_404(User,pk=pk)
    return render(request,'details.html',{'user':user})

def update(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = User_form(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('details',pk=user.pk)
        else:
            print(form.errors)
    else:
        form = User_form(instance=user)
    return render(request,'update.html',{'form':form})

def delete(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('list')
    return render(request,'delete.html',{'user':user})
