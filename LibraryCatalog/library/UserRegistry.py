# All business logic associated with adding users, user login, registration, and display of user info etc should be handled here

from .models.UserModule import User
from . import DataBaseLayer
from datetime import datetime, timedelta
import datetime
import string
import random

class UserRegistry:
    active_user_list = []

    #use default values for all the fields excluding email and password
    def __init__(self):
        pass

    def sign_in(user_form):
        print("sign in!")
        return UserRegistry.authenticate(user_form.cleaned_data['email'], user_form.cleaned_data['password'])
        #sql = "SELECT * FROM user WHERE "
        #user = User(user_data.get('email'), user_data.get('password'))
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

    def authenticate(email=None, password=None):
        print("AUTH  CALLED")
        conn = DataBaseLayer.connectDb()
        sql_select = "SELECT * FROM User WHERE email = '" + email+ "' AND password = '" + password + "';"
        user = UserRegistry.ReformatUserTableObject(DataBaseLayer.selectCommand(conn, sql_select)[0])

        print("$$$$")
        print(user)
        DataBaseLayer.printTable(user)
        session_expire = (datetime.datetime.today()+timedelta(days=30))
        session_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        sql_insert = "UPDATE user SET session_expire = '"+str(session_expire)+"',session_key = '"+session_key+"'  WHERE id = '" + "1"+"';"
        DataBaseLayer.insertCommand(conn, sql_insert)
 
        print("User found")
        return user#wrong, user needs to be updated!

    #not finished
    def formatUserTableObject(bad_user_format):
        f_user = null;
        f_user['id'] = bad_user_format[0];
        f_user['first_name'] = bad_user_format[1];
        f_user['last_name'] = bad_user_format[2];
        f_user['address'] = bad_user_format[3];
        f_user['phone_number'] = bad_user_format[4];
        f_user['xxxx'] = bad_user_format[1];
        f_user['password'] = bad_user_format[6];
        f_user['email'] = bad_user_format[7];
        f_user['address'] = bad_user_format[1];


    ((1, 'Alessandro', 'Kreslin', '9406 Avenue Joseph Melançon', '5144360810', 0, 'admin', 'kalessandro14@gmail.com', datetime.date(2018, 12, 30), 'kalessandro14@gmail.com'),)


    def get_active_users():
        #session_key exists [DONE]
        #session_expire > today's date
        today = datetime.datetime.today()
        return User.objects.filter(session_expire__range=[today, "3020-01-31"]).exclude(session_key="")
