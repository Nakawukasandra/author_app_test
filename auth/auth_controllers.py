from flask import Blueprint, request, jsonify
from app.models.users import User, db
from flask_bcrypt import Bcrypt
from email_validator import validate_email, EmailNotValidError

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
bcrypt = Bcrypt()

@auth.route('/register', methods=['POST'])
def register():
    try:
        # Your registration logic
        pass

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@auth.route('/users/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'contact': user.contact,
            'user_type': user.user_type,
            'biography': user.biography
        }
        output.append(user_data)
    return jsonify({'users': output})

@auth.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    user_data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'contact': user.contact,
        'user_type': user.user_type,
        'biography': user.biography
    }
    return jsonify(user_data)

@auth.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.get_json()
        # Update user fields
        # Your update logic
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete user', 'details': str(e)}), 500
