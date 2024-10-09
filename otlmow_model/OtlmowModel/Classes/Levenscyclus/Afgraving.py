# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlAfgravingSoorten import KlAfgravingSoorten
from ...Datatypes.KlGrondbestemming import KlGrondbestemming
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afgraving(AIMObject):
    """Wordt beschouwd als de verzameling van beheeractiviteiten die uitgevoerd kunnen worden op grond."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afgraving'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond', direction='i')  # i = direction: incoming

        self._bestemming = OTLAttribuut(field=KlGrondbestemming,
                                        naam='bestemming',
                                        label='bestemming',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afgraving.bestemming',
                                        definition='De bestemmingen of doelen van de grond.',
                                        owner=self)

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afgraving.gewicht',
                                     definition='Het gewicht van de grondlaag in ton.',
                                     owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afgraving.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de afgraving.',
                                         owner=self)

        self._soortAfgraving = OTLAttribuut(field=KlAfgravingSoorten,
                                            naam='soortAfgraving',
                                            label='soort afgraving',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afgraving.soortAfgraving',
                                            definition='De specificatie van type handeling bij afgraving.',
                                            owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afgraving.volume',
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
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte in vierkante meter van de afgraving."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortAfgraving(self) -> str:
        """De specificatie van type handeling bij afgraving."""
        return self._soortAfgraving.get_waarde()

    @soortAfgraving.setter
    def soortAfgraving(self, value):
        self._soortAfgraving.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van de grondlaag in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
