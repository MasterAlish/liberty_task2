from peewee import SqliteDatabase


def get_database():
    return SqliteDatabase('local.db')
