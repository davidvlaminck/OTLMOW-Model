import re

from otlmow_model.OtlmowModel.BaseClasses.NaamField import NaamField


class NaampadField(NaamField):
    def __init__(self, naam: str, label: str, objectUri: str, definition: str, owner):
        super().__init__(naam, label, objectUri, definition, owner)

    @classmethod
    def validate(cls, value, attribuut) -> bool:
        if re.match(r'^[\w.\-]+[/[\w.\-]+]*$', value) is None:
            return False
        if attribuut.owner.naam is not None:
            return value.split('/')[-1] == attribuut.owner.naam
        return True

    @classmethod
    def create_dummy_data(cls) -> str:
        return 'dummy/dummy'
