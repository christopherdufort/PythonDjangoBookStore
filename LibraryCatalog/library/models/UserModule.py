#  This Module contains all the User class description

from .. import DataBaseLayer


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class User:
    def __init__(self):
        pass

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )
    def store(self):
        pass

    # to_string method
    def __str__(self):
        return "User Details: "


