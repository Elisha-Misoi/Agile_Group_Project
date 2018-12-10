from moderator import Moderator

class Admin(Moderator):
    
    def __init__(self, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        self.Admin = True

    def edit_comment(self, comment, new_comment):
        """function to edit comment"""
        comment.set_message(new_comment)
        return True

    def delete_comment(self, comment):
        """function to delete comment"""
        comment.set_message(None)
        return True
        