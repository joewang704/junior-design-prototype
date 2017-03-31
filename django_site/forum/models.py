from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.forms import MultipleChoiceField
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
from django.db.models.signals import post_save
from django.dispatch import receiver


# https://blogs.gnome.org/danni/2016/03/08/multiple-choice-using-djangos-postgres-arrayfield/
class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ALZHEIMER = 'alzheimer'
    PARKINSON = 'parkinson'
    CANCER = 'cancer'
    DISEASE_CHOICES = (
        (ALZHEIMER, 'Alzheimer'),
        (PARKINSON, 'Parkinson'),
        (CANCER, 'Cancer'),
    )
    disease_interests = ChoiceArrayField(
        models.CharField(max_length=30, choices=DISEASE_CHOICES),
        default=['parkinson']
    )
    is_patient = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Forum(models.Model):
     title = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    text = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


