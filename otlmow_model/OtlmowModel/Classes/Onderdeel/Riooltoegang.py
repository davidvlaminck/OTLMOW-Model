# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Put import Put
from ...Classes.Abstracten.PutRelatie import PutRelatie
from ...Datatypes.KlUitlaatType import KlUitlaatType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riooltoegang(Put, PutRelatie, PuntGeometrie):
    """Het uiteinde van een rioolbuis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WaterdoorvoerendeDuiker', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._typeRiooltoegang = OTLAttribuut(field=KlUitlaatType,
                                              naam='typeRiooltoegang',
                                              label='type riooltoegang',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang.typeRiooltoegang',
                                              definition='Bepaalt het type van een riooltoegang.',
                                              owner=self)

    @property
    def typeRiooltoegang(self) -> str:
        """Bepaalt het type van een riooltoegang."""
        return self._typeRiooltoegang.get_waarde()

    @typeRiooltoegang.setter
    def typeRiooltoegang(self, value):
        self._typeRiooltoegang.set_waarde(value, owner=self)
