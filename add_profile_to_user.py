from forum.models import Profile
from django.contrib.auth.models import User
users = User.objects.all().select_related('profile')
for a_user in users:
    a_user.profile = Profile.objects.create(user=a_user)


