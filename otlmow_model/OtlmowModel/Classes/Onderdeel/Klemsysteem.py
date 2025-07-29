# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalAnker import KlMateriaalAnker
from ...Datatypes.KlMateriaalStalenKlemblok import KlMateriaalStalenKlemblok
from ...Datatypes.KlTypeAnker import KlTypeAnker
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Klemsysteem(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Stalen klemblokken en ankerstaven die de balg inklemmen tegen de vloer van het stuwhoofd en daarbij de positie fixeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klemsysteem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balgmechanisme', direction='o')  # o = direction: outgoing

        self._hoeveelheidAnkers = OTLAttribuut(field=NonNegIntegerField,
                                               naam='hoeveelheidAnkers',
                                               label='hoeveelheid ankers',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klemsysteem.hoeveelheidAnkers',
                                               definition='Geeft het aantal ankers aan.',
                                               owner=self)

        self._materiaalAnker = OTLAttribuut(field=KlMateriaalAnker,
                                            naam='materiaalAnker',
                                            label='materiaal anker',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klemsysteem.materiaalAnker',
                                            definition='Geeft de mogelijke opties van materialen van de anker aan.',
                                            owner=self)

        self._materiaalStalenKlemblok = OTLAttribuut(field=KlMateriaalStalenKlemblok,
                                                     naam='materiaalStalenKlemblok',
                                                     label='materiaal stalen blok',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klemsysteem.materiaalStalenKlemblok',
                                                     definition='Geeft de mogelijke opties van materiaal van het stalen blok aan.',
                                                     owner=self)

        self._typeAnker = OTLAttribuut(field=KlTypeAnker,
                                       naam='typeAnker',
                                       label='type anker',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klemsysteem.typeAnker',
                                       definition='Geeft de mogelijke opties van type anker aan.',
                                       owner=self)

    @property
    def hoeveelheidAnkers(self) -> int:
        """Geeft het aantal ankers aan."""
        return self._hoeveelheidAnkers.get_waarde()

    @hoeveelheidAnkers.setter
    def hoeveelheidAnkers(self, value):
        self._hoeveelheidAnkers.set_waarde(value, owner=self)

    @property
    def materiaalAnker(self) -> str:
        """Geeft de mogelijke opties van materialen van de anker aan."""
        return self._materiaalAnker.get_waarde()

    @materiaalAnker.setter
    def materiaalAnker(self, value):
        self._materiaalAnker.set_waarde(value, owner=self)

    @property
    def materiaalStalenKlemblok(self) -> str:
        """Geeft de mogelijke opties van materiaal van het stalen blok aan."""
        return self._materiaalStalenKlemblok.get_waarde()

    @materiaalStalenKlemblok.setter
    def materiaalStalenKlemblok(self, value):
        self._materiaalStalenKlemblok.set_waarde(value, owner=self)

    @property
    def typeAnker(self) -> str:
        """Geeft de mogelijke opties van type anker aan."""
        return self._typeAnker.get_waarde()

    @typeAnker.setter
    def typeAnker(self, value):
        self._typeAnker.set_waarde(value, owner=self)
