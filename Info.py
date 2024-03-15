from database import *
import Presenter


class Info:
    leaders = None

    def print_leaders(self):
        db1 = DatabaseConnection()
        db1.connect()
        self.leaders = db1.get_leaders()
        Presenter.present(self.leaders)
        db.close()


a = Info()
a.print_leaders()
