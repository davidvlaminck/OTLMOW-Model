# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.PTModuleMetFirmware import PTModuleMetFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTVerwerkingseenheid(PTModuleMetFirmware):
    """Ook LS-kaart of Local Stationkaart genoemd, de centrale verwerkingseenheid die in verbinding staat met één of meerdere demodulatoren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTVerwerkingseenheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTDemodulatoren', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
