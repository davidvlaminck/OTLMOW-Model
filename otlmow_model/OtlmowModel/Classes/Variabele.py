# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkObjectSV import LinkObjectSV
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlVariabeleType import KlVariabeleType
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Variabele(LinkObjectSV):
    """TODO"""

    typeURI = 'http://lblod.data.gift/vocabularies/variables/Variable'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='http://lblod.data.gift/vocabularies/variables/VariableInstance', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.definieert', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='i')  # i = direction: incoming

        self._label = OTLAttribuut(field=StringField,
                                   naam='label',
                                   label='label',
                                   objectUri='http://lblod.data.gift/vocabularies/variables/Variable.label',
                                   definition='TODO',
                                   owner=self)

        self._type = OTLAttribuut(field=KlVariabeleType,
                                  naam='type',
                                  label='type',
                                  objectUri='http://lblod.data.gift/vocabularies/variables/Variable.type',
                                  definition='TODO',
                                  owner=self)

        self._vereist = OTLAttribuut(field=BooleanField,
                                     naam='vereist',
                                     label='vereist',
                                     objectUri='http://lblod.data.gift/vocabularies/variables/Variable.vereist',
                                     definition='TODO',
                                     owner=self)

    @property
    def label(self) -> str:
        """TODO"""
        return self._label.get_waarde()

    @label.setter
    def label(self, value):
        self._label.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """TODO"""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vereist(self) -> bool:
        """TODO"""
        return self._vereist.get_waarde()

    @vereist.setter
    def vereist(self, value):
        self._vereist.set_waarde(value, owner=self)
