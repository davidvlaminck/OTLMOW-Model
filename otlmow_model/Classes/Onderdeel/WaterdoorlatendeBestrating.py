# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Bestrating import Bestrating
from otlmow_model.Datatypes.KlAardWBSS import KlAardWBSS
from otlmow_model.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from otlmow_model.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB
from otlmow_model.Datatypes.KlWBSSType import KlWBSSType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WaterdoorlatendeBestrating(Bestrating):
    """Betonstraatstenen of betontegels die omwille van hun vormkenmerken (bv. drainageopeningen of verbrede voegen) of betonstructuur (poreus beton met een open korrelopbouw) water doorlaten zoals omschreven in PTV 122."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._aard = OTLAttribuut(field=KlAardWBSS,
                                  naam='aard',
                                  label='aard',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.aard',
                                  definition='Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is.',
                                  owner=self)

        self._afmetingVanBestratingselementLxB = OTLAttribuut(field=KlBestratingselementAfmetingLxB,
                                                              naam='afmetingVanBestratingselementLxB',
                                                              label='afmeting van bestratingselement LxB',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afmetingVanBestratingselementLxB',
                                                              definition='De lengte en breedte van het bestratingselement in millimeter.',
                                                              owner=self)

        self._afwerking = OTLAttribuut(field=KlBestratingAfwerking,
                                       naam='afwerking',
                                       label='afwerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afwerking',
                                       definition='Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlWBSSType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.type',
                                  definition='Het type van waterdoorlatende betonstraatstenen of betontegels.',
                                  owner=self)

    @property
    def aard(self) -> str:
        """Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is."""
        return self._aard.get_waarde()

    @aard.setter
    def aard(self, value):
        self._aard.set_waarde(value, owner=self)

    @property
    def afmetingVanBestratingselementLxB(self) -> str:
        """De lengte en breedte van het bestratingselement in millimeter."""
        return self._afmetingVanBestratingselementLxB.get_waarde()

    @afmetingVanBestratingselementLxB.setter
    def afmetingVanBestratingselementLxB(self, value):
        self._afmetingVanBestratingselementLxB.set_waarde(value, owner=self)

    @property
    def afwerking(self) -> str:
        """Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels."""
        return self._afwerking.get_waarde()

    @afwerking.setter
    def afwerking(self, value):
        self._afwerking.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van waterdoorlatende betonstraatstenen of betontegels."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
