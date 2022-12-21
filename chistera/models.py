# -*-coding: UTF-8-*-
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    """
    Une équipe scrum est un ensemble de personnes qui travaillent sur un projet.
    """
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=150)

class Project(models.Model):
    """
    La représentation d'un projet dans le système.
    Un projet est pris en charge par une équipe.
    """
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=150)

class ProductBacklog(models.Model):
    """
    Un backlog produit Scrum contient un ensemble de user stories.
    Chaque backlog est systématiquement rattaché à un projet.
    """
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=150)

class Sprint(models.Model):
    """
	Le sprint est une itération en Scrum, réalisée par une équipe.
	Dand un sprint, une équipe peut travailler sur plusieurs projets.
    """
    team = models.ForeignKey(Team)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()

class UserStory(models.Model):
    """
    Une user story est une demande client.
    """
    product_backlog = models.ForeignKey(ProductBacklog)
    name = models.CharField(max_length=255)
    description = models.TextField()