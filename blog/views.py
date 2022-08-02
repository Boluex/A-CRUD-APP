from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponse
from.forms import renew,reply

import requests
from django.contrib.sites.shortcuts import get_current_site
from.models import post,comment
from django.contrib.auth.views import login_required
# Create your views here.
@login_required(login_url='sign_in')
def create(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        pic=request.POST.get('pic')
        new_post=post(author=request.user,title=title,content=content,image=pic)
        new_post.save()
        return redirect('/')
    return render(request,'blog/create.html')
@login_required(login_url='sign_in')
def home(request):
    posts=post.objects.all()
    url=get_current_site(request)
    # obj('http://127.0.0.1:8000/')
    return render(request,'blog/home.html',{'posts':posts})
@login_required(login_url='sign_in')
def detail(request,id):
    detail_post=post.objects.get(id=id)
    return render(request,'blog/detail.html',{'post':detail_post})
@login_required(login_url='sign_in')
def delete(request,id):
    delete_post = post.objects.get(id=id)
    if request.user==delete_post.author:
        delete_post.delete()
        messages.success(request,'Deleted successfully')
        return redirect('/')
    else:
        messages.error(request,"Operation denied")
        return redirect('/')
@login_required(login_url='sign_in')
def update(request,id):
    current_post=post.objects.get(id=id)
    if request.method == 'POST':
        if current_post.author == request.user:
            form=renew(request.POST,request.FILES,instance=current_post)
            if form.is_valid():
                form.save()
                messages.success(request,'updated successfully')
                return redirect('/')
        else:
            messages.error(request, "Operation denied")
            return redirect('/')
    form=renew()
    return render(request,'blog/update.html',{'form':form})

@login_required(login_url='sign_in')
def comments(request,id):
    grab = post.objects.get(id=id)
    posts=comment.objects.filter(post=grab)
    return render(request,'blog/comment.html',{'comment':posts,'grab':grab})
@login_required(login_url='sign_in')
def add_comment(request,id):
    if request.method == 'POST':
        # post=request.POST.get('post_id')
        post_id=post.objects.get(id=id)
        content=request.POST.get('content')
        image=request.POST.get('pic')
        new_comment=comment(author=request.user,post=post_id,comment=content,image=image)
        new_comment.save()
        return redirect(reverse(comments, args=[id]))
    return redirect(reverse(comments,args=[id]))

@login_required(login_url='sign_in')
def update_comment(request,id):
    current_post = comment.objects.get(id=id)
    if request.method == 'POST':
        if current_post.author == request.user:
            form = reply(request.POST, request.FILES,instance=current_post)
            if form.is_valid():
                form.save()
                messages.success(request, 'updated successfully')
                return redirect('/')
        else:
            messages.error(request, "Operation denied")
            return redirect('/')
    form=reply()
    return render(request, 'blog/comment_update.html',{'form':form})

def about(request):
    return render(request,'blog/about.html')
@login_required(login_url='sign_in')
def destroy(request,id):
    if request.user==post.author:
        delete_post=comment.objects.get(id=id)
        delete_post.delete()
        messages.success(request,'Deleted successfully')
        return redirect(reverse(comments,args=[id]))
    else:
        messages.error(request,"Operation denied")
        return redirect('/')
