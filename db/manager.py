from db.models import Program, Genre, OtherIdentifier, GroupId

DB_TABLES = [Program, Genre, OtherIdentifier, GroupId]


class DbManager:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.db.connect()
        self.db.create_tables(DB_TABLES)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()
