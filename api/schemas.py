from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class GenreScheme(BaseModel):
    href: Optional[str]
    type: Optional[str]
    definition: Optional[str]

    class Config:
        orm_mode = True


class OtherIdentifierScheme(BaseModel):
    organization: Optional[str]
    type: Optional[str]
    authority: Optional[str]
    value: Optional[str]

    class Config:
        orm_mode = True


class GroupIdScheme(BaseModel):
    value: Optional[str]

    class Config:
        orm_mode = True


class ProgramScheme(BaseModel):
    crid: str
    instance_metadata_id: Optional[str]
    start_of_availability: Optional[date]
    end_of_availability: Optional[date]
    title: Optional[str]
    episode_title: Optional[str]
    genres: List[GenreScheme] = []
    other_identifiers: List[OtherIdentifierScheme] = []
    group_ids: List[str] = []

    class Config:
        orm_mode = True
