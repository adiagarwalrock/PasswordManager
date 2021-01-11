import random


class Encrypter():

    def __init__(self):
        self.pwd = pwd

    def decrypt(self, pwd):
        print("DECRYPT")
        return pwd+"321"

    def encrypt(self, pwd):
        print("ENCRYPT")
        return pwd+"123"


class DatabaseStorage():

    def __init__(self, site, uname, pwd, email, rolling):
        self.site = site
        self.uname = uname
        self.pwd = pwd
        self.email = email
        self.rolling = rolling

    def dataInsertion(self):
        print(self.site, self.pwd, self.uname, self.email, self.rolling)
        print("DATA INSERTION")

    def dataDeletion(self):
        print(self.site, self.pwd, self.uname, self.email, self.rolling)
        print("DATA DELETION")


class PasswordManager(Encrypter):

    def __init__(self, site, uname, email, pwd, rolling):
        self.site = site
        self.uname = uname
        self.email = email
        self.pwd = pwd
        self.rolling = rolling

    def insertion(self):

        pwds = super()
        password = pwds.encrypt(pwd)
        
        objinit = DatabaseStorage(site, password, uname, email, rolling)
        objinit.dataInsertion()

    def deletion(self):

        pwds = super()
        password = pwds.decrypt(pwd)

        objinit = DatabaseStorage(site, password, uname, email, rolling)
        objinit.dataDeletion()


# Driver Code
# site = input()
# uname = input()
# email = input()
# pwd = input()

site = "site"
uname = "uname"
pwd = "pwd"
email = "email"
rolling = random.randint(0, 9)


obj = PasswordManager(site, uname, email, pwd, rolling)
obj.insertion()

objDel = PasswordManager(site, uname, email, pwd, rolling)
objDel.deletion()

