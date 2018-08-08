import factory
import random
from .. models import Transaction
from django.utils import timezone

class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    date = factory.Faker('date_time', tzinfo=timezone.utc)
    head = factory.Faker('first_name')
    amount = random.randint(10, 12)
    method = factory.Faker('first_name')