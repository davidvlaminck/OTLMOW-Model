# coding=utf-8
from datetime import date
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Brandvoorziening import Brandvoorziening
from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.Datatypes.KlBrandhaspelMerk import KlBrandhaspelMerk
from otlmow_model.Datatypes.KlBrandhaspelModelnaam import KlBrandhaspelModelnaam
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.Datatypes.KwantWrdInKubiekeMeterPerSeconde import KwantWrdInKubiekeMeterPerSeconde, KwantWrdInKubiekeMeterPerSecondeWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandhaspel(Brandvoorziening):
    """Een brandslang met spuitmond,opgerold op een haspel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost')

        self._buitendiameter = OTLAttribuut(field=KwantWrdInCentimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.buitendiameter',
                                            definition='Buitendiameter van de slang op de haspel.',
                                            owner=self)

        self._keuringsdatum = OTLAttribuut(field=DateField,
                                           naam='keuringsdatum',
                                           label='keuringsdatum',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.keuringsdatum',
                                           definition='Laatste datum waarop de haspel gekeurd is.',
                                           owner=self)

        self._maximaalDebiet = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                            naam='maximaalDebiet',
                                            label='maximaalDebiet',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.maximaalDebiet',
                                            usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                            deprecated_version='2.0.0',
                                            definition='Het maximale debiet dat door de slang en spuitmond kan stromen.',
                                            owner=self)

        self._maximaalVolumedebiet = OTLAttribuut(field=KwantWrdInKubiekeMeterPerSeconde,
                                                  naam='maximaalVolumedebiet',
                                                  label='maximaal volumedebiet',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.maximaalVolumedebiet',
                                                  definition='Het maximale debiet dat per tijdseenheid door de slang en spuitmond kan stromen.',
                                                  owner=self)

        self._merk = OTLAttribuut(field=KlBrandhaspelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.merk',
                                  definition='Het merk van de brandhaspel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBrandhaspelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.modelnaam',
                                       definition='De modelnaam van de brandhaspel.',
                                       owner=self)

        self._slangLengte = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='slangLengte',
                                         label='slanglengte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel.slangLengte',
                                         definition='Nuttige lengte van de brandslang op de haspel.',
                                         owner=self)

    @property
    def buitendiameter(self) -> KwantWrdInCentimeterWaarden:
        """Buitendiameter van de slang op de haspel."""
        return self._buitendiameter.get_waarde()

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def keuringsdatum(self) -> date:
        """Laatste datum waarop de haspel gekeurd is."""
        return self._keuringsdatum.get_waarde()

    @keuringsdatum.setter
    def keuringsdatum(self, value):
        self._keuringsdatum.set_waarde(value, owner=self)

    @property
    def maximaalDebiet(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het maximale debiet dat door de slang en spuitmond kan stromen."""
        return self._maximaalDebiet.get_waarde()

    @maximaalDebiet.setter
    def maximaalDebiet(self, value):
        self._maximaalDebiet.set_waarde(value, owner=self)

    @property
    def maximaalVolumedebiet(self) -> KwantWrdInKubiekeMeterPerSecondeWaarden:
        """Het maximale debiet dat per tijdseenheid door de slang en spuitmond kan stromen."""
        return self._maximaalVolumedebiet.get_waarde()

    @maximaalVolumedebiet.setter
    def maximaalVolumedebiet(self, value):
        self._maximaalVolumedebiet.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de brandhaspel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de brandhaspel."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def slangLengte(self) -> KwantWrdInMeterWaarden:
        """Nuttige lengte van de brandslang op de haspel."""
        return self._slangLengte.get_waarde()

    @slangLengte.setter
    def slangLengte(self, value):
        self._slangLengte.set_waarde(value, owner=self)
