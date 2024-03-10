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
    if len(term_definition.term.strip()) > 100:
        raise InvalidTermEx("Your term is too long. We recoomend less than 100 chr")
    if len(term_definition.term.strip()) < 1:
        raise InvalidTermEx(
            "Your definition is too short. We need at least 1 character"
        )

    if len(term_definition.definition) > 500:
        raise InvalidDefinitonEx(
            "Your definition is too long. We recoomend less than 500 chr"
        )
    if len(term_definition.definition.strip()) < 1:
        raise InvalidDefinitonEx(
            "Your definition is too short. We need at least 1 character"
        )
    return True
