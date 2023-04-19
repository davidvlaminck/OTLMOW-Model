# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from otlmow_model.Datatypes.DtcLENorm import DtcLENorm, DtcLENormWaarden
from otlmow_model.Datatypes.KlLESchampkantType import KlLESchampkantType
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class SchampkantStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, die zones van voertuigenverkeer onderling of voertuigenzones van andere verkeerszones scheidt en de overschrijding door voertuigen bemoeilijkt maar geen voertuigkerende functie heeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.breedte',
                                     definition='De breedte van de gestandaardiseerde schampkant in centimeter.',
                                     owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.dikte',
                                   definition='De dikte van de gestandaardiseerde schampkant in centimeter.',
                                   owner=self)

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.norm',
                                  definition='De gestandaardiseerde schampkant volgens aangeduide norm.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlLESchampkantType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.type',
                                  definition='Het type van gestandaardiseerde schampkant.',
                                  owner=self)

    @property
    def breedte(self) -> KwantWrdInCentimeterWaarden:
        """De breedte van de gestandaardiseerde schampkant in centimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInCentimeterWaarden:
        """De dikte van de gestandaardiseerde schampkant in centimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def norm(self) -> DtcLENormWaarden:
        """De gestandaardiseerde schampkant volgens aangeduide norm."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van gestandaardiseerde schampkant."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
