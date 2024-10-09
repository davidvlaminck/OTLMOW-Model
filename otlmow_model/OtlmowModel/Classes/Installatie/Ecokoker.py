# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlEcoEcokokerType import KlEcoEcokokerType
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecokoker(AIMObject, LijnGeometrie):
    """Een kleine ecotunnel of ecokoker is een doorgang voor dieren onder een weg of spoorweg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geleiding', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis', direction='i')  # i = direction: incoming

        self._type = OTLAttribuut(field=KlEcoEcokokerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker.type',
                                  definition='Het type van ecokoker zoals bv. amfibieënkoker, ….',
                                  owner=self)

    @property
    def type(self) -> str:
        """Het type van ecokoker zoals bv. amfibieënkoker, …."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
