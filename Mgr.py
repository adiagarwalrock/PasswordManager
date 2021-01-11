import random
import pymysql
import config


class PasswordManager():

    def __init__(self, site, uname, email, pwd, rolling):
        self.site = site
        self.uname = uname
        self.email = email
        self.pwd = pwd
        self.rolling = rolling


class Encrypter(PasswordManager):

    def __init__(self, site, uname, email, pwd, rolling):
        super().__init__(site, uname, email, pwd, rolling)
   
    def encrypt(self, pwd, uname):
        print(site, uname, email, pwd, rolling)
        print("*****ENCRYPTION*****")
        encryptPWD = 'encryptPWD'
        encryptUNAME = 'encryptUNAME'
        return [encryptPWD, encryptUNAME]

    def decrypt(self, pwd, uname):
        print(site, uname, email, pwd, rolling)
        print("*****DECRYPTION*****")
        decryptPWD = 'decryptPWD'
        decryptUNAME = 'decryptUNAME'
        return [decryptPWD, decryptUNAME]


class DatabaseStorage(Encrypter, PasswordManager):

    def __init__(self, site, uname, email, rolling):
        super().__init__(site, uname, email, pwd, rolling)

        # self.host = config.DATABASE[0]
        # self.port = config.DATABASE[1]
        # self.user = config.DATABASE[2]
        # self.password = config.DATABASE[3]
        # self.db = config.DATABASE[4]

    def dataInsertion(self, site, uname, email, pwd, rolling):
        
        print(site, uname, email, pwd, rolling)
        print("*****DATA INSERTION*****")
        return

    def dataDeletion(self, site, uname, email, pwd, rolling):
        print(site, uname, email, pwd, rolling)
        print("*****DATA DELETION*****")
        return

    def dataRetreval(self, site, uname, email, pwd, rolling):
        print(site, uname, email, pwd, rolling)
        print("*****DATA DELETION*****")
        return


# Driver Code
site = input()
uname = input()
email = input()
pwd = input()
rolling = random.randint(0, 9)

pwdEncrypt = Encrypter(site, uname, email, pwd, rolling)
pwd = pwdEncrypt.encrypt(pwd, uname)
pwd = pwdEncrypt.decrypt(pwd, uname)

pwdDB = DatabaseStorage(site, uname, email, rolling)
pwdDB.dataInsertion(site, pwd[0], pwd[1], email, rolling)
pwdDB.dataDeletion(site, pwd[0], pwd[1], email, rolling)
