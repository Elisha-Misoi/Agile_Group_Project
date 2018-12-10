
from datetime import datetime
# from comment import Comment

class BadRequestError(Exception):
    pass

class User(object):

    def __init_(self, username, password):
        self.username = username
        self.password = password
        self.loggedInAt = None
        self.isLoggedIn = False
        self.comment = None
        self.isAdmin = False
        self.isModerator = False

    def log_in(self, username, password):
        """
        Takes a username and password.
        Sets the isLoggedIn variable to True.
        Sets the current logged in time
        """

        if username == self.username and password == self.password:
            self.isLoggedIn = True
            self.loggedInAt = datetime.utcnow()
        return False

    def log_out(self):
        if self.isLoggedIn:
            self.isLoggedIn = False
            return True
        return False

    def edit_comment(self, comment, message):
        
        if comment.get_author.get_username == self.username:
            comment.set_message(message)
            return True
        return False

     def create_comment(self, comment, message):
        """
        creates a new comment.
        comment - Comment Object
        message = string
        Returns a comment object
        """
        return comment(self, message)

    def get_last_logged_in(self):
        return self.loggedInAt

    @property
    def get_username(self):
        return self.username

    def delete_comment(self, comment):

        raise BadRequestError




