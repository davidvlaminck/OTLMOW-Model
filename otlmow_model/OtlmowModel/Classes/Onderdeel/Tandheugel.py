# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlVetType import KlVetType
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tandheugel(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een rechthoekige staaf, ook tandlat of heugel genoemd, die aan één kant is voorzien van vertanding, zoals een tandwiel. De tanden grijpen in op die van een bijbehorend tandwiel, waardoor een rotatie kan worden omgezet in een lineaire beweging of omgekeerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandheugel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aangrijpingsstoel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tandheugelmechanisme', direction='o')  # o = direction: outgoing

        self._lengteTandheugel = OTLAttribuut(field=KwantWrdInMillimeter,
                                              naam='lengteTandheugel',
                                              label='lengte heugel',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandheugel.lengteTandheugel',
                                              definition='De lengte van de tandheugel.',
                                              owner=self)

        self._typeVet = OTLAttribuut(field=KlVetType,
                                     naam='typeVet',
                                     label='type vet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandheugel.typeVet',
                                     definition='Geeft aan welk type vet gebruikt wordt om de tandheugel overbrenging te smeren.',
                                     owner=self)

    @property
    def lengteTandheugel(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de tandheugel."""
        return self._lengteTandheugel.get_waarde()

    @lengteTandheugel.setter
    def lengteTandheugel(self, value):
        self._lengteTandheugel.set_waarde(value, owner=self)

    @property
    def typeVet(self) -> str:
        """Geeft aan welk type vet gebruikt wordt om de tandheugel overbrenging te smeren."""
        return self._typeVet.get_waarde()

    @typeVet.setter
    def typeVet(self, value):
        self._typeVet.set_waarde(value, owner=self)
