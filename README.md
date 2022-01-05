# Pyinsta

Documentando o desenvolvimento de um website de blogs.

Para um melhor entendimento de como o framework django funciona:

![Untitled](Pyinsta%20fb44be6ad67a4d3eb3b34a350c2b20ea/Untitled.png)

1. Criando projeto (com servidor web):
    
    ```bash
    django-admin startproject pyinsta
    
    #Comando que roda o servidor
    #python manage.py runserver
    ```
    
2. Criando App:
    
    ```bash
    python manage.py startapp website
    ```
    
    1. Criando modelos para os dados do nosso app:
        
        ```python
        from django.db import models
        
        # Create your models here.
        
        class Person(models.Model):
        	name = models.CharField(max_length = 100)
        	user_name = models.CharField(max_length = 20)
        	birth_date = models.DateTimeField()
        	def __str__(self):
        		return self.user_name
        
        class Account(models.Model):
        	person = models.ForeignKey(Person, on_delete=models.CASCADE)
        
        	def __str__(self):
        		return self.choice_text
        
        class Blog(models.Model):
        	account = models.ForeignKey(Account, on_delete=models.CASCADE)
        
        	def __str__(self):
        		return self.choice_text
        
        class Post(models.Model):
        	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
        	
        	def __str__(self):
        		return self.choice_text
        ```
        
    2. Criando as views do nosso app:
        
        ```python
        from django.shortcuts import get_object_or_404, render
        
        from .models import *
        
        # Create your views here.
        def index(request):
            latest_post_list = Post.objects.order_by('-pub_date')[:5]
            context = {'latest_post_list': latest_post_list}
            return render(request, 'website/index.html', context)
        ```
        
    
    c. Dando permissões do projeto para que ele possa administrar o app.
    
    ```python
    from django.contrib import admin
    from . import models as mod
    
    model_classes = [cls for name, cls in mod.__dict__.items() if isinstance(cls, type)]
    
    # Register your models here.
    for model_class in model_classes: admin.site.register(model_class)
    ```
    
    d. Criando URLs de redirecionamento para as views:
    
    - Criando o arquivo ***pyinsta/website/urls.py:***
        
        ```bash
        ***touch website/urls.py***
        ```
        
        ```python
        from django.urls import path
        
        from . import views
        
        app_name = 'website'
        urlpatterns = [
            # ex: /polls/
            path('', views.index, name='index'),
        ]
        ```
        
    1. Criando template:
        
        ```bash
        mkdir website/templates/website && touch website/templates/website/index.html
        ```
        
        ```html
        {% if latest_post_list %}
            <ul>
            {% for post in latest_post_list %}
                <li><a href="{% url 'website:detail' post.id %}">{{ post.question_text }}</a></li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No posts.</p>
        {% endif %}
        ```
        
3. Configurando app no projeto:
    1. Instalando a aplicação na config do projeto ***pyinsta/settings.py:***
        
        ```python
        # Application definition
        
        INSTALLED_APPS = [
            '**website.apps.WebsiteConfig**',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
        ```
        
    
    b. Configurando URLs para ocorrer o redirecionamento para o App:
    
    - Redirecionando para a url do app na cofig do projeto ***pyinsta/urls.py:***
        
        ```python
        from django.contrib import admin
        from django.urls import path, include
        
        urlpatterns = [
            path('website/', include('website.urls')),
            path('admin/', admin.site.urls),
        ]
        ```
        
    
    c. Criando usuário administrador do projeto:
    
    ```python
    python manage.py createsuperuser
    ```
    

---

## Como iniciar o projeto na sua máquina:

Basta ir ao terminal e executar o seguinte:

```python
blablala
```