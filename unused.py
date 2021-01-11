def __connect__(self):
        self.con = pymysql.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            db=self.db,
            cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def __commit__(self):
        self.con.commit()

    def executeWrite(self, sql):
        try:
            self.__connect__()
            self.cur.execute(sql)
            self.__commit__()
            return True

        except pymysql.MySQLError as e:
            print("Mysql Error:", e)
            return False

        finally:
            self.__disconnect__()

    def fetchRead(self, sql):
        try:
            self.__connect__()
            self.cur.execute(sql)
            result = self.cur.fetchall()
            self.__disconnect__()
            return result

        except pymysql.MySQLError as e:
            print("Mysql Error:", e)
            
        finally:
            self.__disconnect__()
