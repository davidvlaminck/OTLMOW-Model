# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.FirmwareObject import FirmwareObject
from otlmow_model.Classes.Abstracten.IPNetwerkToegangObject import IPNetwerkToegangObject
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlIPModuleTGCMerk import KlIPModuleTGCMerk
from otlmow_model.Datatypes.KlIPModuleTGCModelnaam import KlIPModuleTGCModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class IPModuleTGC(ElektrischComponentennummerObject, FirmwareObject, IPNetwerkToegangObject, SerienummerObject, AIMNaamObject):
    """Deze controller voorziet de verbinding tussen de centrale server en de lokale toegangscontroller. Deze verbinding gebeurt over het IP-netwerk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IPModuleTGC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        ElektrischComponentennummerObject.__init__(self)
        FirmwareObject.__init__(self)
        IPNetwerkToegangObject.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeurmoduleTGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller')

        self._merk = OTLAttribuut(field=KlIPModuleTGCMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IPModuleTGC.merk',
                                  definition='Het merk van de IP-Toegangscontroller.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIPModuleTGCModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IPModuleTGC.modelnaam',
                                       definition='De modelnaam van de IP-Toegangscontroller.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de IP-Toegangscontroller."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de IP-Toegangscontroller."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
