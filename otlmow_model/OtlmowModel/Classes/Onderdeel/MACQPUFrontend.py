# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.PU import PU


# Generated with OTLClassCreator. To modify: extend, do not edit
class MACQPUFrontend(PU):
    """Een processing unit van MACQ die de link legt tussen de AID-module en de AID-push server en de correlatiemodule."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MACQPUFrontend'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
