# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAfmetingBxlxhInM import (
    DtcAfmetingBxlxhInM,
    DtcAfmetingBxlxhInMWaarden,
)
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sluisvloertegel(BetonnenConstructieElement, AIMNaamObject, VlakGeometrie):
    """Een betontegel met grote afmetingen specifiek van toepassing voor de bodem van een sluis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sluisvloertegel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerlaag', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInM,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sluisvloertegel.afmetingen',
                                        definition='De afmetingen van de sluisvloertegel: breedte, lengte en hoogte, uitgedrukt in meter.',
                                        owner=self)

        self._heeftVoegbanden = OTLAttribuut(field=BooleanField,
                                             naam='heeftVoegbanden',
                                             label='heeft voegbanden',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sluisvloertegel.heeftVoegbanden',
                                             definition='Geeft aan of de sluisvloertegel al dan niet voegbanden heeft',
                                             owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlxhInMWaarden:
        """De afmetingen van de sluisvloertegel: breedte, lengte en hoogte, uitgedrukt in meter."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def heeftVoegbanden(self) -> bool:
        """Geeft aan of de sluisvloertegel al dan niet voegbanden heeft"""
        return self._heeftVoegbanden.get_waarde()

    @heeftVoegbanden.setter
    def heeftVoegbanden(self, value):
        self._heeftVoegbanden.set_waarde(value, owner=self)
