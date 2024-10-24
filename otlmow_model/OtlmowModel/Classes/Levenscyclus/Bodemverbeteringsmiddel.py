# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlGrondverbeteringsmiddel import KlGrondverbeteringsmiddel
from ...Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bodemverbeteringsmiddel(AIMObject):
    """Het verwerken van bodemverbeteringsmiddelen omvat het gelijkmatig spreiden ervan op bepaalde grondoppervlakken en/of het verwerken in plantputten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bodemverbeteringsmiddel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond', direction='i')  # i = direction: incoming

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bodemverbeteringsmiddel.gewicht',
                                     definition='Het gewicht in kilogram van de verbeterde grond.',
                                     owner=self)

        self._grondverbeteringsmiddel = OTLAttribuut(field=KlGrondverbeteringsmiddel,
                                                     naam='grondverbeteringsmiddel',
                                                     label='grondverbeteringsmiddel',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bodemverbeteringsmiddel.grondverbeteringsmiddel',
                                                     definition='Het verwerken van bodemverbeteringsmiddelen omvat het gelijkmatig spreiden ervan op bepaalde grondoppervlakken en/of het verwerken in plantputten.',
                                                     owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bodemverbeteringsmiddel.oppervlakte',
                                         definition='De oppervlakte van de verbeterde grond in vierkante meter.',
                                         owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bodemverbeteringsmiddel.volume',
                                    definition='Het volume van de verbeterde grond in kubieke meter.',
                                    owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht in kilogram van de verbeterde grond."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def grondverbeteringsmiddel(self) -> str:
        """Het verwerken van bodemverbeteringsmiddelen omvat het gelijkmatig spreiden ervan op bepaalde grondoppervlakken en/of het verwerken in plantputten."""
        return self._grondverbeteringsmiddel.get_waarde()

    @grondverbeteringsmiddel.setter
    def grondverbeteringsmiddel(self, value):
        self._grondverbeteringsmiddel.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de verbeterde grond in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van de verbeterde grond in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
