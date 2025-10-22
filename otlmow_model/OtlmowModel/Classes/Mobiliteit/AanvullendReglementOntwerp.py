# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkObjectSV import LinkObjectSV
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanvullendReglementOntwerp(LinkObjectSV):
    """TODO"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='http://todo.com/AanvullendReglement.isOntwerpVoor', target='https://data.vlaanderen.be/ns/besluit#AanvullendReglement', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#bevatMaatregelOntwerp', target='https://data.vlaanderen.be/ns/mobiliteit#MobliteitsmaatregelOntwerp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#bevatOntwerp', target='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp', direction='i')  # i = direction: incoming

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp.naam',
                                  definition='TODO',
                                  owner=self)

    @property
    def naam(self) -> str:
        """TODO"""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
