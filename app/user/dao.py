from flask import jsonify
from flask_electron.dao.base import BaseDAO
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from .models import User

PASSWORD_MIN = 8


class UserDAO(BaseDAO):
    json = False

    def __init__(self, model=User):
        super().__init__(model)
        self.user = None
        self.model = model

    def save(self, instance):
        self.model = instance
        instance.password = self.encrypt_user_password(instance.password)
        super().save(instance)

    def validate(self, username, password):
        if len(username) < 3:
            return 'Username must be at least 3 characters in length', 406

        if self.get_one_by(self.model.username.name, username):
            return 'Username already exists in database.', 409

        if len(password) < PASSWORD_MIN:
            return 'Password must contain at least {} characters'.format(PASSWORD_MIN), 406

        return True

    def post(self, payload):
        """
        Handles the main POST logic for new user.
        :param payload: input key/values for API view.
        :return: API dict response
        :rtype: dict
        """

        try:
            self.validate_arguments(payload)
        except ValueError as error:
            return jsonify(
                message=str(error),
                schema=list(self.model.keys())
            ), 400

        username = payload.get('username')
        password = payload.get('password')

        # Run value based validation and catch any failure notes.
        status = self.validate(username, password)
        if status is not True:
            # Unpack validation status tuple and respond with message and code
            message, code = status
            return jsonify(message=message), code

        user = self.create(payload)
        self.encrypt_user_password(user)
        user.persist()

        user = self.get_one_by(self.model.username.name, username)
        return user

    def encrypt_user_password(self, password):
        """
        Take the existing user password and generate a sha hash of the password. Encrypt before storing in DB
        :return: None
        """

        return generate_password_hash(password)

    def check_user_password(self, user, password):
        """
        Takes a plain text password, then perform a decrypted password check.
        :param user: User instance
        :param password: Plain text password input
        :return: True or False whether password is valid
        :rtype: bool
        """

        if check_password_hash(user.password, password):
            return True
        return False
