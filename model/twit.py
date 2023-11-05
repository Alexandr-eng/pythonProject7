from model.user import User

class Twit:
    def __int__(self, body: str, author: User):
        self.body = body
        self.author = author