from datetime import date
from typing import List

from fastapi import FastAPI

from api import schemas
from api.db_service import ProgramsDatabaseService

app = FastAPI()


@app.get("/programs", response_model=List[schemas.ProgramScheme])
def get_all_programs(
        sort_by: str = None,
        start_date_from: date = None,
        start_date_to: date = None,
        page: int = 1,
        per_page: int = 10):
    service = ProgramsDatabaseService()
    return service.get_programs(sort_by, start_date_from, start_date_to, page, per_page)
