# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlPutbekledingType import KlPutbekledingType
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Putbekleding(AIMObject, PuntGeometrie):
    """De soort afwerkingslaag waarmee een put bekleed is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte', direction='i')  # i = direction: incoming

        self._laagdikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='laagdikte',
                                       label='laagdikte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding.laagdikte',
                                       definition='De dikte van de bekledingslaag in millimeter.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlPutbekledingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding.type',
                                  definition='Bepaalt het type van de putbekleding.',
                                  owner=self)

    @property
    def laagdikte(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van de bekledingslaag in millimeter."""
        return self._laagdikte.get_waarde()

    @laagdikte.setter
    def laagdikte(self, value):
        self._laagdikte.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Bepaalt het type van de putbekleding."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
