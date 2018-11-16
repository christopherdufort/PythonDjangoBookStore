#  This Module contains all the Music class description

from .. import DataBaseLayer


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class Music:
    def __init__(self):
        pass

    # Example function
    def is_loanable(self):
            return "true"

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )
    def store(self):
        pass

    # to_string method
    def __str__(self):
        return "Music Details: "


