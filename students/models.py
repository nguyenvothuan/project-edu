from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.


class Student(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    school = models.CharField(max_length=100, blank=True)
    
    # if not self.check_role(user, self.role):
    #                 return Response({'status': False,
    #                              'message': "User's %s is false" % self.role},
    #                             status=status.HTTP_400_BAD_REQUEST)