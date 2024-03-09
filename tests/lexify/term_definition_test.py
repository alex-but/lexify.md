from lexify.term_definition import (
    InvalidDefiniton,
    TermDefinition,
    validate_term_definition,
    InvalidTerm,
)
import pytest


def test_valid_term_defintion_validation():
    term = "avalidterm"
    definition = "a valid definition"
    term_definition = TermDefinition(term=term, definition=definition)
    assert validate_term_definition(term_definition=term_definition) == True


def test_invalid_term_validation():
    # term containing a space
    term = "invalid term"
    definition = "a valid definition"
    term_definition = TermDefinition(term=term, definition=definition)
    with pytest.raises(InvalidTerm):
        validate_term_definition(term_definition=term_definition)


def test_invalid_definition_len_validation():
    term = "avalidterm"
    # definition longer than 500chr
    definition = "a valid definition" * 100
    term_definition = TermDefinition(term=term, definition=definition)
    with pytest.raises(InvalidDefiniton):
        validate_term_definition(term_definition=term_definition)
