# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ConstructiefObject import ConstructiefObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlTypeWand import KlTypeWand
from otlmow_model.Datatypes.KlZijdenType import KlZijdenType
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wand(ConstructiefObject, LijnGeometrie):
    """Een verticaal constructiedeel, vrijstaand of omsluitend die een afscheiding vormt, bv. tussen 2 ruimtes."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        ConstructiefObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanvaarbescherming')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler')

        self._isDragend = OTLAttribuut(field=BooleanField,
                                       naam='isDragend',
                                       label='is dragend',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand.isDragend',
                                       definition='Geeft aan of de wand dragend is, al dan niet.',
                                       owner=self)

        self._typeWand = OTLAttribuut(field=KlTypeWand,
                                      naam='typeWand',
                                      label='type wand',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand.typeWand',
                                      definition='De functie die de wand uitoefent.',
                                      owner=self)

        self._zijden = OTLAttribuut(field=KlZijdenType,
                                    naam='zijden',
                                    label='zijden',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand.zijden',
                                    definition='Het type van de zijden dat de wand heeft (recht, rond, schuin,...).',
                                    owner=self)

    @property
    def isDragend(self) -> bool:
        """Geeft aan of de wand dragend is, al dan niet."""
        return self._isDragend.get_waarde()

    @isDragend.setter
    def isDragend(self, value):
        self._isDragend.set_waarde(value, owner=self)

    @property
    def typeWand(self) -> str:
        """De functie die de wand uitoefent."""
        return self._typeWand.get_waarde()

    @typeWand.setter
    def typeWand(self, value):
        self._typeWand.set_waarde(value, owner=self)

    @property
    def zijden(self) -> str:
        """Het type van de zijden dat de wand heeft (recht, rond, schuin,...)."""
        return self._zijden.get_waarde()

    @zijden.setter
    def zijden(self, value):
        self._zijden.set_waarde(value, owner=self)
