from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    kategoriya = models.ManyToManyField("Kategoriya", help_text="Вибери категорію статті")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def display_kategoriya(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ kategoriya.name for kategoriya in self.kategoriya.all()[:3] ])
    display_kategoriya.short_description = "Категорія"

class Kategoriya(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Введи назву категорії (Адміністрування або Програмування і тд.,тп.")
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name