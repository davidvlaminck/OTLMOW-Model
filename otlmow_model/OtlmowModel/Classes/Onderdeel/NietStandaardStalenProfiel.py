# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StalenProfiel import StalenProfiel
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietStandaardStalenProfiel(StalenProfiel):
    """Een stalen constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. Niet-standaard stalen profiel omvat alle speciale,op maat gemaakte en/of niet vaak voorkomende profielen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MVPaal', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._detailDwarsdoorsnede = OTLAttribuut(field=DtcDocument,
                                                  naam='detailDwarsdoorsnede',
                                                  label='detail dwarsdoorsnede',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.detailDwarsdoorsnede',
                                                  definition='Details van de afmetingen en van de dwarsdoorsnedes.',
                                                  owner=self)

        self._profielbreedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='profielbreedte',
                                            label='profielbreedte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielbreedte',
                                            usagenote='Attribuut uit gebruik sinds versie 2.5.0 ',
                                            deprecated_version='2.5.0',
                                            definition='De korte afmeting in millimeter van het profiel.',
                                            owner=self)

        self._profielhoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='profielhoogte',
                                           label='profielhoogte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielhoogte',
                                           usagenote='Attribuut uit gebruik sinds versie 2.5.0 ',
                                           deprecated_version='2.5.0',
                                           definition='De langste afmeting in millimeter van het profiel.',
                                           owner=self)

    @property
    def detailDwarsdoorsnede(self) -> DtcDocumentWaarden:
        """Details van de afmetingen en van de dwarsdoorsnedes."""
        return self._detailDwarsdoorsnede.get_waarde()

    @detailDwarsdoorsnede.setter
    def detailDwarsdoorsnede(self, value):
        self._detailDwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def profielbreedte(self) -> KwantWrdInMillimeterWaarden:
        """De korte afmeting in millimeter van het profiel."""
        return self._profielbreedte.get_waarde()

    @profielbreedte.setter
    def profielbreedte(self, value):
        self._profielbreedte.set_waarde(value, owner=self)

    @property
    def profielhoogte(self) -> KwantWrdInMillimeterWaarden:
        """De langste afmeting in millimeter van het profiel."""
        return self._profielhoogte.get_waarde()

    @profielhoogte.setter
    def profielhoogte(self, value):
        self._profielhoogte.set_waarde(value, owner=self)
