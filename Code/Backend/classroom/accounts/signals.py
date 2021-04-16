# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import StudentProfile, FacultyProfile


# @receiver(post_save, sender= User)
# def create_user_profile( sender, instance, created, **kwargs):
#     print('Account create Demo',created)
#     if instance.is_student:
#         StudentProfile.objects.get_or_create(user= instance)
#     else:
#         FacultyProfile.objects.get_or_create(user= instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print('Saving account')
#     if instance.is_student:
#         instance.student_profile.save()
#     else:
#         FacultyProfile.objects.get_or_create(user= instance)