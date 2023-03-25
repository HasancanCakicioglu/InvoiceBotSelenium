import shelve

class SingletonDB:
    __instance = None

    @staticmethod
    def getInstance():
        if SingletonDB.__instance == None:
            SingletonDB.__instance = SingletonDB()
        return SingletonDB.__instance

    def __init__(self):
        self.__db = shelve.open("databaseDB.db",writeback=True)

    def openDB(self):
        self.__db = shelve.open("databaseDB.db", writeback=True)


    def get(self, key):
        if key in self.__db:
            return self.__db[key]
        else:
            return ""
    """
    def get(self, key):
        if not self.__db.close:
            if key in self.__db:
                return self.__db[key]
        return ""

    """
    def set(self, key, value):
        self.__db[key] = value

    def close(self):
        self.__db.close()

