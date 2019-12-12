from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Mentee, Mentor, Blog 

# Create your views here.
def index(request):
    return render(request, 'alfa/index.html',{})

def blog(request):
    blog_data = Blog.objects.all()
    return render(request, 'alfa/blog.html',{'blog_data' : blog_data})

def mentee(request):
    mentee_data = Mentee.objects.all()
    return render(request, 'alfa/mentee.html',{'mentee_data' : mentee_data})

def mentor(request):
    mentor_data = Mentor.objects.all()
    return render(request, 'alfa/mentor.html',{'mentor_data' : mentor_data})

def author(request):
    return render(request, 'alfa/author.html',{})

def form(request):
    return render(request, 'alfa/form.html',{})

def news(request):
    foto_blog = request.POST['form_image']
    judul_blog = request.POST['form_title']
    isi_blog = request.POST['form_content']
    tanggal_blog = request.POST['form_date']

    news = Blog(foto_blog=foto_blog, judul_blog=judul_blog, isi_blog=isi_blog, tanggal_blog=tanggal_blog)
    news.save()

    blog_data = Blog.objects.all()
    return render(request, 'alfa/blog.html',{'blog_data' : blog_data})

def BacaSelengkapnya(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'alfa/baca_selengkapnya.html', {'blog': blog})