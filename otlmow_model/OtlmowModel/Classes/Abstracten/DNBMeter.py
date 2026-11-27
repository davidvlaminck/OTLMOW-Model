# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Energiemeter import Energiemeter
from ...Datatypes.KlEnergiemeterDNBMeteropnameFrequentie import (
    KlEnergiemeterDNBMeteropnameFrequentie,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBMeter(Energiemeter):
    """Abstracte voor elk toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor diverse metingen van doorgevoerde energie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._meteropnameFrequentie = OTLAttribuut(field=KlEnergiemeterDNBMeteropnameFrequentie,
                                                   naam='meteropnameFrequentie',
                                                   label='meteropname frequentie',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter.meteropnameFrequentie',
                                                   definition='Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder.',
                                                   owner=self)

    @property
    def meteropnameFrequentie(self) -> str:
        """Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder."""
        return self._meteropnameFrequentie.get_waarde()

    @meteropnameFrequentie.setter
    def meteropnameFrequentie(self, value):
        self._meteropnameFrequentie.set_waarde(value, owner=self)
