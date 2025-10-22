# coding=utf-8
from ...Classes..Variabele import Variabele


# Generated with OTLClassCreator. To modify: extend, do not edit
class VariabeleMetLocatie(Variabele):
    """TODO"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#VariabeleMetLocatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='http://lblod.data.gift/vocabularies/variables/VariableInstance', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.definieert', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='i')  # i = direction: incoming
