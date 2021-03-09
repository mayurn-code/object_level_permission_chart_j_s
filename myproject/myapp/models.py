from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    CHOISE_Field=[
        ("Tata","Tata"),
        ("ford","ford"),
        ("mahindra","mahindra"),
        ("hundai","hundai"),
    ]
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=50,choices=CHOISE_Field)
    model_no = models.CharField(max_length=20)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        permissions =[
            ('can_view_brand_name_only','Can View Brand Name Only'),
            ('can_view_model_no','Can View Model No')
        ]


class Application(models.Model):
    name = models.CharField(max_length=40)
    details = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name