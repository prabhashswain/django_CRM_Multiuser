from django.contrib.auth.models import Group,User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Customer


@receiver(post_save,sender=User)
def create_customer_profile(sender,instance,created,*args,**kwargs):
    if created:
        #adding user to customer group
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        #adding customer profile
        Customer.objects.create(
            user = instance,
            name = instance.username
        )
        print("Profile Created Successfully!!!!")