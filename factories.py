from datetime import date

import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = 'Weid',
    last_name = 'Test',
    username = 'deni',
    email = 'wet@test.ru',
    password = '007777'
    birth_date = factory.Faker('date_object')

    class Meta:
        model = 'users.User'


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'test_name'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = 'ads.Selection'


class AdFactory(factory.django.DjangoModelFactory):
    name = 'Ad'
    author = factory.SubFactory(UserFactory)
    price = 1

    class Meta:
        model = 'ads.Ad'

