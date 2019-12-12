from django.db import models

# Create your models here.

class Mentee(models.Model):
    foto_mentee = models.CharField(max_length=200,default="")
    nama_mentee = models.CharField(max_length=200,default="")
    quote_mentee = models.CharField(max_length=200,default="")

    def __str__ (self):
        return self.nama_mentee
        
class Mentor(models.Model):
    foto_mentor = models.CharField(max_length=200,default="")
    nama_mentor = models.CharField(max_length=200,default="")
    pengalaman_mentor = models.CharField(max_length=200,default="")
    quote_mentor = models.CharField(max_length=200,default="")

    def __str__ (self):
        return self.nama_mentor

class Blog(models.Model):
    foto_blog = models.CharField(max_length=200,default="")
    judul_blog = models.CharField(max_length=200,default="")
    isi_blog = models.TextField(default="")
    tanggal_blog = models.DateField("tanggal blog")

    def __str__ (self):
        return self.judul_blog