# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlBinnenverlichtingstoestelSchakelwijze import KlBinnenverlichtingstoestelSchakelwijze
from otlmow_model.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Binnenverlichtingstoestel(AIMObject, PuntGeometrie):
    """Een verlichtingstoestel dat binnen in een gebouw geplaatst wordt. Een verlichtingstoestel is de combinatie van de lamp en de armatuur."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller')

        self._schakelwijze = OTLAttribuut(field=KlBinnenverlichtingstoestelSchakelwijze,
                                          naam='schakelwijze',
                                          label='schakelwijze',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel.schakelwijze',
                                          definition='Geeft aan hoe het toestel aan- en uitgeschakeld wordt.',
                                          owner=self)

        self._soortLamp = OTLAttribuut(field=KlBinnenverlichtingstoestelSoortLamp,
                                       naam='soortLamp',
                                       label='soort lamp',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel.soortLamp',
                                       definition='Geeft aan welke soort lamp er gebruikt wordt in het binnenverlichtingstoestel.',
                                       owner=self)

    @property
    def schakelwijze(self) -> str:
        """Geeft aan hoe het toestel aan- en uitgeschakeld wordt."""
        return self._schakelwijze.get_waarde()

    @schakelwijze.setter
    def schakelwijze(self, value):
        self._schakelwijze.set_waarde(value, owner=self)

    @property
    def soortLamp(self) -> str:
        """Geeft aan welke soort lamp er gebruikt wordt in het binnenverlichtingstoestel."""
        return self._soortLamp.get_waarde()

    @soortLamp.setter
    def soortLamp(self, value):
        self._soortLamp.set_waarde(value, owner=self)
