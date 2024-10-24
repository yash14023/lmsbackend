from flask_mysqldb import MySQL
from flask import jsonify

class Book:
    
    def __init__(self, title, authors, average_rating, isbn, isbn13, language_code, 
                 num_pages, ratings_count, text_reviews_count, publication_date, 
                 publisher, publication_year, qty, status, is_available):
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date = publication_date
        self.publisher = publisher
        self.publication_year = publication_year
        self.qty = qty
        self.status = status
        self.is_available = is_available

    def get_all():
        from app import mysql
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Books')
        books = cur.fetchall()
        cur.close()
        return books

    def add_book(book_data):
        book_data = jsonify.load(book_data)
        from app import mysql 
        cur = mysql.connection.cursor()
        try:
            add_book_query = '''
            INSERT INTO Books (Title, Authors, AverageRating, Isbn, Isbn13, 
                             LanguageCode, NumPages, RatingsCount, TextReviewsCount, 
                             PublicationDate, Publisher, PublicationYear, Qty, 
                             Status, IsAvailable)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            book_values = (book_data.title, book_data.authors, book_data.average_rating,
                         book_data.isbn, book_data.isbn13, book_data.language_code,
                         book_data.num_pages, book_data.ratings_count,
                         book_data.text_reviews_count, book_data.publication_date,
                         book_data.publisher, book_data.publication_year,
                         book_data.qty, book_data.status, book_data.is_available)
            
            cur.execute(add_book_query, book_values)
            # mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error adding book: {e}")
            return False
        finally:
            cur.close()

    def update_book(book_id, book_data):
        from app import mysql
        cur = mysql.connection.cursor()
        try:
            update_book_query = '''
            UPDATE Books
            SET Title = %s, Authors = %s, AverageRating = %s, Isbn = %s, 
                Isbn13 = %s, LanguageCode = %s, NumPages = %s, RatingsCount = %s, 
                TextReviewsCount = %s, PublicationDate = %s, Publisher = %s, 
                PublicationYear = %s, Qty = %s, Status = %s, IsAvailable = %s
            WHERE bookId = %s
            '''
            book_values = (
                book_data.get('title'), book_data.get('authors'),
                book_data.get('average_rating'), book_data.get('isbn'),
                book_data.get('isbn13'), book_data.get('language_code'),
                book_data.get('num_pages'), book_data.get('ratings_count'),
                book_data.get('text_reviews_count'), book_data.get('publication_date'),
                book_data.get('publisher'), book_data.get('publication_year'),
                book_data.get('qty'), book_data.get('status'),
                book_data.get('isAvailable'), book_id
            )
            cur.execute(update_book_query, book_values)
            mysql.connection.commit()
            return {"message": "Book updated successfully!"}, 200
        except mysql.connection.Error as err:
            return {"error": str(err)}, 500
        finally:
            cur.close()
            
    def get_by_id(book_id):
        from app import mysql
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM Books WHERE bookId = %s', (book_id,))
            book = cur.fetchone()
            cur.close()
            if book is None:
                return None
            return book
        except mysql.connection.Error as err:
            return {"error": str(err)}, 500

    def get_total_books():
        from app import mysql
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM Books')
            total_books = cur.fetchone()
            cur.close()
            return total_books
        except mysql.connection.Error as err:
            return {"error": str(err)}, 500

    def delete(book_id):
        from app import mysql
        try:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM Books WHERE bookId = %s', (book_id,))
            mysql.connection.commit()
            affected_rows = cur.rowcount
            cur.close()
            return affected_rows > 0
        except mysql.connection.Error as err:
            return False, str(err)
