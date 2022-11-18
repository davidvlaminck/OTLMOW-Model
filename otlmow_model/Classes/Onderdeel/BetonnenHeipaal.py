# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from otlmow_model.Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlTypeSchachtHeipaal import KlTypeSchachtHeipaal
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenHeipaal(BetonnenConstructieElement, Funderingspaal):
    """Betonnen paal die in de grond wordt gebracht door deze in een hei-installatie te plaatsen waarna men er een zwaar gewicht (heiblok) op laat vallen. De grond onder de paal wordt samengeperst waardoor de draagkracht groter wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BetonnenConstructieElement.__init__(self)
        Funderingspaal.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')

        self._diameterPaalschacht = OTLAttribuut(field=KwantWrdInMillimeter,
                                                 naam='diameterPaalschacht',
                                                 label='diameter paalschacht',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.diameterPaalschacht',
                                                 definition='Doorsnede in millimeter van de schacht van de paal.',
                                                 owner=self)

        self._heeftVerbredeVoet = OTLAttribuut(field=BooleanField,
                                               naam='heeftVerbredeVoet',
                                               label='heeft verbrede voet',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.heeftVerbredeVoet',
                                               definition='Geeft aan of de voet breder is gemaakt, al dan niet.',
                                               owner=self)

        self._heeftVerlorenVoerbuis = OTLAttribuut(field=BooleanField,
                                                   naam='heeftVerlorenVoerbuis',
                                                   label='heeft verloren voerbuis',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.heeftVerlorenVoerbuis',
                                                   definition='Aanduiding of de heipaal een verloren voerbuis heeft.',
                                                   owner=self)

        self._typeSchacht = OTLAttribuut(field=KlTypeSchachtHeipaal,
                                         naam='typeSchacht',
                                         label='type schacht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.typeSchacht',
                                         definition='De soort schacht van de heipaal.',
                                         owner=self)

    @property
    def diameterPaalschacht(self) -> KwantWrdInMillimeterWaarden:
        """Doorsnede in millimeter van de schacht van de paal."""
        return self._diameterPaalschacht.get_waarde()

    @diameterPaalschacht.setter
    def diameterPaalschacht(self, value):
        self._diameterPaalschacht.set_waarde(value, owner=self)

    @property
    def heeftVerbredeVoet(self) -> bool:
        """Geeft aan of de voet breder is gemaakt, al dan niet."""
        return self._heeftVerbredeVoet.get_waarde()

    @heeftVerbredeVoet.setter
    def heeftVerbredeVoet(self, value):
        self._heeftVerbredeVoet.set_waarde(value, owner=self)

    @property
    def heeftVerlorenVoerbuis(self) -> bool:
        """Aanduiding of de heipaal een verloren voerbuis heeft."""
        return self._heeftVerlorenVoerbuis.get_waarde()

    @heeftVerlorenVoerbuis.setter
    def heeftVerlorenVoerbuis(self, value):
        self._heeftVerlorenVoerbuis.set_waarde(value, owner=self)

    @property
    def typeSchacht(self) -> str:
        """De soort schacht van de heipaal."""
        return self._typeSchacht.get_waarde()

    @typeSchacht.setter
    def typeSchacht(self, value):
        self._typeSchacht.set_waarde(value, owner=self)
