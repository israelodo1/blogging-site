from django.db import models
class blog(models.Model):
    title = models.CharField(max_length = 200)
    image = models.CharField(max_length =2025)
    content = models.TextField()
    description = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default = 0)

def _str_(self):
    return self.title  


class comment(models.Model):
    posts = models.ForeignKey(blog, related_name="comments", on_delete=models.CASCADE)
    names = models.CharField(max_length = 300 ) 
    emails =  models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    
