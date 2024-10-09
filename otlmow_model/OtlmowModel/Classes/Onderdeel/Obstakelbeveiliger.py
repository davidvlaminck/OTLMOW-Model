# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AfschermendeConstructie import AfschermendeConstructie
from ...Classes.Abstracten.SchokindexVoertuigkering import SchokindexVoertuigkering
from ...Datatypes.KlLEACObstakelbeveiligerType import KlLEACObstakelbeveiligerType
from ...Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Obstakelbeveiliger(AfschermendeConstructie, SchokindexVoertuigkering, VlakGeometrie):
    """Een energie-absorberende constructie voor voertuigen,geïnstalleerd vóór één of meerdere obstakels,met als doel de ernst van een botsing te reduceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau', direction='i', deprecated='2.0.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex', direction='i', deprecated='2.0.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie', direction='o')  # o = direction: outgoing

        self._performantieniveau = OTLAttribuut(field=KlLEACPerformantieniveau,
                                                naam='performantieniveau',
                                                label='performantieniveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.performantieniveau',
                                                definition='Het niveau waarop de obstakelbeveiliger is getest.',
                                                owner=self)

        self._type = OTLAttribuut(field=KlLEACObstakelbeveiligerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.type',
                                  definition='De functie die de obstakelbeveiliger vervult.',
                                  owner=self)

    @property
    def performantieniveau(self) -> str:
        """Het niveau waarop de obstakelbeveiliger is getest."""
        return self._performantieniveau.get_waarde()

    @performantieniveau.setter
    def performantieniveau(self, value):
        self._performantieniveau.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De functie die de obstakelbeveiliger vervult."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
