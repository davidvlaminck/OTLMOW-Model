# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from ...Datatypes.DtcLENorm import DtcLENorm, DtcLENormWaarden
from ...Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm, DtcTrottoirbandVormWaarden
from ...Datatypes.KlLETrottoirbandWatergreppelType import KlLETrottoirbandWatergreppelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandWatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, die een trottoirband en een watergreppel combineert in een geheel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', direction='i')  # i = direction: incoming

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.norm',
                                  definition='De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlLETrottoirbandWatergreppelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.type',
                                  definition='Het type van gestandaardiseerde trottoirband_watergreppel.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.vorm',
                                  definition='De vorm van de gestandaardiseerde trottoirband_watergreppel.',
                                  owner=self)

    @property
    def norm(self) -> DtcLENormWaarden:
        """De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van gestandaardiseerde trottoirband_watergreppel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self) -> DtcTrottoirbandVormWaarden:
        """De vorm van de gestandaardiseerde trottoirband_watergreppel."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
