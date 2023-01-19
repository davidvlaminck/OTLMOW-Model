# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlGrondherkomst import KlGrondherkomst
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afdekking(AIMObject):
    """Wordt beschouwd als de verzameling van beheeractiviteiten die uitgevoerd kunnen worden op grond."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afdekking'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._herkomst = OTLAttribuut(field=KlGrondherkomst,
                                      naam='herkomst',
                                      label='herkomst',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afdekking.herkomst',
                                      definition='De herkomst van de grond.',
                                      owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afdekking.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de afdekking.',
                                         owner=self)

    @property
    def herkomst(self) -> str:
        """De herkomst van de grond."""
        return self._herkomst.get_waarde()

    @herkomst.setter
    def herkomst(self, value):
        self._herkomst.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte in vierkante meter van de afdekking."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
