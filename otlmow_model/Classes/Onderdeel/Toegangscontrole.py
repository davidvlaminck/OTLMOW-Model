# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlToegangscontroleSleuteltype import KlToegangscontroleSleuteltype
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangscontrole(AIMNaamObject, PuntGeometrie):
    """Component voor controle van de toegang tot een ruimte of behuizing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')

        self._heeftBadgelezer = OTLAttribuut(field=BooleanField,
                                             naam='heeftBadgelezer',
                                             label='heeft badgelezer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.heeftBadgelezer',
                                             definition='Geeft aan of de toegangscontrole uitgerust is met een badgelezer.',
                                             owner=self)

        self._heeftSlotMetAfstandsbediening = OTLAttribuut(field=BooleanField,
                                                           naam='heeftSlotMetAfstandsbediening',
                                                           label='heeft slot met afstandsbediening',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.heeftSlotMetAfstandsbediening',
                                                           definition='Geeft aan of het objecttype waaraan de toegangscontrole bevestigd is, kan geopend worden via een slot met afstandsbediening.',
                                                           owner=self)

        self._sleutelType = OTLAttribuut(field=KlToegangscontroleSleuteltype,
                                         naam='sleutelType',
                                         label='type sleutel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.sleutelType',
                                         definition='De soort sleutel die wordt gebruikt om de toegang te regelen.',
                                         owner=self)

    @property
    def heeftBadgelezer(self) -> bool:
        """Geeft aan of de toegangscontrole uitgerust is met een badgelezer."""
        return self._heeftBadgelezer.get_waarde()

    @heeftBadgelezer.setter
    def heeftBadgelezer(self, value):
        self._heeftBadgelezer.set_waarde(value, owner=self)

    @property
    def heeftSlotMetAfstandsbediening(self) -> bool:
        """Geeft aan of het objecttype waaraan de toegangscontrole bevestigd is, kan geopend worden via een slot met afstandsbediening."""
        return self._heeftSlotMetAfstandsbediening.get_waarde()

    @heeftSlotMetAfstandsbediening.setter
    def heeftSlotMetAfstandsbediening(self, value):
        self._heeftSlotMetAfstandsbediening.set_waarde(value, owner=self)

    @property
    def sleutelType(self) -> str:
        """De soort sleutel die wordt gebruikt om de toegang te regelen."""
        return self._sleutelType.get_waarde()

    @sleutelType.setter
    def sleutelType(self, value):
        self._sleutelType.set_waarde(value, owner=self)
