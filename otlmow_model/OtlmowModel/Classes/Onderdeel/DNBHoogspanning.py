# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.Abstracten.DNB import DNB
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBHoogspanning(DNB, NaampadObject):
    """Aansluiting op het hoogspanningsnet van de distributienetbeheerder."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBHoogspanning'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSAankomstDNB', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._meternummer = OTLAttribuut(field=StringField,
                                         naam='meternummer',
                                         label='meternummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBHoogspanning.meternummer',
                                         definition='Het serienummer (nummer van het fabrikaat) op de meter.',
                                         owner=self)

    @property
    def meternummer(self) -> str:
        """Het serienummer (nummer van het fabrikaat) op de meter."""
        return self._meternummer.get_waarde()

    @meternummer.setter
    def meternummer(self, value):
        self._meternummer.set_waarde(value, owner=self)
