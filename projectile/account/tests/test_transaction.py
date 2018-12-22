import json
import random

from faker import Faker

from django.urls import reverse
from common.test_case import BoilerTestCase
from . import AccountFactory
from .. models import Account
from rest_framework.test import APIRequestFactory

class AccountListAPITest(BoilerTestCase):
    url = reverse('accounts-list')
    fake = Faker()
    print url
    def test_transaction_list_get(self):
        # ===========================================
        #  Check without login
        # ===========================================
        request = self.client.get(self.url)
        self.assertCredentialNotProvided(request)

        # ===========================================
        #  Check with login
        # ===========================================
        # login = self.client.login(password='testpass')
        # # login = self.client.login(phone=self.user.phone, password='testpass')
        # self.assertTrue(login)
        # print login
        transaction_object = AccountFactory.create_batch(2)
        print transaction_object[0].id
        transaction = Account.objects.all()
        print transaction
        # factory = APIRequestFactory()
        # request = factory.get(self.url)
        # print request.data