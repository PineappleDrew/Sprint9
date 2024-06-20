import pytest
from main import BooksCollector


class TestBooksCollector:


    # тестируем добавление двух книг
    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # тест на добавление книг с разными жанрами
    @pytest.mark.parametrize('genre', ['Фэнтези', 'Драма'])
    def test_set_book_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')

        collector.set_book_genre('Гарри Поттер и философский камень', genre)

        assert collector.get_book_genre('Гарри Поттер и философский камень') == genre

    # тест на вывод списка книг с определенным жанром
    @pytest.mark.parametrize('genre, expected_result', [('Фантастика', ['Космическая одиссея', '2001 год', 'Солярис']),
                                                       ('Ужасы', ['Стрелок', 'Оно', 'Ведьмин хвост']),
                                                       ('Детективы', ['Сон']),
                                                       ('Мультфильмы', [])])
    def test_get_books_with_specific_genre(self, genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Космическая одиссея')
        collector.add_new_book('2001 год')
        collector.add_new_book('Стрелок')
        collector.add_new_book('Солярис')
        collector.add_new_book('Оно')
        collector.add_new_book('Сон')

        collector.set_book_genre('Космическая одиссея', 'Фантастика')
        collector.set_book_genre('2001 год', 'Фантастика')
        collector.set_book_genre('Стрелок', 'Ужасы')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сон', 'Детективы')

        assert collector.get_books_with_specific_genre(genre) == expected_result

    # тест на получение списка книг, подходящих детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Красная шапочка')
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Оно')
        collector.add_new_book('Волшебник изумрудного города')

        collector.set_book_genre('Красная шапочка', 'Сказка')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фэнтези')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Волшебник изумрудного города', 'Фэнтези')

        assert collector.get_books_for_children() == ['Красная шапочка', 'Волшебник изумрудного города']

    # тест на добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фэнтези')
        collector.set_book_genre('Оно', 'Ужасы')

        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и философский камень', 'Оно']

    # тест на удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фэнтези')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Оно')

        collector.delete_book_from_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и философский камень']

    # тест на получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и философский камень']
