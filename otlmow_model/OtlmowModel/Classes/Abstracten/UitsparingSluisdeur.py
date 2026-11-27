# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlVastAanslagmateriaal import KlVastAanslagmateriaal
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class UitsparingSluisdeur(VlakGeometrie):
    """Een abstracte om eigenschappen en relaties van de uitsparingen te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd', 'o', None),  # o = direction: outgoing
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._detailplan = OTLAttribuut(field=DtcDocument,
                                        naam='detailplan',
                                        label='detailplan',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur.detailplan',
                                        definition='Het detailplan van de uitsparing.',
                                        owner=self)

        self._vastAanslagmateriaal = OTLAttribuut(field=KlVastAanslagmateriaal,
                                                  naam='vastAanslagmateriaal',
                                                  label='vast aanslagmateriaal',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur.vastAanslagmateriaal',
                                                  definition='De verschillende mogelijkheden m.b.t. het materiaal van de aanslag',
                                                  owner=self)

    @property
    def detailplan(self) -> DtcDocumentWaarden:
        """Het detailplan van de uitsparing."""
        return self._detailplan.get_waarde()

    @detailplan.setter
    def detailplan(self, value):
        self._detailplan.set_waarde(value, owner=self)

    @property
    def vastAanslagmateriaal(self) -> str:
        """De verschillende mogelijkheden m.b.t. het materiaal van de aanslag"""
        return self._vastAanslagmateriaal.get_waarde()

    @vastAanslagmateriaal.setter
    def vastAanslagmateriaal(self, value):
        self._vastAanslagmateriaal.set_waarde(value, owner=self)
