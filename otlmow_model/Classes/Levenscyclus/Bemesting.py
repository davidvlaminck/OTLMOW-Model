# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlBemesting import KlBemesting
from otlmow_model.Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bemesting(AIMObject):
    """Wordt beschouwd als de verzameling van beheeractiviteiten die uitgevoerd kunnen worden op grond."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bemesting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._bemesting = OTLAttribuut(field=KlBemesting,
                                       naam='bemesting',
                                       label='bemesting',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bemesting.bemesting',
                                       definition='Het toevoegen van en verwerken van meststoffen zowel bij aanleg alsook bij beheer.',
                                       owner=self)

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bemesting.gewicht',
                                     definition='Het gewicht in kilogram van de te bewerken grond.',
                                     owner=self)

    @property
    def bemesting(self) -> str:
        """Het toevoegen van en verwerken van meststoffen zowel bij aanleg alsook bij beheer."""
        return self._bemesting.get_waarde()

    @bemesting.setter
    def bemesting(self, value):
        self._bemesting.set_waarde(value, owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht in kilogram van de te bewerken grond."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)
