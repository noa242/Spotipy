class User:
    def __init__(self, user_id, user_name, password, user_type):
        self.__id = user_id
        self.__user_name = user_name
        self.__password = password
        self.__type = user_type

    def id(self):
        return self.__id

    def user_name(self):
        return self.__user_name

    def password(self):
        return self.__password

    def user_type(self):
        return self.__type


