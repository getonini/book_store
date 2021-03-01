from django.db import models


class DateTimeDBOps(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_cadastro'
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True,
        db_column='dt_atualizacao'
    )

    class Meta:
        abstract = True


class Author(DateTimeDBOps):
    id_author = models.BigAutoField(primary_key=True, db_column='id_autor')
    name = models.CharField(db_column='nome_autor', max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'autor'
        ordering = ['id_author']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Client(DateTimeDBOps):
    id_client = models.BigAutoField(primary_key=True, db_column='id_cliente')
    name = models.CharField(db_column='nome_cliente', max_length=255)
    active = models.BooleanField(db_column='ativo', default=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'cliente'
        ordering = ['id_client']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Book(DateTimeDBOps):
    id_book = models.BigAutoField(primary_key=True, db_column='id_livro')
    book_title = models.CharField(db_column='titulo_livro', max_length=255)
    date_booking = models.DateTimeField(db_column='dt_reserva', null=True, blank=True)

    author = models.ForeignKey(Author, db_column='id_autor', null=False, related_name='book_set',
                               on_delete=models.CASCADE)

    def __str__(self):
        return 'Book {}'.format(self.book_title)

    class Meta:
        db_table = 'livro'
        ordering = ['id_book']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


class Borrow(models.Model):
    id_borrow = models.BigAutoField(primary_key=True, db_column='id_emprestimo')
    date_borrow = models.DateTimeField(db_column='dt_emprestimo', null=True, blank=True)
    date_devolution = models.DateTimeField(db_column='dt_devolucao', null=True, blank=True)

    book = models.ForeignKey(Book, db_column='id_livro', null=False, related_name='borrow_set',
                             on_delete=models.CASCADE)
    client = models.ForeignKey(Client, db_column='id_cliente', null=True, related_name='borrow_set',
                               on_delete=models.CASCADE)

    def __str__(self):
        return 'Borrow {}'.format(self.id_borrow)

    class Meta:
        db_table = 'emprestimo'
        ordering = ['id_borrow']
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
