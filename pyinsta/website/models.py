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
	profile = models.ImageField(upload_to ='img/profiles/%Y/%m/%d/', default='img/cage.jpg')

	def __str__(self):
		return str(self.person)

class Blog(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.account)

class Post(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	image = models.ImageField(upload_to ='img/posts/%Y/%m/%d/', default='img/cage.jpg')
	text = models.CharField(max_length = 200, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.')
	def __str__(self):
		return str(self.blog)

