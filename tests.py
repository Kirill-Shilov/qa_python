

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

    def test_set_book_rating_set_rating_less_than_1(self, collector):
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.set_book_rating(book, 0)
        res = collector.get_book_rating(book)

        assert res != 0

    def test_set_book_rating_set_rating_more_than_10(self, collector):
        book = 'Гордость и предубеждение и зомби' 
        collector.add_new_book(book)
        collector.set_book_rating(book, 11)
        res = collector.get_book_rating(book)

        assert res != 11

    def test_get_book_rating_unexists_book_have_not_rating(self, collector):
        res = collector.get_book_rating('unexists book')

        assert not res

    def test_add_book_in_favorites_add_and_check_for_existing(self, collector):
        first_book = 'Гордость и предубеждение и зомби'
        second_book = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        collector.add_book_in_favorites(first_book)
        res = collector.get_list_of_favorites_books()

        assert first_book in res and second_book not in res

    def test_add_book_in_favorites_try_add_to_favirites_when_it_not_exists(self, collector):
        book = 'Гордость и предубеждение и зомби'
        collector.add_book_in_favorites(book)
        res = collector.get_list_of_favorites_books()

        assert book not in res

    def test_delete_book_from_favorites_add_to_favorite_check_delete_check_again(self, collector):
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        res_one = collector.get_list_of_favorites_books()
        assert book in res_one
        collector.delete_book_from_favorites(book)
        res_two = collector.get_list_of_favorites_books()

        assert book not in res_two

