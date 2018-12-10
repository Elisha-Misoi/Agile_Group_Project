import datetime


class Comment(object):
    def __init__(self, author, message, replied_to=None):
        self.author = author
        self.message = message
        self.replied_to = replied_to
        self.created_at = datetime.datetime.utcnow()

    @property
    def get_author(self):
        '''method to set author'''
        return self.author

    def set_author(self, value):
        '''method to set author'''
        self.author = value

    @property
    def get_message(self):
        '''method to get mesage'''
        return self.message

    def set_message(self, value):
        '''method to set a message'''
        self.message = value

    @property
    def get_reply_to(self):
        '''method to get replied to'''
        return self.replied_to

    def set_reply_to(self, value):
        '''method to set replied to'''
        self.replied_to = value

    @property
    def get_create_at(self):
        '''method to return creation time'''
        return self.created_at

