import os
import pytest
from lexify.glossary_parser import (
    generate_glossary,
    parse_glossary,
    InvalidGlossaryFormatEx,
)
from lexify.term_definition import TermDefinition


def test_invalid_glossary_format():
    glossary_str = "ana are mere"
    with pytest.raises(InvalidGlossaryFormatEx):
        parse_glossary(glossary=glossary_str)


def test_valid_glossary_format():
    test_glossary: list[TermDefinition] = [
        TermDefinition(
            term="dependencies",
            definition="software packages that have to be installed in your computer to run a software.",
        ),
        TermDefinition(
            term="development environment",
            definition="a local folder with the dependencies required by a specific software application.",
        ),
    ]
    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(
        os.path.join(TEST_DIR, "assets/mock_glossary.md"), "r"
    ) as mock_glossary_file:
        glossary_str = mock_glossary_file.read()
        glossary = parse_glossary(glossary=glossary_str)
        assert glossary == test_glossary


def test_glossary_generator():
    term_definitions: list[TermDefinition] = [
        TermDefinition(
            term="dependencies",
            definition="software packages that have to be installed in your computer to run a software.",
        ),
        TermDefinition(
            term="development environment",
            definition="a local folder with the dependencies required by a specific software application.",
        ),
    ]
    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(
        os.path.join(TEST_DIR, "assets/mock_glossary.md"), "r"
    ) as mock_glossary_file:
        test_glossary_str = mock_glossary_file.read()
        glossary_str = generate_glossary(term_definitions=term_definitions)
        assert test_glossary_str == glossary_str
