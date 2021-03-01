from rest_framework import serializers

from books.models import Book, Author, Client, Borrow
from books.utils import days_between_today_and_param


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name']
        read_only_fields = ['id_author']


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['id_client']


class BorrowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'
        read_only_fields = ['id_borrow']


class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id_book', 'book_title', 'date_booking', 'author']
        read_only_fields = ['id_book']


class BookDetailSerializer(BookSerializer):

    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        if obj.borrow_set and obj.borrow_set.filter(book_id=obj.id_book):
            return 'Emprestado'
        return 'Disponível'

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ['status']


class BookClientSerializer(serializers.ModelSerializer):

    book = BookSerializer()
    days_of_delay = serializers.SerializerMethodField()
    fine_rate = serializers.SerializerMethodField()

    def get_days_of_delay(self, obj):
        #nessa solucao, imaginamos um cenario de que o prazo de entrega do livro seria de 10 dias.
        days_borrow = days_between_today_and_param(obj.date_borrow)
        if days_borrow <= 10:
            return 0
        return days_between_today_and_param(obj.date_borrow)

    # multa
    # nessa solucao, imaginamos um cenario de que o prazo de entrega do livro seria de 10 dias e valor de multa: 5 reais
    def get_fine_rate(self, obj):
        fine_rate = 5.00
        days_borrow = days_between_today_and_param(obj.date_borrow)
        if days_borrow in range(11, 14):
            value = fine_rate + (fine_rate * 3 / 100)
            return self.sum_percent_by_day(0.2, value, days_borrow)
        elif days_borrow in range(13, 16):
            value = fine_rate + (fine_rate * 5 / 100)
            return self.sum_percent_by_day(0.4, value, days_borrow)
        elif days_borrow > 15:
            value = fine_rate + (fine_rate * 7 / 100)
            return self.sum_percent_by_day(0.6, value, days_borrow)
        return 0.00

    class Meta:
        model = Book
        fields = ['book', 'days_of_delay', 'fine_rate',]

    def sum_percent_by_day(self, percent, value, days_borrow):
        for val in range(0, days_borrow - 10):
            value = value + (value * percent / 100)
        return float("%.2f" % value)
