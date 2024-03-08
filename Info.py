from database import *
class Info:
    leaders = None
    def print(self):
        db1 = DatabaseConnection()
        db1.connect()
        self.leaders = db1.getleaders()
        print(self.leaders)
        db.close()

a = Info()
a.print()