from lexify.term_definition import TermDefinition


class InvalidGlossaryFormatEx(Exception):
    pass


def parse_glossary(glossary: str) -> list[TermDefinition]:
    pass


def generate_glossary(term_definitions: TermDefinition) -> str:
    pass
