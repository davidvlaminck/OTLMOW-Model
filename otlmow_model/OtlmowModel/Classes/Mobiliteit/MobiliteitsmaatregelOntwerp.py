# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkObjectSV import LinkObjectSV
from ...Datatypes.KlCode import KlCode


# Generated with OTLClassCreator. To modify: extend, do not edit
class MobiliteitsmaatregelOntwerp(LinkObjectSV):
    """TODO"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#MobliteitsmaatregelOntwerp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='http://www.w3.org/ns/prov#wasDerivedFrom', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel.verwijdertMaatregel', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#wordtAangeduidDoor', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#bevatMaatregelOntwerp', target='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#ontwerpVanMaatregel', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregel', direction='u')  # u = unidirectional

        self._status = OTLAttribuut(field=KlCode,
                                    naam='status',
                                    label='naam',
                                    objectUri='https://data.vlaanderen.be/ns/mobiliteit#MobliteitsmaatregelOntwerp.status',
                                    definition='TODO',
                                    owner=self)

    @property
    def status(self) -> str:
        """TODO"""
        return self._status.get_waarde()

    @status.setter
    def status(self, value):
        self._status.set_waarde(value, owner=self)
