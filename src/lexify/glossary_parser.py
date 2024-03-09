from lexify.term_definition import TermDefinition

from lexify.wording import DEFINITIONS, GLOSSARY, INDEX


class InvalidGlossaryFormatEx(Exception):
    pass


def parse_glossary(glossary: str) -> list[TermDefinition]:
    # Split in lines
    glossary_lines: list[str] = glossary.splitlines()
    # now extra whitespaces
    glossary_lines = [line for line in glossary_lines if line.strip()]

    try:
        title_idx = glossary_lines.index(f"# {GLOSSARY}")
    except Exception as e:
        raise InvalidGlossaryFormatEx(
            "The format of the exisiting glossary is incorrect. The '# Glossary' title is missing"
        )
    try:
        index_idx = glossary_lines.index(f"## {INDEX}")
        definitions_idx = glossary_lines.index(f"## {DEFINITIONS}")
    except Exception as e:
        raise InvalidGlossaryFormatEx(
            "The format of the exisiting glossary is incorrect. The '# Index' or `# Definitions` are missing"
        )
    indexes = glossary_lines[index_idx + 1 : definitions_idx]
    definitions = glossary_lines[definitions_idx + 1 :]

    try:
        assert title_idx < index_idx
        assert index_idx < definitions_idx
        no_indexes = len(indexes)
        no_defs = len(definitions) / 2
        assert no_indexes == no_defs

    except Exception as e:
        raise InvalidGlossaryFormatEx(
            "The format of the exisiting glossary is incorrect. Order of titles missmatch or not matching indexes and definitions"
        )
    term_definitions = []
    # agregate definition pairs
    for term, definition in zip(definitions[0::2], definitions[1::2]):
        term = term.replace("####", "").strip()
        term_definition = TermDefinition(
            term=term,
            definition=definition,
        )
        term_definitions.append(term_definition)
    return term_definitions


def generate_glossary(term_definitions: list[TermDefinition]) -> str:
    glossary_lines = []
    glossary_lines.append(f"# {GLOSSARY}\n\n")
    glossary_lines.append(f"## {INDEX}\n\n")
    for term_definition in term_definitions:
        glossary_lines.append(
            f"[{term_definition.term}](#{term_definition.anchor})\n\n"
        )
    glossary_lines.append(f"## {DEFINITIONS}\n\n")
    for term_definition in term_definitions:
        glossary_lines.append(
            f"#### {term_definition.term}\n{term_definition.definition}\n"
        )
    return "".join(glossary_lines)
