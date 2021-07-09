from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from departments.models import Department

# Расширение стандартного пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_of_user')

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    MENTOR = 'mentor'
    LEADER = 'leader'
    GUEST = 'guest'
    LOAN_ROLE = (
        (ADMIN, 'Админ'),
        (MODERATOR, 'Модератор'),
        (MENTOR, 'Наставник'),
        (LEADER, 'Руководитель'),
        (GUEST, 'Гость')
    )
    role_of_user = models.CharField(max_length=100, choices=LOAN_ROLE, db_index=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)

    def is_admin_or_moderator(self):
        if self.role_of_user == 'admin' or self.role_of_user == 'moderator':
            return True
        return False

    def is_not_guest(self):
        if self.role_of_user != 'guest':
            return True
        return False

    def is_not_guest_and_mentor(self):
        if self.role_of_user != 'guest' or self.role_of_user == 'mentor':
            return True
        return False

    def __str__(self):
        return self.user.__str__()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
