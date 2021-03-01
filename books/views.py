import datetime

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from books.models import Book, Client, Borrow
from books.serializers import ClientSerializer, BookClientSerializer, BookDetailSerializer

__author__ = 'Guilherme Tonini'

from books.utils import days_between_today_and_param


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    serializer_class = BookDetailSerializer
    ordering = ('id',)

    def get_queryset(self):
        return Book.objects.filter(borrow_set__date_devolution__isnull=True).all()

    @action(detail=True, methods=['GET'])
    def reserve(self, request, pk):
        book = get_object_or_404(Book, id_book=pk)
        # esta validacao devido ao tempo de reserva ser de 3 dias

        if book.date_booking and days_between_today_and_param(book.date_booking) < 3:
            raise ValidationError("This book it's already reserved less than 3 days")
        book.date_booking = datetime.datetime.today()
        book.save()
        serializer = BookDetailSerializer(book, many=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ClientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    serializer_class = ClientSerializer
    ordering = ('id',)

    def get_queryset(self):
        return Client.objects.all()

    @action(detail=True, methods=['GET'])
    def books(self, request, pk):
        client = get_object_or_404(Client, id_client=pk)
        borrows = Borrow.objects.filter(client=client, date_devolution=None)
        if borrows:
            serializer = BookClientSerializer(borrows, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_200_OK, data="Don't have any barrow for this cliente.")
