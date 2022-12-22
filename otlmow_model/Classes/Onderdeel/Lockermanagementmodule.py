# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlLockermanagementmoduleMerk import KlLockermanagementmoduleMerk
from otlmow_model.Datatypes.KlLockermanagementmoduleModelnaam import KlLockermanagementmoduleModelnaam
from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lockermanagementmodule(AIMNaamObject, PuntGeometrie):
    """Inrichting voor het beheer van lockerkasten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockermanagementmodule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockerkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._aantalLockers = OTLAttribuut(field=NonNegIntegerField,
                                           naam='aantalLockers',
                                           label='aantal lockers',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockermanagementmodule.aantalLockers',
                                           definition='Het aantal lockers dat door deze module wordt beheerd.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlLockermanagementmoduleMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockermanagementmodule.merk',
                                  definition='Het merk van de lockermanagementmodule.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLockermanagementmoduleModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockermanagementmodule.modelnaam',
                                       definition='De modelnaam van de lockermanagementmodule.',
                                       owner=self)

    @property
    def aantalLockers(self) -> int:
        """Het aantal lockers dat door deze module wordt beheerd."""
        return self._aantalLockers.get_waarde()

    @aantalLockers.setter
    def aantalLockers(self, value):
        self._aantalLockers.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de lockermanagementmodule."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de lockermanagementmodule."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
