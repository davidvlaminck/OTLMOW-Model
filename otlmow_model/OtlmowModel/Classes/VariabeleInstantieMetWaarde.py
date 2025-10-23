# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes..VariabeleInstantie import VariabeleInstantie
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VariabeleInstantieMetWaarde(VariabeleInstantie):
    """TODO"""

    typeURI = 'https://lblod.data.gift/vocabularies/variables/VariableInstanceWithLiteralValue'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://lblod.data.gift/vocabularies/variables/VariableInstanceWithLiteralValue.waarde',
                                    definition='TODO',
                                    owner=self)

    @property
    def waarde(self) -> str:
        """TODO"""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self)
