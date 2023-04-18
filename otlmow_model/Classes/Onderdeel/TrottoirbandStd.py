# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from otlmow_model.Datatypes.DtcLENorm import DtcLENorm, DtcLENormWaarden
from otlmow_model.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm, DtcTrottoirbandVormWaarden
from otlmow_model.Datatypes.KlLETrottoirbandType import KlLETrottoirbandType


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting,bestemd om de rand van de verharding te beschermen en te versterken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd')

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.norm',
                                  definition='De gestandaardiseerde trottoirband volgens aangeduide norm.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlLETrottoirbandType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.type',
                                  definition='Bepaling van het type van trottoirband.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.vorm',
                                  definition='Bepaling van de vorm van de trottoirband.',
                                  owner=self)

    @property
    def norm(self) -> DtcLENormWaarden:
        """De gestandaardiseerde trottoirband volgens aangeduide norm."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Bepaling van het type van trottoirband."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self) -> DtcTrottoirbandVormWaarden:
        """Bepaling van de vorm van de trottoirband."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
