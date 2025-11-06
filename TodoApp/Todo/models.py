from django.db import models

class Todo(models.Model):
    # Todo fields
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # arragement based on recently created
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
