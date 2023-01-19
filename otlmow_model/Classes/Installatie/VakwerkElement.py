# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ConstructiefObject import ConstructiefObject
from otlmow_model.Datatypes.KlTypeVakwerkElement import KlTypeVakwerkElement
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VakwerkElement(ConstructiefObject, VlakGeometrie):
    """Element dat deel uitmaakt van een constructie waarbij balken en staven, volgens een stelsel van rechthoeken en/of driehoeken, aan de uiteinden en/of kruiselings verbonden worden tot een onwrikbaar geheel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VakwerkElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        ConstructiefObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Windverband')

        self._typeVakwerkElement = OTLAttribuut(field=KlTypeVakwerkElement,
                                                naam='typeVakwerkElement',
                                                label='type vakwerk-element',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VakwerkElement.typeVakwerkElement',
                                                definition='Het type van vakwerk-element.',
                                                owner=self)

    @property
    def typeVakwerkElement(self) -> str:
        """Het type van vakwerk-element."""
        return self._typeVakwerkElement.get_waarde()

    @typeVakwerkElement.setter
    def typeVakwerkElement(self, value):
        self._typeVakwerkElement.set_waarde(value, owner=self)
