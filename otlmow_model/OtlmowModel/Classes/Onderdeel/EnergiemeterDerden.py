# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.Energiemeter import Energiemeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class EnergiemeterDerden(Energiemeter):
    """Toestel dat eigendom is van een derde partij, verschillend van de distributienetbeheerder, waarmee het energieverbruik van de installaties van deze derden gemeten wordt. Deze energiemeters komen enkel voor op: - installaties van AWV waarop derden een afzonderlijke kring hebben gekregen voor het voeden van hun eigen installaties - installaties van derden waarop AWV een afzonderlijke kring heeft gekregen voor het voeden van onze installaties"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDerden'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedingDerdenLaagspanning', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
