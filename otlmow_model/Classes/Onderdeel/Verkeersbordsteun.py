# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Draagconstructie import Draagconstructie
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from otlmow_model.Datatypes.KlVerkeersbordsteunType import KlVerkeersbordsteunType
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordsteun(Draagconstructie, AIMNaamObject, PuntGeometrie):
    """Een draagconstructie voor verkeersborden. Dit kan een ronde paal of een vakwerksteun zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker')

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.breedte',
                                     usagenote='De breedte van een verkeersbordsteun wordt vooral gebruikt wanneer de verkeersbordsteun van het type vakwerksteun is.',
                                     definition='De breedte van een verkeersbordsteun in millimeter.',
                                     owner=self)

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.diameter',
                                      definition='De diameter van de verkeersbordpaal in millimeter.',
                                      owner=self)

        self._fabricagevoorschrift = OTLAttribuut(field=StringField,
                                                  naam='fabricagevoorschrift',
                                                  label='fabricagevoorschrift',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.fabricagevoorschrift',
                                                  definition='Genormaliseerde referentie waaraan het infrastructuur element aan voldoet.',
                                                  owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengte',
                                    definition='De lengte van de verkeersbordpaal in meter.',
                                    owner=self)

        self._lengteBovengronds = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='lengteBovengronds',
                                               label='lengte bovengronds',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengteBovengronds',
                                               definition='De bovengrondse lengte van de verkeersbordpaal in meter.',
                                               owner=self)

        self._lengteOndergronds = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='lengteOndergronds',
                                               label='lengte ondergronds',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengteOndergronds',
                                               definition='De ondergrondse lengte van de verkeersbordpaal in meter.',
                                               owner=self)

        self._operationeleStatus = OTLAttribuut(field=KlOperationeleStatus,
                                                naam='operationeleStatus',
                                                label='operationele status',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.operationeleStatus',
                                                usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                                deprecated_version='2.0.0',
                                                definition='De operationele status van de verkeersbordsteun.',
                                                owner=self)

        self._type = OTLAttribuut(field=KlVerkeersbordsteunType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.type',
                                  definition='Het type verkeersbordpaal.',
                                  owner=self)

        self._wanddikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='wanddikte',
                                       label='wanddikte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.wanddikte',
                                       definition='De dikte van de wand in millimeter.',
                                       owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van een verkeersbordsteun in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de verkeersbordpaal in millimeter."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def fabricagevoorschrift(self) -> str:
        """Genormaliseerde referentie waaraan het infrastructuur element aan voldoet."""
        return self._fabricagevoorschrift.get_waarde()

    @fabricagevoorschrift.setter
    def fabricagevoorschrift(self, value):
        self._fabricagevoorschrift.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de verkeersbordpaal in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def lengteBovengronds(self) -> KwantWrdInMeterWaarden:
        """De bovengrondse lengte van de verkeersbordpaal in meter."""
        return self._lengteBovengronds.get_waarde()

    @lengteBovengronds.setter
    def lengteBovengronds(self, value):
        self._lengteBovengronds.set_waarde(value, owner=self)

    @property
    def lengteOndergronds(self) -> KwantWrdInMeterWaarden:
        """De ondergrondse lengte van de verkeersbordpaal in meter."""
        return self._lengteOndergronds.get_waarde()

    @lengteOndergronds.setter
    def lengteOndergronds(self, value):
        self._lengteOndergronds.set_waarde(value, owner=self)

    @property
    def operationeleStatus(self) -> str:
        """De operationele status van de verkeersbordsteun."""
        return self._operationeleStatus.get_waarde()

    @operationeleStatus.setter
    def operationeleStatus(self, value):
        self._operationeleStatus.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type verkeersbordpaal."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def wanddikte(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van de wand in millimeter."""
        return self._wanddikte.get_waarde()

    @wanddikte.setter
    def wanddikte(self, value):
        self._wanddikte.set_waarde(value, owner=self)
