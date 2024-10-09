# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlBeheerHoutigeVegetatie import KlBeheerHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerHoutigeVegetatie(AIMObject):
    """Het beheerobject voor de houtige vegetatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie', direction='i')  # i = direction: incoming

        self._beheeroptie = OTLAttribuut(field=KlBeheerHoutigeVegetatie,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie.beheeroptie',
                                         kardinaliteit_max='*',
                                         definition='Aanduiding van welk beheer wordt toegepast op de houtige vegetatie.',
                                         owner=self)

        self._heeftBeheerplan = OTLAttribuut(field=BooleanField,
                                             naam='heeftBeheerplan',
                                             label='heeft beheerplan',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie.heeftBeheerplan',
                                             definition='Aanduiding of er een beheerplan bestaat.',
                                             owner=self)

    @property
    def beheeroptie(self) -> List[str]:
        """Aanduiding van welk beheer wordt toegepast op de houtige vegetatie."""
        return self._beheeroptie.get_waarde()

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def heeftBeheerplan(self) -> bool:
        """Aanduiding of er een beheerplan bestaat."""
        return self._heeftBeheerplan.get_waarde()

    @heeftBeheerplan.setter
    def heeftBeheerplan(self, value):
        self._heeftBeheerplan.set_waarde(value, owner=self)
