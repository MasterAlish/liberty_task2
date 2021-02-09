import peewee

from db.db import get_database
from db.manager import DbManager
from db.models import Program, Genre, OtherIdentifier, GroupId


class ProgramToSqlite:
    def __call__(self, program_data: dict):
        with DbManager(get_database()) as db:
            try:
                program = Program()
                program.init_with_data(program_data)
                program.save()
            except peewee.IntegrityError as e:
                print("Duplicate found: "+ repr(e))
                return

            for genre_data in program_data["genres"]:
                genre = Genre(program=program)
                genre.init_with_data(genre_data)
                genre.save()

            for other_identifier_data in program_data["other_identifiers"]:
                identifier = OtherIdentifier(program=program)
                identifier.init_with_data(other_identifier_data)
                identifier.save()

            for group_id_value in program_data["group_ids"]:
                group_id = GroupId(program=program)
                group_id.value = group_id_value
                group_id.save()


