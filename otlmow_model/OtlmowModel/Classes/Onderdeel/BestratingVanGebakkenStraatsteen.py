# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Bestrating import Bestrating
from ...Datatypes.KlFormaatGebakkenStraatsteen import KlFormaatGebakkenStraatsteen
from ...Datatypes.KlStandaardkwaliteitsklasse import KlStandaardkwaliteitsklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGebakkenStraatsteen(Bestrating):
    """Gebakken straatstenen zijn straatstenen, in hoofdzaak vervaardigd uit klei al dan niet gemengd met leem, zand, brandstoffen of andere toeslagstoffen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen'
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

        self._formaatVanBestratingselement = OTLAttribuut(field=KlFormaatGebakkenStraatsteen,
                                                          naam='formaatVanBestratingselement',
                                                          label='formaat van bestratingselement',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.formaatVanBestratingselement',
                                                          definition='Bepaling van de afmeting van het bestratingselement.',
                                                          owner=self)

        self._standaardkwaliteitsklasse = OTLAttribuut(field=KlStandaardkwaliteitsklasse,
                                                       naam='standaardkwaliteitsklasse',
                                                       label='standaardkwaliteitsklasse',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.standaardkwaliteitsklasse',
                                                       definition='De standaardkwaliteitsklasse volgens PTV 910.',
                                                       owner=self)

    @property
    def formaatVanBestratingselement(self) -> str:
        """Bepaling van de afmeting van het bestratingselement."""
        return self._formaatVanBestratingselement.get_waarde()

    @formaatVanBestratingselement.setter
    def formaatVanBestratingselement(self, value):
        self._formaatVanBestratingselement.set_waarde(value, owner=self)

    @property
    def standaardkwaliteitsklasse(self) -> str:
        """De standaardkwaliteitsklasse volgens PTV 910."""
        return self._standaardkwaliteitsklasse.get_waarde()

    @standaardkwaliteitsklasse.setter
    def standaardkwaliteitsklasse(self, value):
        self._standaardkwaliteitsklasse.set_waarde(value, owner=self)
