import random
import datetime

import factory

from faker import Faker
from factory.django import DjangoModelFactory

from books.models import Book, Author, Client, Borrow

fake = Faker('pt_BR')


class AuthorFactory(DjangoModelFactory):

    class Meta:
        model = Author

    id_author = random.randint(1000, 99999)
    name = fake.name()


class BookFactory(DjangoModelFactory):

    class Meta:
        model = Book

    id_book = random.randint(1000, 99999)
    book_title = fake.name()
    author = factory.SubFactory(AuthorFactory)


class ClientFactory(DjangoModelFactory):

    class Meta:
        model = Client

    id_client = random.randint(1000, 99999)
    name = fake.name()
    active = True


class BorrowFactory(DjangoModelFactory):

    class Meta:
        model = Borrow

    id_borrow = random.randint(1000, 99999)
    date_borrow = datetime.datetime(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 28))
    date_devolution = None

    book = factory.SubFactory(BookFactory)
    client = factory.SubFactory(ClientFactory)
