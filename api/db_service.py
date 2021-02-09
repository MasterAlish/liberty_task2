from datetime import date

from db.db import get_database
from db.manager import DbManager
from db.models import Program


class ProgramsDatabaseService:
    SORT_FIELDS_MAP = {
        "title": Program.title,
        "episode_title": Program.episode_title,
        "start_of_availability": Program.start_of_availability,
        "-title": Program.title.desc(),
        "-episode_title": Program.episode_title.desc(),
        "-start_of_availability": Program.start_of_availability.desc(),
    }

    def get_programs(self, sort_by: str = None, start_date_from: date = None, start_date_to: date = None, page: int = 1, per_page: int = 10):
        sort_field = self.SORT_FIELDS_MAP.get(sort_by, None)

        with DbManager(get_database()) as db:
            programs = Program.select().order_by(sort_field)
            if start_date_from:
                programs = programs.where(Program.start_of_availability >= start_date_from)
            if start_date_to:
                programs = programs.where(Program.start_of_availability <= start_date_to)

        return list(programs.paginate(page, per_page))
