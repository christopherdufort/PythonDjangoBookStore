# All business logic associated with adding users, user login, registration, and display of user info etc should be handled here

from .models.UserModule import User


class UserRegistry:
    active_user_list = []

    #use default values for all the fields excluding email and password
    def __init__(self):
        pass

    def sign_in(self, user_data):
        user = User(user_data.get('email'), user_data.get('password'))
        #use bcrypt to check if this password matches the hashed password in the db

#     def authenticate(request, email=None, password=None):
#         print("AUTH  CALLED")
#         try:
#             user = User.objects.get(email=email, password=password)
#         except User.DoesNotExist:
#             return "user not found"
#         except User.MultipleObjectsReturned:
#             return "multiple users with this email exist"
#         print("User found")
#         return user