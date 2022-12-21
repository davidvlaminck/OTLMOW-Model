# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlGrondbestemming import KlGrondbestemming
from otlmow_model.Datatypes.KlUitgravingSoorten import KlUitgravingSoorten
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Uitgraving(AIMObject):
    """Wordt beschouwd als de verzameling van beheeractiviteiten die uitgevoerd kunnen worden op grond."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Uitgraving'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._bestemming = OTLAttribuut(field=KlGrondbestemming,
                                        naam='bestemming',
                                        label='bestemming',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Uitgraving.bestemming',
                                        definition='De bestemmingen of doelen van de grond.',
                                        owner=self)

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Uitgraving.gewicht',
                                     definition='Het gewicht van de grondlaag in ton.',
                                     owner=self)

        self._soortUitgraving = OTLAttribuut(field=KlUitgravingSoorten,
                                             naam='soortUitgraving',
                                             label='soort uitgraving',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Uitgraving.soortUitgraving',
                                             definition='De specificatie van type grond bij uitgraving.',
                                             owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Uitgraving.volume',
                                    definition='Het volume van de grondlaag in kubieke meter.',
                                    owner=self)

    @property
    def bestemming(self) -> str:
        """De bestemmingen of doelen van de grond."""
        return self._bestemming.get_waarde()

    @bestemming.setter
    def bestemming(self, value):
        self._bestemming.set_waarde(value, owner=self)

    @property
    def gewicht(self) -> KwantWrdInTonWaarden:
        """Het gewicht van de grondlaag in ton."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def soortUitgraving(self) -> str:
        """De specificatie van type grond bij uitgraving."""
        return self._soortUitgraving.get_waarde()

    @soortUitgraving.setter
    def soortUitgraving(self, value):
        self._soortUitgraving.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van de grondlaag in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
