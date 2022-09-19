# qa_python
1. test_add_new_book_add_two_books - Тест возможности добавления книг в books_rating
2. test_add_new_book_add_book_twise - Тест на то что повторное добавление книги в books_rating невозможно
3. test_set_book_rating_set_rating_for_unexsists_book - Тест на отсутствие возможности установить рейтинг для книги которой нет в books_rating
4. test_set_book_rating_set_rating_less_than_1 - Проверка на отсутствие возможности утановить для книги рейтинг ниже чем 1
5. test_set_book_rating_set_rating_more_than_10 - Проверка на отсутствие возможности утановить для книги рейтинг выше чем 10
6. test_get_book_rating_unexists_book_have_not_rating - Проверка на то что запрос рейтинга книги которой нет в books_rating вернет None
7. test_add_book_in_favorites_add_and_check_for_existing - Добавление 2х книг в books_rating , добавление первой из них в favorites,чек на наличие первой в favorites и отсутствие в favorites второй
8. test_add_book_in_favorites_try_add_to_favirites_when_it_not_exists - Проверка на невозможность добавить в favorites книгу которой нет в books_rating
9. test_delete_book_from_favorites_add_to_favorite_check_delete_check_again - Проверка на возможноть удалить книгу
