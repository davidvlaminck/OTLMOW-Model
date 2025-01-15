# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcLENorm import DtcLENorm, DtcLENormWaarden
from ...Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm, DtcTrottoirbandVormWaarden
from ...Datatypes.KlLEWatergreppelType import KlLEWatergreppelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting,bestemd om water van de verharding op te vangen en af te voeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', direction='i')  # i = direction: incoming

        self._isVerholen = OTLAttribuut(field=BooleanField,
                                        naam='isVerholen',
                                        label='is verholen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.isVerholen',
                                        usagenote='Attribuut uit gebruik sinds versie 2.14.0 ',
                                        deprecated_version='2.14.0',
                                        definition='Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit.',
                                        owner=self)

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.norm',
                                  definition='De gestandaardiseerde watergreppel volgens aangeduide norm.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlLEWatergreppelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.type',
                                  definition='Het type van gestandaardiseerde watergreppel.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.vorm',
                                  definition='De vorm van de watergreppel.',
                                  owner=self)

    @property
    def isVerholen(self) -> bool:
        """Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit."""
        return self._isVerholen.get_waarde()

    @isVerholen.setter
    def isVerholen(self, value):
        self._isVerholen.set_waarde(value, owner=self)

    @property
    def norm(self) -> DtcLENormWaarden:
        """De gestandaardiseerde watergreppel volgens aangeduide norm."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van gestandaardiseerde watergreppel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self) -> DtcTrottoirbandVormWaarden:
        """De vorm van de watergreppel."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
