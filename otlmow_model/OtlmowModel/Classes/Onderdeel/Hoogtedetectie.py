# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlHoogtedetectieMerk import KlHoogtedetectieMerk
from ...Datatypes.KlHoogtedetectieModelnaam import KlHoogtedetectieModelnaam
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoogtedetectie(NaampadObject, PuntGeometrie):
    """Hoogtedetectiesysteem voor het voorkomen van schade aan kunstwerken. Stuurt vaak een dynamisch bord aan. Voor handhaving staat het in relatie met een ANPR-camera."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._detectiehoogte = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='detectiehoogte',
                                            label='detectiehoogte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.detectiehoogte',
                                            definition='De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen.',
                                            owner=self)

        self._merk = OTLAttribuut(field=KlHoogtedetectieMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.merk',
                                  usagenote='volgens een keuzelijst',
                                  definition='Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHoogtedetectieModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.modelnaam',
                                       usagenote='Uit een keuzelijst.',
                                       definition='De modelnaam van de hoogtedetectie.',
                                       owner=self)

    @property
    def detectiehoogte(self) -> KwantWrdInMeterWaarden:
        """De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen."""
        return self._detectiehoogte.get_waarde()

    @detectiehoogte.setter
    def detectiehoogte(self, value):
        self._detectiehoogte.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de hoogtedetectie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
