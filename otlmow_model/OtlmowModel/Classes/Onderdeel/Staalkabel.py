# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlSlagrichting import KlSlagrichting
from ...Datatypes.KlVetType import KlVetType
from ...Datatypes.KwantWrdInMegaPascal import (
    KwantWrdInMegaPascal,
    KwantWrdInMegaPascalWaarden,
)
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Staalkabel(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een kabel die bestaat uit meerdere strengen,waarbij elke streng afzonderlijk is opgebouwd uit gewikkelde staaldraden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Staalkabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AsLagerCombinatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aangrijpingsstoel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Evenaar', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelspanner', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabeltrommel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RegelbaarTegengewicht', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VastTegengewicht', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelbewegingsmechanisme', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingssteun', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelsteun', 'o', '2.21.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Keerwiel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rol', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._diameterKabel = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='diameterKabel',
                                           label='diameter kabel',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Staalkabel.diameterKabel',
                                           definition='De diameter van de staalkabel, uitgedrukt in millimeter.',
                                           owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Staalkabel.lengte',
                                    definition='De lengte van de staalkabel, uitgedrukt in meter.',
                                    owner=self)

        self._slagrichting = OTLAttribuut(field=KlSlagrichting,
                                          naam='slagrichting',
                                          label='slagrichting',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Staalkabel.slagrichting',
                                          definition='De slagrichting geeft aan op welke wijze de strengen rond de kern worden geslagen.',
                                          owner=self)

        self._treksterkte = OTLAttribuut(field=KwantWrdInMegaPascal,
                                         naam='treksterkte',
                                         label='treksterkte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Staalkabel.treksterkte',
                                         definition='De treksterkte van een staalkabel is de maximale trekkracht die de staalkabel aan kan.',
                                         owner=self)

        self._typeVet = OTLAttribuut(field=KlVetType,
                                     naam='typeVet',
                                     label='type vet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Staalkabel.typeVet',
                                     definition='Geeft aan met welk type vet de staalkabel gesmeerd is.',
                                     owner=self)

    @property
    def diameterKabel(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de staalkabel, uitgedrukt in millimeter."""
        return self._diameterKabel.get_waarde()

    @diameterKabel.setter
    def diameterKabel(self, value):
        self._diameterKabel.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de staalkabel, uitgedrukt in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def slagrichting(self) -> str:
        """De slagrichting geeft aan op welke wijze de strengen rond de kern worden geslagen."""
        return self._slagrichting.get_waarde()

    @slagrichting.setter
    def slagrichting(self, value):
        self._slagrichting.set_waarde(value, owner=self)

    @property
    def treksterkte(self) -> KwantWrdInMegaPascalWaarden:
        """De treksterkte van een staalkabel is de maximale trekkracht die de staalkabel aan kan."""
        return self._treksterkte.get_waarde()

    @treksterkte.setter
    def treksterkte(self, value):
        self._treksterkte.set_waarde(value, owner=self)

    @property
    def typeVet(self) -> str:
        """Geeft aan met welk type vet de staalkabel gesmeerd is."""
        return self._typeVet.get_waarde()

    @typeVet.setter
    def typeVet(self, value):
        self._typeVet.set_waarde(value, owner=self)
