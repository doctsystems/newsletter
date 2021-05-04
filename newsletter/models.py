from django.db import models

class Newsletter(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Subscriber(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	newsletter = models.ManyToManyField(Newsletter, through='Subscription')

	def __str__(self):
		return self.name

class Issue(models.Model):
	content = models.TextField()
	title = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Subscription(models.Model):
	newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
	subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.subscriber} Subscribed to {self.newsletter}"


		