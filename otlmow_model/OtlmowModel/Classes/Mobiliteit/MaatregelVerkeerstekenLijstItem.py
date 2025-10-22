# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkObjectSV import LinkObjectSV
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class MaatregelVerkeerstekenLijstItem(LinkObjectSV):
    """TODO"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#MaatregelVerkeerstekenLijstItem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#MaatregelVerkeerstekenLijstItem.heeftVerkeerstekenLijstItem', target='https://data.vlaanderen.be/ns/mobiliteit#Mobiliteitsmaatregelconcept', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#heeftItem', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='u')  # u = unidirectional

        self._positie = OTLAttribuut(field=IntegerField,
                                     naam='positie',
                                     label='positie',
                                     objectUri='https://data.vlaanderen.be/ns/mobiliteit#MaatregelVerkeerstekenLijstItem.positie',
                                     definition='',
                                     owner=self)

    @property
    def positie(self) -> int:
        """"""
        return self._positie.get_waarde()

    @positie.setter
    def positie(self, value):
        self._positie.set_waarde(value, owner=self)
