import json
from datetime import datetime, timedelta


from rest_framework import status

from books.tests.factories import BookFactory, BorrowFactory, ClientFactory


def test_select_books(customer_client):
    book = BookFactory()
    response = customer_client.get(f"/v1/books/", content_type="application/json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert book.id_book == json.loads(response.content)[0].get('id_book')


def test_reserve_book(customer_client):
    book = BookFactory()
    response = customer_client.get(f"/v1/books/{book.id_book}/reserve/", content_type="application/json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert book.id_book == json.loads(response.content).get('id_book')


def test_find_by_client_17_days_delay(customer_client):
    book = BookFactory()
    client = ClientFactory()
    date_borrow = datetime.today() - timedelta(days=17)
    borrow = BorrowFactory(client=client, book=book, date_borrow=date_borrow)
    response = customer_client.get(f"/v1/client/{client.id_client}/books/", content_type="application/json")

    # THEN
    content = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert content.get('days_of_delay') == 17
    assert content.get('fine_rate') == 5.58


def test_find_by_client_11_days_delay(customer_client):
    book = BookFactory()
    client = ClientFactory()
    date_borrow = datetime.today() - timedelta(days=11)
    borrow = BorrowFactory(client=client, book=book, date_borrow=date_borrow)
    response = customer_client.get(f"/v1/client/{client.id_client}/books/", content_type="application/json")

    # THEN
    content = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert content.get('days_of_delay') == 11
    assert content.get('fine_rate') == 5.16


def test_find_by_client_10_days_delay(customer_client):
    book = BookFactory()
    client = ClientFactory()
    date_borrow = datetime.today() - timedelta(days=10)
    borrow = BorrowFactory(client=client, book=book, date_borrow=date_borrow)
    response = customer_client.get(f"/v1/client/{client.id_client}/books/", content_type="application/json")

    # THEN
    content = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert content.get('days_of_delay') == 0
    assert content.get('fine_rate') == 0.0


def test_find_by_client_14_days_delay(customer_client):
    book = BookFactory()
    client = ClientFactory()
    date_borrow = datetime.today() - timedelta(days=14)
    borrow = BorrowFactory(client=client, book=book, date_borrow=date_borrow)
    response = customer_client.get(f"/v1/client/{client.id_client}/books/", content_type="application/json")

    # THEN
    content = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert content.get('days_of_delay') == 14
    assert content.get('fine_rate') == 5.33
