# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Verkeersbord import Verkeersbord
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.DteKleurRAL import DteKleurRAL, DteKleurRALWaarden
from otlmow_model.Datatypes.KlRetroreflecterendVerkeersbordAfwerkingsgraad import KlRetroreflecterendVerkeersbordAfwerkingsgraad
from otlmow_model.Datatypes.KlRetroreflecterendVerkeersbordGrootteorde import KlRetroreflecterendVerkeersbordGrootteorde
from otlmow_model.Datatypes.KlRetroreflecterendVerkeersbordMerk import KlRetroreflecterendVerkeersbordMerk
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroreflecterendVerkeersbord(Verkeersbord, AIMObject, PuntGeometrie):
    """Verkeersbord met op het beeldvlak een tekening en/of tekst die worden weergegeven met een geëigend bekledingsmateriaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BiFlashInstallatie')

        self._afwerkingsgraad = OTLAttribuut(field=KlRetroreflecterendVerkeersbordAfwerkingsgraad,
                                             naam='afwerkingsgraad',
                                             label='afwerkingsgraad',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.afwerkingsgraad',
                                             definition='De afwerkingsgraad van het retroreflecterend verkeersbord, volgens een keuzelijst op basis van SB250.',
                                             owner=self)

        self._grootteorde = OTLAttribuut(field=KlRetroreflecterendVerkeersbordGrootteorde,
                                         naam='grootteorde',
                                         label='grootteorde',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.grootteorde',
                                         kardinaliteit_min='0',
                                         definition='De classificatie naar grootteorde van het verkeersbord, zoals gedefinieerd in SB250 hoofdstuk 10.',
                                         owner=self)

        self._kleurAchterkant = OTLAttribuut(field=DteKleurRAL,
                                             naam='kleurAchterkant',
                                             label='kleur achterkant',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.kleurAchterkant',
                                             definition='De kleur van de achterkant van het retroreflecterend verkeersbord.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlRetroreflecterendVerkeersbordMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.merk',
                                  usagenote='Te selecteren uit een keuzelijst.',
                                  definition='De merknaam van het verkeersbord; duidt op de leverancier of producent van het verkeersbord.',
                                  owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.oppervlakte',
                                         kardinaliteit_min='0',
                                         definition='De oppervlakte van het beeldvlak van een verkeersbord.',
                                         owner=self)

    @property
    def afwerkingsgraad(self) -> str:
        """De afwerkingsgraad van het retroreflecterend verkeersbord, volgens een keuzelijst op basis van SB250."""
        return self._afwerkingsgraad.get_waarde()

    @afwerkingsgraad.setter
    def afwerkingsgraad(self, value):
        self._afwerkingsgraad.set_waarde(value, owner=self)

    @property
    def grootteorde(self) -> str:
        """De classificatie naar grootteorde van het verkeersbord, zoals gedefinieerd in SB250 hoofdstuk 10."""
        return self._grootteorde.get_waarde()

    @grootteorde.setter
    def grootteorde(self, value):
        self._grootteorde.set_waarde(value, owner=self)

    @property
    def kleurAchterkant(self) -> DteKleurRALWaarden:
        """De kleur van de achterkant van het retroreflecterend verkeersbord."""
        return self._kleurAchterkant.get_waarde()

    @kleurAchterkant.setter
    def kleurAchterkant(self, value):
        self._kleurAchterkant.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van het verkeersbord; duidt op de leverancier of producent van het verkeersbord."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van het beeldvlak van een verkeersbord."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
