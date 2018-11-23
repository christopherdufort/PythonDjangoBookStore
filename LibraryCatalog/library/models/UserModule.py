#  This Module contains all the User class description
from datetime import datetime
from datetime import timedelta
import random
from .. import DataBaseLayer
import string


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class User:
    user_id: int = -1
    first_name: str
    last_name: str
    address: str
    phone: str
    is_admin: int
    password: str
    email: str
    session_expire: str
    session_key: str

    def __init__(self):
        pass

    def populateUser(self,user_id,first_name,last_name,address,phone,is_admin,password,email,session_expire,session_key):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.is_admin = is_admin
        self.password = password
        self.email = email
        self.session_expire = session_expire
        self.session_key = session_key

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module ) Active Record
    def store(self, is_admin):
        session_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        session_expire = (datetime.today()+timedelta(hours=1))
        sql = "INSERT INTO `soen341`.`user`(`first_name`, `last_name`, `email`, `address`, `phone_number`, `password`, `session_key`, `session_expire`, `is_admin`) VALUES('";
        sql += self.first_name + "', '"
        sql += self.last_name + "', '"
        sql += self.email + "', '"
        sql += self.address + "', '"
        sql += self.phone + "', '"
        sql += self.password + "', '"
        sql += str(session_key) + "', '"
        sql += str(session_expire) + "', '"
        sql += str(is_admin) + "');"
        print(sql)
        DataBaseLayer.insertCommand(sql)



    # to_string method
    def __str__(self):
        return "User Details: "


