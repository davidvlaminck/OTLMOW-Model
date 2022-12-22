# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.IPNetwerkToegangObject import IPNetwerkToegangObject
from otlmow_model.Classes.Abstracten.RHZModule import RHZModule
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlAlarmModuleMerk import KlAlarmModuleMerk
from otlmow_model.Datatypes.KlAlarmModuleModelnaam import KlAlarmModuleModelnaam
from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AlarmModule(IPNetwerkToegangObject, RHZModule, SerienummerObject, AIMNaamObject):
    """Module binnen een installatie, waar de verschillende alarmen van andere modules toekomen, en die via het netwerk doorgestuurd kunnen worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AlarmModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        IPNetwerkToegangObject.__init__(self)
        RHZModule.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._aantalAlarmen = OTLAttribuut(field=NonNegIntegerField,
                                           naam='aantalAlarmen',
                                           label='aantal alarmen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AlarmModule.aantalAlarmen',
                                           definition='Het aantal verschillende configureerbare alarmen dat de alarmmodule telt.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlAlarmModuleMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AlarmModule.merk',
                                  definition='Merknaam van de alarm module.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlAlarmModuleModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AlarmModule.modelnaam',
                                       definition='Modelnaam van de alarm module.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AlarmModule.technischeFiche',
                                             definition='De technische fiche van de alarm module.',
                                             owner=self)

    @property
    def aantalAlarmen(self) -> int:
        """Het aantal verschillende configureerbare alarmen dat de alarmmodule telt."""
        return self._aantalAlarmen.get_waarde()

    @aantalAlarmen.setter
    def aantalAlarmen(self, value):
        self._aantalAlarmen.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de alarm module."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de alarm module."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de alarm module."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
