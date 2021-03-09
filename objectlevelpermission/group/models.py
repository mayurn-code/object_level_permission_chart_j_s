from django.db import models


"""
It is a Customer Class 
For The Making Table in Database.
"""
class Customer(models.Model):
    ChoiceField=[
        ("Application1","Application1"),
        ("Application2","Application2"),
        ("Application3","Application3"),
        ("Page1","Page1"),
        ("Page2","Page2"),
        ("Page3","Page3"),
    ]
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    mobile = models.CharField(max_length=10,null=True, blank=True)
    other = models.CharField(max_length=15,choices=ChoiceField)
    query = models.CharField(max_length=300,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name