from user import User
from comment import Comment
from admin import Admin

db = []

comments = []

def create_user():
    runapp = True
    while runapp:
        create_account = str(input('Do you want to create an account?(y/n): '))
        if create_account == 'n':
            runapp = False
            continue

        username = str(input('enter username: '))
        password = str(input('enter password: ')) 

        user1 = User(username, password)
        db.append(user1)

        create_comment = str(input('Do you want to create a comment?(y/n): '))

        if create_comment == 'n':
            runapp = False
            continue

        comment = str(input('enter comment: '))

        comment1 = Comment(user1, comment)
        comments.append(comment1)
    
    if user1:
        return user1


def view_all_comments():
    view_all  = str(input('Do you want to view all comments?(y/n): '))
    if view_all == 'n':
        return
    for comment in comments:
        print(comment.get_message)


def view_all_users(user):
    view_all  = str(input('Do you want to view all users?(y/n): '))
    if view_all == 'n':
        return
    if isinstance(user, Admin):
        for user in db:
            print(user.get_username)


def view_user_comment():
    prompt = "Do you want to view all comments from user ?(y/n): "
    view_all  = str(input(prompt))
    if view_all == 'n':
        return

    username = input('Enter username: ')
    
    for comment in comments: 
        if comment.get_author.get_username == username:
            print(comment.get_message)
        else:
            print('sorry you cannot view this user comment')
            return

if __name__ == "__main__":
    user = create_user()
    view_all_comments()
    view_all_users(user)
    view_user_comment()




