import re

from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


class NaamField(StringField):
    def __init__(self, naam: str, label: str, objectUri: str, definition: str, owner):
        super().__init__(naam, label, objectUri, definition, owner)

    @classmethod
    def validate(cls, value, attribuut) -> bool:
        if not StringField.validate(value, attribuut):
            return False
        if re.match(r'^[\w.\-]*$', value) is None:
            return False
        if hasattr(attribuut.owner, 'naampad') and attribuut.owner.naampad is not None:
            return attribuut.owner.naampad.split('/')[-1] == value
        return True

    @classmethod
    def create_dummy_data(cls) -> str:
        return 'dummy'
