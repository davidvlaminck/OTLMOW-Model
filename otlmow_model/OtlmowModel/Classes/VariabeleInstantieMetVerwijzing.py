# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes..VariabeleInstantie import VariabeleInstantie, VariabeleWaarden
from ...Datatypes.Variabele import Variabele


# Generated with OTLClassCreator. To modify: extend, do not edit
class VariabeleInstantieMetVerwijzing(VariabeleInstantie):
    """TODO"""

    typeURI = 'http://lblod.data.gift/vocabularies/variables/VariableInstanceWithResourceValue'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._waarde = OTLAttribuut(field=DtcVariabele,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='http://lblod.data.gift/vocabularies/variables/VariableInstanceWithResourceValue.waarde',
                                    definition='TODO',
                                    owner=self)

    @property
    def waarde(self) -> VariabeleWaarden:
        """TODO"""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self)
