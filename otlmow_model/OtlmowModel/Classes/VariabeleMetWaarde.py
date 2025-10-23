# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes..Variabele import Variabele
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VariabeleMetWaarde(Variabele):
    """TODO"""

    typeURI = 'http://lblod.data.gift/vocabularies/variables/VariableWithLiteralValue'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='http://lblod.data.gift/vocabularies/variables/VariableInstance', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.definieert', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='i')  # i = direction: incoming

        self._standaardwaarde = OTLAttribuut(field=StringField,
                                             naam='standaardwaarde',
                                             label='standaard waarde',
                                             objectUri='http://lblod.data.gift/vocabularies/variables/VariableWithLiteralValue.standaardwaarde',
                                             definition='Dit is een letterlijke waarde (bijvoorbeeld een tekst, getal of datum) die als uitgangspunt of suggestie dient bij het invullen van de variabele.',
                                             owner=self)

    @property
    def standaardwaarde(self) -> str:
        """Dit is een letterlijke waarde (bijvoorbeeld een tekst, getal of datum) die als uitgangspunt of suggestie dient bij het invullen van de variabele."""
        return self._standaardwaarde.get_waarde()

    @standaardwaarde.setter
    def standaardwaarde(self, value):
        self._standaardwaarde.set_waarde(value, owner=self)
