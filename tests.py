import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_book_twise(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating_for_unexsists_book(self, collector):
        collector.set_book_rating('unexists book', 4)
        res = collector.get_book_rating('unexists book')

        assert not res

    def test_set_book_rating_set_rating_less_1(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        res = collector.get_book_rating('Гордость и предубеждение и зомби')

        assert res != 0


