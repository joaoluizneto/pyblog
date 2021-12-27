from django.contrib import admin
from . import models as mod

model_classes = [cls for name, cls in mod.__dict__.items() if isinstance(cls, type)]

# Register your models here.
for model_class in model_classes: admin.site.register(model_class)

