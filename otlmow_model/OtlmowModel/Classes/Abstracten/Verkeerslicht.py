# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlVerkeerslichtMasker import KlVerkeerslichtMasker
from ...Datatypes.KlVerkeerslichtMerk import KlVerkeerslichtMerk
from ...Datatypes.KlVerkeerslichtModelnaam import KlVerkeerslichtModelnaam
from ...Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeerslicht(AIMNaamObject, PuntGeometrie):
    """Abstracte voor verkeerslichten. Dit zijn apparaten, opgesteld naast of boven de weg, om weggebruikers visueel te geleiden over een kruispunt door het gebruik van rode, oranje-gele en groene lichten. De bepalingen van de wegcode zijn van toepassing, meer bepaald titel III, hoofdstuk I, artikelen 61 t.e.m. 64."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerafsluiting', direction='o')  # o = direction: outgoing

        self._masker = OTLAttribuut(field=KlVerkeerslichtMasker,
                                    naam='masker',
                                    label='masker',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.masker',
                                    definition='Type masker dat is aangebracht op het verkeerslicht.',
                                    owner=self)

        self._merk = OTLAttribuut(field=KlVerkeerslichtMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.merk',
                                  definition='Het merk van het verkeerslicht.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVerkeerslichtModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.modelnaam',
                                       definition='De modelnaam/product range van het verkeerslicht.',
                                       owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.vermogen',
                                      definition='Vermogen (Watt) van het verkeerslicht.',
                                      owner=self)

    @property
    def masker(self) -> str:
        """Type masker dat is aangebracht op het verkeerslicht."""
        return self._masker.get_waarde()

    @masker.setter
    def masker(self, value):
        self._masker.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het verkeerslicht."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van het verkeerslicht."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInWattWaarden:
        """Vermogen (Watt) van het verkeerslicht."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
