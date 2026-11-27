# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalVoegplaat import KlMateriaalVoegplaat
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voegplaat(AIMNaamObject, PuntGeometrie):
    """Een plaatvormig element dat in voegen van betonconstructies wordt aangebracht. Wordt veelal voorzien t.p.v. (gronddichte) uitzettingsvoegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._materiaalVoegplaat = OTLAttribuut(field=KlMateriaalVoegplaat,
                                                naam='materiaalVoegplaat',
                                                label='materiaal voegplaat',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegplaat.materiaalVoegplaat',
                                                definition='De verschillende opties van materiaal voor voegplaten.',
                                                owner=self)

    @property
    def materiaalVoegplaat(self) -> str:
        """De verschillende opties van materiaal voor voegplaten."""
        return self._materiaalVoegplaat.get_waarde()

    @materiaalVoegplaat.setter
    def materiaalVoegplaat(self, value):
        self._materiaalVoegplaat.set_waarde(value, owner=self)
