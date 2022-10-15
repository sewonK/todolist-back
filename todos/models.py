from django.db import models
from django.utils import timezone
from accounts.models import User

class Todo(models.Model): 
    text = models.TextField()
    done = models.BooleanField(default=False) 
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

    def check_todo(self):
        self.done = True if self.done == False else False
        self.save()

    def __str__(self):
        return self.text