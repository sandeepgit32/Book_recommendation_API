INSERT INTO book (name, publisher, rating, public_id) values("book1", "pub1", 4, "bid1")
INSERT INTO author (name, public_id) values("auth1", "aid1")
INSERT INTO book_author (book_id, author_id) values("bid1", "aid1")

select book.public_id, book.name, book.publisher, book.rating, author.public_id as author_name
from book 
join book_author
on book.public_id = book_author.book_id
join author
on book_author.author_id = author.public_id;

