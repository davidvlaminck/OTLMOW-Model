# coding=utf-8
from ...Classes.Abstracten.LinkObjectSV import LinkObjectSV


# Generated with OTLClassCreator. To modify: extend, do not edit
class VariabeleInstantie(LinkObjectSV):
    """TODO"""

    typeURI = 'http://lblod.data.gift/vocabularies/variables/VariableInstance'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='http://lblod.data.gift/vocabularies/variables/Variable', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='http://lblod.data.gift/vocabularies/variables/VariableWithLiteralValue', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='https://data.vlaanderen.be/ns/mobiliteit#VariabeleMetLocatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='https://data.vlaanderen.be/ns/mobiliteit#VariabeleMetVerwijzing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#heeftVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#VerkeersbordVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#heeftVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#VerkeerslichtVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#heeftVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#heeftVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#WegmarkeringVerkeersteken', direction='o')  # o = direction: outgoing
