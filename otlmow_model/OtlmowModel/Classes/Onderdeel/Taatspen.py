# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalDeklaag import KlMateriaalDeklaag
from ...Datatypes.KlMateriaalTaatsmechanisme import KlMateriaalTaatsmechanisme
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taatspen(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een onderdeel dat de verbinding maakt tussen de taatsschoen en taatspot binnen het taatsmechanisme."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspot', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftHouder = OTLAttribuut(field=BooleanField,
                                         naam='heeftHouder',
                                         label='heeft houder',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen.heeftHouder',
                                         definition='Geeft aan of de taatspen een houder heeft of niet.',
                                         owner=self)

        self._materiaalDeklaag = OTLAttribuut(field=KlMateriaalDeklaag,
                                              naam='materiaalDeklaag',
                                              label='materiaal deklaag',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen.materiaalDeklaag',
                                              definition='Het materiaal van het deklaag',
                                              owner=self)

        self._materiaalTaatspen = OTLAttribuut(field=KlMateriaalTaatsmechanisme,
                                               naam='materiaalTaatspen',
                                               label='materiaal taatspen',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen.materiaalTaatspen',
                                               definition='Het materiaal van de taatspen.',
                                               owner=self)

    @property
    def heeftHouder(self) -> bool:
        """Geeft aan of de taatspen een houder heeft of niet."""
        return self._heeftHouder.get_waarde()

    @heeftHouder.setter
    def heeftHouder(self, value):
        self._heeftHouder.set_waarde(value, owner=self)

    @property
    def materiaalDeklaag(self) -> str:
        """Het materiaal van het deklaag"""
        return self._materiaalDeklaag.get_waarde()

    @materiaalDeklaag.setter
    def materiaalDeklaag(self, value):
        self._materiaalDeklaag.set_waarde(value, owner=self)

    @property
    def materiaalTaatspen(self) -> str:
        """Het materiaal van de taatspen."""
        return self._materiaalTaatspen.get_waarde()

    @materiaalTaatspen.setter
    def materiaalTaatspen(self, value):
        self._materiaalTaatspen.set_waarde(value, owner=self)
