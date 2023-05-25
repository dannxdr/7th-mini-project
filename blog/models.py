import os

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    head_image = models.ImageField(blank=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True) #마지막으로 저장된 시점을 자동으로 저장
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    #updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.created_at}'
    
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):           #파일 경로는 제외하고 파일명만 나오게 함
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):            #확장자를 찾아냄
        return self.get_file_name().split('.')[-1] # a.b.txt =>  a  b  text ('.')을 기준으로 나눠짐



