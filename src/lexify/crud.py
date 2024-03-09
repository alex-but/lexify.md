from lexify import term_definition
from lexify.term_definition import TermDefinition


class TermDoesNotExistEx(Exception):
    pass


class TermAlreadyExistsEx(Exception):
    pass


def read(term: str, lexicon: list[TermDefinition]) -> str:
    try:
        term_definition = next(td for td in lexicon if td.term == term)
    except StopIteration:
        raise TermDoesNotExistEx("Term %s is not part of the glossary", term)
    return term_definition.definition


def create(
    term_definition: TermDefinition, lexicon: list[TermDefinition]
) -> list[TermDefinition]:
    term_exists = True
    try:
        read(term=term_definition.term, lexicon=lexicon)
    except TermDoesNotExistEx as e:
        term_exists = False
    finally:
        if term_exists:
            raise TermAlreadyExistsEx(
                "You cannot add %s. It's already defined. Try updating it",
                term_definition.term,
            )
    lexicon_with_new = lexicon + [term_definition]
    lexicon_with_new = sorted(lexicon_with_new, key=lambda x: x.term)
    return lexicon_with_new


def delete(term: str, lexicon: list[TermDefinition]) -> list[TermDefinition]:
    try:
        next(td for td in lexicon if td.term == term)
    except StopIteration:
        raise TermDoesNotExistEx("Term %s is not part of the glossary", term)
    return [td for td in lexicon if td.term != term]


def update(
    term_definition: TermDefinition, lexicon: list[TermDefinition]
) -> list[TermDefinition]:
    lexicon_without = delete(term=term_definition.term, lexicon=lexicon)
    lexicon_with_updated = create(
        term_definition=term_definition, lexicon=lexicon_without
    )
    return lexicon_with_updated
