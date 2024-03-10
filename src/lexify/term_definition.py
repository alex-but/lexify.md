from dataclasses import dataclass


class InvalidTermEx(Exception):
    pass


class InvalidDefinitonEx(Exception):
    pass


@dataclass
class TermDefinition:
    term: str
    definition: str

    @property
    def anchor(self):
        return self.term.replace(" ", "-").lower()


def validate_term_definition(term_definition: TermDefinition) -> bool:
    if " " in term_definition.term:
        raise InvalidTermEx("Your term %s includes spaces", term_definition.term)
    if len(term_definition.definition) > 500:
        raise InvalidDefinitonEx(
            "Your definition is too long. We recoomend less than 500 chr"
        )
    if len(term_definition.definition.strip()) < 1:
        raise InvalidDefinitonEx(
            "Your definition is too short. We need at least 3 characters"
        )
    return True
