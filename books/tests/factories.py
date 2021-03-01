import random

import factory

from faker import Faker
from factory.django import DjangoModelFactory

from books.models import Book, Author

fake = Faker('pt_BR')


class AuthorFactory(DjangoModelFactory):

    class Meta:
        model = Author

    id_author = random.randint(1, 99999)
    name = fake.name()


class BookFactory(DjangoModelFactory):

    class Meta:
        model = Book

    id_book = random.randint(1, 99999)
    book_title = fake.name()
    author = factory.SubFactory(AuthorFactory)
