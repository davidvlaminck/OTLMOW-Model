# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.PTModuleZFirmware import PTModuleZFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTDemodulatoren(PTModuleZFirmware):
    """De functie van de demodulator bestaat erin de data,ontvangen door de lus,te decoderen en in het juiste formaat door te sturen naar de centrale verwerkingseenheid,de PT-verwerkingseenheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTDemodulatoren'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTVerwerkingseenheid', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
