from lexify.term_definition import (
    InvalidDefinitonEx,
    TermDefinition,
    validate_term_definition,
    InvalidTermEx,
)
import pytest


def test_valid_term_defintion_validation():
    term = "a valid term"
    definition = "a valid definition"
    term_definition = TermDefinition(term=term, definition=definition)
    assert validate_term_definition(term_definition=term_definition) == True


def test_invalid_term_validation():
    # term too long
    long_term = "invalid term" * 100
    definition = "a valid definition"
    term_definition = TermDefinition(term=long_term, definition=definition)
    with pytest.raises(InvalidTermEx):
        validate_term_definition(term_definition=term_definition)

    short_term = ""
    definition = "a valid definition"
    term_definition = TermDefinition(term=short_term, definition=definition)
    with pytest.raises(InvalidTermEx):
        validate_term_definition(term_definition=term_definition)


def test_invalid_definition_len_validation():
    term = "avalidterm"
    # definition longer than 500chr
    long_definition = "a valid definition" * 100
    term_definition = TermDefinition(term=term, definition=long_definition)
    with pytest.raises(InvalidDefinitonEx):
        validate_term_definition(term_definition=term_definition)

    short_definition = ""
    term_definition = TermDefinition(term=term, definition=short_definition)
    with pytest.raises(InvalidDefinitonEx):
        validate_term_definition(term_definition=term_definition)
