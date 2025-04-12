from django.db import models


class PortfolioDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    skills = models.TextField()
    role = models.TextField()
    experience = models.TextField()
    projects = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

