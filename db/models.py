from peewee import *

from db.db import get_database


class Program(Model):
    crid = CharField(unique=True)
    instance_metadata_id = CharField(null=True)
    start_of_availability = DateField(null=True)
    end_of_availability = DateField(null=True)
    title = CharField(null=True)
    episode_title = CharField(null=True)

    def init_with_data(self, data):
        self.crid = data["crid"]
        self.instance_metadata_id = data["instance_metadata_id"]
        self.start_of_availability = data["start_of_availability"]
        self.end_of_availability = data["end_of_availability"]
        self.title = data["title"]
        self.episode_title = data["episode_title"]

    @property
    def genres(self):
        return list(self.genres_set)

    @property
    def other_identifiers(self):
        return list(self.other_identifiers_set)

    @property
    def group_ids(self):
        groups = self.group_ids_set.select(GroupId.value)
        return list(map(lambda s: s.value, groups))

    class Meta:
        database = get_database()


class Genre(Model):
    program = ForeignKeyField(Program, backref="genres_set")
    href = CharField()
    type = CharField(null=True)
    definition = CharField(null=True)

    def init_with_data(self, data):
        self.href = data["href"]
        self.type = data["type"]
        self.definition = data.get("definition", None)

    class Meta:
        database = get_database()


class OtherIdentifier(Model):
    program = ForeignKeyField(Program, backref="other_identifiers_set")
    organization = CharField(null=True)
    type = CharField(null=True)
    authority = CharField(null=True)
    value = CharField()

    def init_with_data(self, data):
        self.organization = data["organization"]
        self.type = data["type"]
        self.authority = data["authority"]
        self.value = data["value"]

    class Meta:
        database = get_database()


class GroupId(Model):
    program = ForeignKeyField(Program, backref="group_ids_set")
    value = CharField()

    class Meta:
        database = get_database()
