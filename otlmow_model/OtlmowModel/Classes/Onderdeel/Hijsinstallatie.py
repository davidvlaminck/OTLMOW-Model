# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInKilogram import (
    KwantWrdInKilogram,
    KwantWrdInKilogramWaarden,
)
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hijsinstallatie(AIMNaamObject, PuntGeometrie):
    """Het geheel van werktuig met aandrijving bestemd voor het verticaal verplaatsen van vrij zware lasten of componenten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.21.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder', 'u', '2.21.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting', 'u', '2.21.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', 'o', '2.21.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', '2.21.0'),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._hijskracht = OTLAttribuut(field=KwantWrdInKilogram,
                                        naam='hijskracht',
                                        label='hijskracht',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie.hijskracht',
                                        usagenote='Klasse uit gebruik sinds versie 2.21.0 ',
                                        deprecated_version='2.21.0',
                                        definition='De maximale hijskracht in kilogram waarvoor de hijsinstallatie gekeurd is.',
                                        owner=self)

        self._maximaalNiveauverschil = OTLAttribuut(field=KwantWrdInMeter,
                                                    naam='maximaalNiveauverschil',
                                                    label='maximaal niveauverschil',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie.maximaalNiveauverschil',
                                                    usagenote='Klasse uit gebruik sinds versie 2.21.0 ',
                                                    deprecated_version='2.21.0',
                                                    definition='Het verticaal bereik van de hijsinstallatie.',
                                                    owner=self)

    @property
    def hijskracht(self) -> KwantWrdInKilogramWaarden:
        """De maximale hijskracht in kilogram waarvoor de hijsinstallatie gekeurd is."""
        return self._hijskracht.get_waarde()

    @hijskracht.setter
    def hijskracht(self, value):
        self._hijskracht.set_waarde(value, owner=self)

    @property
    def maximaalNiveauverschil(self) -> KwantWrdInMeterWaarden:
        """Het verticaal bereik van de hijsinstallatie."""
        return self._maximaalNiveauverschil.get_waarde()

    @maximaalNiveauverschil.setter
    def maximaalNiveauverschil(self, value):
        self._maximaalNiveauverschil.set_waarde(value, owner=self)
