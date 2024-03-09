from dataclasses import dataclass


class InvalidTerm(Exception):
    pass


class InvalidDefiniton(Exception):
    pass


@dataclass
class TermDefinition:
    term: str
    definition: str

    @property
    def anchor(self):
        return self.term.replace(" ", "-")


def validate_term_definition(term_definition: TermDefinition) -> bool:
    if " " in term_definition.term:
        raise InvalidTerm("Your term %s includes spaces", term_definition.term)
    if len(term_definition.definition) > 500:
        raise InvalidDefiniton(
            "Your definition is too long. We recoomend less than 500 chr"
        )
    return True
