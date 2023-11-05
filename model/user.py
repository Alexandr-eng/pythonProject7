class User:
    def __init__(self, username: str):
        self.username = username


    # def __repr__(self):
    #     db.sessions.add(self)
    #     db.sessions.commit()
    #
    #
    # def __delete__(self):
    #     db.sessions.delite(self)
    #     db.sessions.commit()