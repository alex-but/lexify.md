from lexify.term_definition import TermDefinition
import re

from lexify.wording import DEFINITIONS, GLOSSARY, INDEX


class InvalidGlossaryFormatEx(Exception):
    pass


def parse_glossary(glossary: str) -> list[TermDefinition]:
    # Split in lines
    glossary_lines: list[str] = glossary.splitlines()
    # now extra whitespaces
    glossary_lines = [line for line in glossary_lines if line.strip()]

    title_idx = glossary_lines.index(f"# {GLOSSARY}")
    index_idx = glossary_lines.index(f"## {INDEX}")
    definitions_idx = glossary_lines.index(f"## {DEFINITIONS}")

    indexes = glossary_lines[index_idx + 1 : definitions_idx]
    definitions = glossary_lines[definitions_idx:]

    assert len(indexes) == len(definitions)
    term_definitoins = []
    for definition in definitions:
        parsed_term_condition = re.match(
            "<a name='(.*)'></a>**(.*)**: (.*)", definition
        )
        term_definitoins.append(
            term=parsed_term_condition.group(1),
            definition=parsed_term_condition.group(2),
        )
    return parsed_term_condition


def generate_glossary(term_definitions: TermDefinition) -> str:
    pass
