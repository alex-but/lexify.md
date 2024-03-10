import pytest
from lexify import term_definition
from lexify.crud import (
    TermAlreadyExistsEx,
    TermDoesNotExistEx,
    create,
    delete,
    read,
    update,
)
from lexify.term_definition import TermDefinition


def test_create():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="C", definition="def_c"),
    ]
    new_term_definition = TermDefinition(term="b", definition="def_b")

    result_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="b", definition="def_b"),
        TermDefinition(term="C", definition="def_c"),
    ]

    assert result_glossary == create(
        term_definition=new_term_definition, lexicon=test_glossary
    )


def test_read():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="c", definition="def_c"),
    ]
    term = "a"
    definition = "def_a"

    assert definition == read(term=term, lexicon=test_glossary)


def test_update():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="c", definition="def_c"),
    ]
    new_term_definition = TermDefinition(term="a", definition="def_A")

    result_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_A"),
        TermDefinition(term="c", definition="def_c"),
    ]
    assert result_glossary == update(
        term_definition=new_term_definition, lexicon=test_glossary
    )


def test_delete():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="c", definition="def_c"),
    ]
    term = "a"

    result_glossary: list[TermDefinition] = [
        TermDefinition(term="c", definition="def_c"),
    ]
    assert result_glossary == delete(term=term, lexicon=test_glossary)


def test_invalid_create():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="c", definition="def_c"),
    ]
    existing_term_definition = TermDefinition(term="a", definition="def_A")
    with pytest.raises(TermAlreadyExistsEx):
        create(term_definition=existing_term_definition, lexicon=test_glossary)


def test_invalid_read():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="c", definition="def_c"),
    ]
    missing_term = "x"
    with pytest.raises(TermDoesNotExistEx):
        read(term=missing_term, lexicon=test_glossary)


def test_invalid_update():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="c", definition="def_c"),
    ]
    missing_term_definition = TermDefinition(term="b", definition="def_B")
    with pytest.raises(TermDoesNotExistEx):
        update(term_definition=missing_term_definition, lexicon=test_glossary)


def test_invalid_delete():
    test_glossary: list[TermDefinition] = [
        TermDefinition(term="a", definition="def_a"),
        TermDefinition(term="c", definition="def_c"),
    ]
    missing_term = "x"

    with pytest.raises(TermDoesNotExistEx):
        delete(term=missing_term, lexicon=test_glossary)
