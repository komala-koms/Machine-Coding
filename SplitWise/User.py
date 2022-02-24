class User:
    __id = None
    __name = None
    __mobile = None
    __email = None

    def __init__(self, __id, __name, __mobile, __email):
        self.__id = __id
        self.__name = __name
        self.__mobile = __mobile
        self.__email = __email

    def setId(self,__id):
        self.__id = __id

    def setName(self,__name):
        self.__name == __name

    def setMobile(self,__mobile):
        self.__mobile = __mobile

    def setEmail(self,__email):
        self.__email = __email

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getMobile(self,__mobile):
        return self.__mobile

    def getEmail(self):
        return self.__email