# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Buis import Buis
from ...Classes.Abstracten.BVAfwateringKunstwerken import BVAfwateringKunstwerken
from ...Datatypes.KlDraineerbuisMateriaal import KlDraineerbuisMateriaal
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draineerbuis(BVAfwateringKunstwerken, Buis, PuntGeometrie):
    """Een buis voor het afvoeren van water uit de bodem over en door de grond,met als gevolg het verlagen van het grondwaterpeil."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', '2.8.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftDrainbrug = OTLAttribuut(field=BooleanField,
                                            naam='heeftDrainbrug',
                                            label='heeft drainbrug',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.heeftDrainbrug',
                                            definition='Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden.',
                                            owner=self)

        self._materiaal = OTLAttribuut(field=KlDraineerbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.materiaal',
                                       definition='Bepaalt het materiaal van de draineerbuis.',
                                       owner=self)

    @property
    def heeftDrainbrug(self) -> bool:
        """Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden."""
        return self._heeftDrainbrug.get_waarde()

    @heeftDrainbrug.setter
    def heeftDrainbrug(self, value):
        self._heeftDrainbrug.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de draineerbuis."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
