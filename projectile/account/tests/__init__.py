import factory
import random
from .. models import Account
from django.utils import timezone

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    date = factory.Faker('date_time', tzinfo=timezone.utc)
    head = factory.Faker('first_name')
    amount = random.randint(10, 12)
    method = factory.Faker('first_name')