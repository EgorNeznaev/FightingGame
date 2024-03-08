import sqlite3

class DatabaseConnection:
    _instance = None


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_name='my_database.db'):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Connected to database: {self.db_name}")
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            print(f"Disconnected from database: {self.db_name}")
            self.connection = None

    def getleaders(self):
        if not self.connection:
            print("No active database connection.")
            return
        cursor = self.connection.cursor()
        query = "SELECT nickname, wins FROM leaderboard"
        cursor.execute(query)
        leaders = cursor.fetchall()
        cursor.close()
        return leaders


db = DatabaseConnection()
db.connect()
db.close()