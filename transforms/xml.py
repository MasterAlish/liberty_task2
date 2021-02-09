import xml.etree.ElementTree as ET
from datetime import datetime


XML_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class ProgramXmlParser:
    def __init__(self):
        pass

    def __call__(self, xml_data) -> dict:
        program = {}
        root = ET.fromstring(xml_data)

        program_tag = root.find("ProgramDescription/ProgramLocationTable/OnDemandProgram/Program")
        if program_tag is not None:
            program["crid"] = program_tag.attrib["crid"]

        instance_metadata_id_tag = root.find("ProgramDescription/ProgramLocationTable/OnDemandProgram/InstanceMetadataId")
        if instance_metadata_id_tag is not None:
            program["instance_metadata_id"] = instance_metadata_id_tag.text

        date_tag = root.find("ProgramDescription/ProgramLocationTable/OnDemandProgram/StartOfAvailability")
        if date_tag is not None:
            program["start_of_availability"] = self.parse_xml_date(date_tag.text)

        date_tag = root.find("ProgramDescription/ProgramLocationTable/OnDemandProgram/EndOfAvailability")
        if date_tag is not None:
            program["end_of_availability"] = self.parse_xml_date(date_tag.text)

        title_tags = root.findall("ProgramDescription/ProgramInformationTable/ProgramInformation/BasicDescription/Title")
        for title_tag in title_tags:
            if title_tag.attrib.get("type") is None:
                program["title"] = title_tag.text
            elif title_tag.attrib.get("type") == "episodeTitle":
                program["episode_title"] = title_tag.text

        program["genres"] = self.read_genres(root)
        program["other_identifiers"] = self.read_other_identifiers(root)
        program["group_ids"] = self.read_group_ids(root)

        return program

    def read_genres(self, root):
        genres = []
        genre_tags = root.findall("ProgramDescription/ProgramInformationTable/ProgramInformation/BasicDescription/Genre")
        for genre_tag in genre_tags:
            genre = {
                "type": genre_tag.attrib["type"],
                "href": genre_tag.attrib["href"]
            }
            definition_tag = genre_tag.find("Definition")
            if definition_tag is not None:
                genre["definition"] = definition_tag.text
            genres.append(genre)
        return genres

    def read_group_ids(self, root):
        group_ids = []
        group_tags = root.findall("ProgramDescription/GroupInformationTable/GroupInformation")
        for group_tag in group_tags:
            group_ids.append(group_tag.attrib["groupId"])
        return group_ids

    def read_other_identifiers(self, root):
        identifiers = []
        other_identifier_tags = root.findall("ProgramDescription/ProgramInformationTable/ProgramInformation/OtherIdentifier")
        for other_identifier_tag in other_identifier_tags:
            identifiers.append({
                "type": other_identifier_tag.attrib["type"],
                "authority": other_identifier_tag.attrib["authority"],
                "organization": other_identifier_tag.attrib["organization"],
                "value": other_identifier_tag.text
            })
        return identifiers

    def parse_xml_date(self, text):
        return datetime.strptime(text, XML_DATE_FORMAT)
