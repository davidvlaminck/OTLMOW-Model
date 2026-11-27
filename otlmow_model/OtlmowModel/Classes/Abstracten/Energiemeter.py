# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.IntegerField import IntegerField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlEnergiemeterMetertype import KlEnergiemeterMetertype
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Energiemeter(AIMNaamObject, PuntGeometrie):
    """Abstracte voor alle energiemeters."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aantalTelwerken = OTLAttribuut(field=IntegerField,
                                             naam='aantalTelwerken',
                                             label='aantal telwerken',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.aantalTelwerken',
                                             definition='Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter.',
                                             owner=self)

        self._meternummer = OTLAttribuut(field=StringField,
                                         naam='meternummer',
                                         label='meternummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.meternummer',
                                         definition='Het serienummer (nummer van het fabrikaat) op de meter.',
                                         owner=self)

        self._metertype = OTLAttribuut(field=KlEnergiemeterMetertype,
                                       naam='metertype',
                                       label='metertype',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.metertype',
                                       definition='Type meter (mechanisch, elektronisch).',
                                       owner=self)

    @property
    def aantalTelwerken(self) -> int:
        """Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter."""
        return self._aantalTelwerken.get_waarde()

    @aantalTelwerken.setter
    def aantalTelwerken(self, value):
        self._aantalTelwerken.set_waarde(value, owner=self)

    @property
    def meternummer(self) -> str:
        """Het serienummer (nummer van het fabrikaat) op de meter."""
        return self._meternummer.get_waarde()

    @meternummer.setter
    def meternummer(self, value):
        self._meternummer.set_waarde(value, owner=self)

    @property
    def metertype(self) -> str:
        """Type meter (mechanisch, elektronisch)."""
        return self._metertype.get_waarde()

    @metertype.setter
    def metertype(self, value):
        self._metertype.set_waarde(value, owner=self)
