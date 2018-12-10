from user import User

class Moderator(User):
    
    def __init__(self, *args, **kwargs):
        super(Moderator, self).__init__(*args, **kwargs)
        self.isModerator = True

    def delete_comment(self, comment):
        """function to delete comment"""
        comment.set_message(None)
        return True

    