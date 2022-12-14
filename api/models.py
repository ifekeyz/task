from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


# Create your models here.
class Deposite(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    amount = models.IntegerField()

    @receiver(post_save, sender=User)
    def Createprofile(sender,instance,created, **kwargs):
        if created:
            user = instance
            profile = User.objects.create(
                user=user,
                name=user.first_name,
                email=user.email
            )
    

    

    # def __str__(self):
    #     return self.amount

class Withdraw(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    amount_to_withdraw = models.IntegerField()

    @receiver(post_delete, sender=User)
    def Withdraw(sender,instance, **kwargs):
        user = instance.user
        user.delete()


    def subtract(self):
        realBalance = Deposite.objects.filter(id=id)
        amount = Withdraw.objects.all()
        for item in realBalance:
            realBalance.amount -= amount.amount_to_withdraw
            return item

    

    def __str__(self):
        return self.user

class Balance(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return self.user

