from rest_framework import status

from books.tests.factories import BookFactory


def test_select_books(customer_client):
    book = BookFactory()
    response = customer_client.get(f"/v1/books", content_type="application/json")

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
