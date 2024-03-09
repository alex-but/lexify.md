import pytest
from lexify.glossary_parser import parse_glossary, InvalidGlossaryFormatEx
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
            term="dependencies",
            definition="a local folder with the dependencies required by a specific software application.",
        ),
    ]
    with open("./asets/mock_glossary.md", "r") as mock_glossary_file:
        glossary_str = mock_glossary_file.read()
        glossary = parse_glossary(glossary=glossary_str)
        assert glossary == test_glossary
