from flask import Blueprint,request,jsonify
from flask_cors import cross_origin
from ..controllers.book_controller import BookController


# def test():
#   print("hhey")

bp = Blueprint('books', __name__)
@cross_origin(origin="http://localhost:3000")

@bp.route('/', methods=['GET'])
def get_books():
    return BookController.get_all_books()

@bp.route('/add', methods=['POST'])
def add_book():
    try:
        book_data = request.get_json()
        if not book_data:
            return jsonify({"error": "No data provided"})
        success = BookController.add_book(book_data)
        if success:
            return jsonify({"message": "Book added successfully"})
        else:
            return jsonify({"error": "Failed to add book"})
            
    except Exception as e:
        return jsonify({"error": str(e)})




@bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return BookController.get_book_by_id(book_id)

@bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    try: 
        book_data = request.get_json()
        if not book_data:
            return jsonify({"error" : "No Data Provided"})
        return BookController.update_book(book_id)
    except Exception as e:
        return jsonify({"error": str(e)})

@bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return BookController.delete_book(book_id)