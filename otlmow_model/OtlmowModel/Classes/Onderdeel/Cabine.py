# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Inloopbehuizing import Inloopbehuizing
from ...Datatypes.KlCabineAardingsstelsel import KlCabineAardingsstelsel
from ...Datatypes.KlCabineStandaardtype import KlCabineStandaardtype
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cabine(Inloopbehuizing, VlakGeometrie):
    """Een behuizing voornamelijk bestemd voor het beschermen van elektromechanische technieken waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', direction='u')  # u = unidirectional

        self._aardingsstelsel = OTLAttribuut(field=KlCabineAardingsstelsel,
                                             naam='aardingsstelsel',
                                             label='aardingsstelsel',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.aardingsstelsel',
                                             usagenote='Attribuut uit gebruik sinds versie 2.7.0 ',
                                             deprecated_version='2.7.0',
                                             definition='Keuze tussen verschillende types voor het gebruikte aardingsstelsel.',
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

    @property
    def aardingsstelsel(self) -> str:
        """Keuze tussen verschillende types voor het gebruikte aardingsstelsel."""
        return self._aardingsstelsel.get_waarde()

    @aardingsstelsel.setter
    def aardingsstelsel(self, value):
        self._aardingsstelsel.set_waarde(value, owner=self)

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
