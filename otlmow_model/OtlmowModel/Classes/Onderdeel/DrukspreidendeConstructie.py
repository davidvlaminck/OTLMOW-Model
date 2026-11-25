# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereLaag import AndereLaag
from ...Classes.Abstracten.LaagDikte import LaagDikte


# Generated with OTLClassCreator. To modify: extend, do not edit
class DrukspreidendeConstructie(AndereLaag, LaagDikte):
    """Een ondergrondse constructieve laag, geplaatst tussen verharding en groeimedium of ondergrond (bv. doorwortelbare fundering), bedoeld om belastingen te spreiden, bodemverdichting te beperken en opdruk van de verharding door wortelgroei te voorkomen, meestal uitgevoerd met sandwichpanelen of gelijkaardige prefab-units."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DrukspreidendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftBoomkratsubstraat = OTLAttribuut(field=BooleanField,
                                                    naam='heeftBoomkratsubstraat',
                                                    label='heeft boomkratsubstraat',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DrukspreidendeConstructie.heeftBoomkratsubstraat',
                                                    definition='Duidt aan of de prefab-units al dan niet opgevuld zijn met boomkratsubstraat.',
                                                    owner=self)

    @property
    def heeftBoomkratsubstraat(self) -> bool:
        """Duidt aan of de prefab-units al dan niet opgevuld zijn met boomkratsubstraat."""
        return self._heeftBoomkratsubstraat.get_waarde()

    @heeftBoomkratsubstraat.setter
    def heeftBoomkratsubstraat(self, value):
        self._heeftBoomkratsubstraat.set_waarde(value, owner=self)
