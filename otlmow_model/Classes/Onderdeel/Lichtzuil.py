# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.EMAfbakening import EMAfbakening
from otlmow_model.Datatypes.KlLichtzuilSoortLamp import KlLichtzuilSoortLamp
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtzuil(EMAfbakening, PuntGeometrie):
    """Inwendig verlichte, geel gekleurde conische steun, inclusief het voetstuk waarop het bevestigd is, die gebruikt wordt om obstakels op de weg te signaleren voor het aankomend verkeer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtzuil'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._soortLamp = OTLAttribuut(field=KlLichtzuilSoortLamp,
                                       naam='soortLamp',
                                       label='soort lamp',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtzuil.soortLamp',
                                       definition='Welke soort lamp er gebruikt wordt in de lichtzuil.',
                                       owner=self)

    @property
    def soortLamp(self) -> str:
        """Welke soort lamp er gebruikt wordt in de lichtzuil."""
        return self._soortLamp.get_waarde()

    @soortLamp.setter
    def soortLamp(self, value):
        self._soortLamp.set_waarde(value, owner=self)
