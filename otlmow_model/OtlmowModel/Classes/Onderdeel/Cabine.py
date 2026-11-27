# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Inloopbehuizing import Inloopbehuizing
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlCabineAardingsstelsel import KlCabineAardingsstelsel
from ...Datatypes.KlCabineStandaardtype import KlCabineStandaardtype
from ...Datatypes.KlNetwerklocatie import KlNetwerklocatie
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cabine(Inloopbehuizing, NaampadObject, PuntGeometrie, VlakGeometrie):
    """Een behuizing voornamelijk bestemd voor het beschermen van elektromechanische technieken waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TTSegment', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aardingsstelsel = OTLAttribuut(field=KlCabineAardingsstelsel,
                                             naam='aardingsstelsel',
                                             label='aardingsstelsel',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.aardingsstelsel',
                                             usagenote='Attribuut uit gebruik sinds versie 2.7.0 ',
                                             deprecated_version='2.7.0',
                                             definition='Keuze tussen verschillende types voor het gebruikte aardingsstelsel.',
                                             owner=self)

        self._heeftIsolatie = OTLAttribuut(field=BooleanField,
                                           naam='heeftIsolatie',
                                           label='heeft isolatie',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.heeftIsolatie',
                                           definition='Geeft aan of de cabine is voorzien van isolatie.',
                                           owner=self)

        self._kelderdiepte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='kelderdiepte',
                                          label='kelderdiepte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.kelderdiepte',
                                          definition='Binnenhoogte in meter van de kabelkelder onder de cabine.',
                                          owner=self)

        self._standaardtype = OTLAttribuut(field=KlCabineStandaardtype,
                                           naam='standaardtype',
                                           label='standaardtype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.standaardtype',
                                           definition='Het type van de cabine volgens de gangbare standaarden.',
                                           owner=self)

        self._typeNetwerklocatie = OTLAttribuut(field=KlNetwerklocatie,
                                                naam='typeNetwerklocatie',
                                                label='keuzelijst netwerklocaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.typeNetwerklocatie',
                                                definition='De verschillende opties netwerklocatie.',
                                                owner=self)

    @property
    def aardingsstelsel(self) -> str:
        """Keuze tussen verschillende types voor het gebruikte aardingsstelsel."""
        return self._aardingsstelsel.get_waarde()

    @aardingsstelsel.setter
    def aardingsstelsel(self, value):
        self._aardingsstelsel.set_waarde(value, owner=self)

    @property
    def heeftIsolatie(self) -> bool:
        """Geeft aan of de cabine is voorzien van isolatie."""
        return self._heeftIsolatie.get_waarde()

    @heeftIsolatie.setter
    def heeftIsolatie(self, value):
        self._heeftIsolatie.set_waarde(value, owner=self)

    @property
    def kelderdiepte(self) -> KwantWrdInMeterWaarden:
        """Binnenhoogte in meter van de kabelkelder onder de cabine."""
        return self._kelderdiepte.get_waarde()

    @kelderdiepte.setter
    def kelderdiepte(self, value):
        self._kelderdiepte.set_waarde(value, owner=self)

    @property
    def standaardtype(self) -> str:
        """Het type van de cabine volgens de gangbare standaarden."""
        return self._standaardtype.get_waarde()

    @standaardtype.setter
    def standaardtype(self, value):
        self._standaardtype.set_waarde(value, owner=self)

    @property
    def typeNetwerklocatie(self) -> str:
        """De verschillende opties netwerklocatie."""
        return self._typeNetwerklocatie.get_waarde()

    @typeNetwerklocatie.setter
    def typeNetwerklocatie(self, value):
        self._typeNetwerklocatie.set_waarde(value, owner=self)
