# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Put import Put
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlPutType import KlPutType
from ...Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class InspectieputRiolering(Put, AIMObject, VlakGeometrie):
    """Dient om de aanwezige riolering te kunnen inspecteren, reinigen of onderhouden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw', direction='i', deprecated='2.1.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht', direction='i')  # i = direction: incoming

        self._hoekverdraaiing = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                             naam='hoekverdraaiing',
                                             label='hoekverdraaiing',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering.hoekverdraaiing',
                                             definition='Verschil in richting tussen inkomende en uitgaande rioolbuis.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlPutType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering.type',
                                  definition='Het type van de put zoals beschreven in hoofdstuk 7 van het standaardbestek 250.',
                                  owner=self)

    @property
    def hoekverdraaiing(self) -> KwantWrdInDecimaleGradenWaarden:
        """Verschil in richting tussen inkomende en uitgaande rioolbuis."""
        return self._hoekverdraaiing.get_waarde()

    @hoekverdraaiing.setter
    def hoekverdraaiing(self, value):
        self._hoekverdraaiing.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van de put zoals beschreven in hoofdstuk 7 van het standaardbestek 250."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
