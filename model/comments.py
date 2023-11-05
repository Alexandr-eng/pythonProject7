from model.user import User
class Comment:
    def __init__(self, comments: str, author: User):
        self.comments = comments
        self.author = author