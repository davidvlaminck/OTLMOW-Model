# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlTypeMicropaal import KlTypeMicropaal
from ...Datatypes.KwantWrdInKubiekeMeterPerUur import (
    KwantWrdInKubiekeMeterPerUur,
    KwantWrdInKubiekeMeterPerUurWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class Micropaal(Funderingspaal):
    """In de grond gevormde paal met kleine diameter die bestaat uit een stalen inbouwelement (staaf) waarrond een groutkolom wordt gevormd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerankeringsplaatMicropaal', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._typeMicropaal = OTLAttribuut(field=KlTypeMicropaal,
                                           naam='typeMicropaal',
                                           label='type micropaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal.typeMicropaal',
                                           definition='Keuzelijst om het type micropaal te kunnen aangeven.',
                                           owner=self)

        self._uitvoeringsrapport = OTLAttribuut(field=DtcDocument,
                                                naam='uitvoeringsrapport',
                                                label='uitvoeringsrapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal.uitvoeringsrapport',
                                                definition='Rapport van de uitvoering per paal, met vermelding van de paalnummer, de nominale belasting, datum uitvoering boring, het volume van het cementgrout, details van de wapening, van het boorprofiel en van de injecties per fase,...',
                                                owner=self)

        self._volumeCementgrout = OTLAttribuut(field=KwantWrdInKubiekeMeterPerUur,
                                               naam='volumeCementgrout',
                                               label='volume cement grout',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal.volumeCementgrout',
                                               definition='Volume van het cement per uur in kubieke meter.',
                                               owner=self)

    @property
    def typeMicropaal(self) -> str:
        """Keuzelijst om het type micropaal te kunnen aangeven."""
        return self._typeMicropaal.get_waarde()

    @typeMicropaal.setter
    def typeMicropaal(self, value):
        self._typeMicropaal.set_waarde(value, owner=self)

    @property
    def uitvoeringsrapport(self) -> DtcDocumentWaarden:
        """Rapport van de uitvoering per paal, met vermelding van de paalnummer, de nominale belasting, datum uitvoering boring, het volume van het cementgrout, details van de wapening, van het boorprofiel en van de injecties per fase,..."""
        return self._uitvoeringsrapport.get_waarde()

    @uitvoeringsrapport.setter
    def uitvoeringsrapport(self, value):
        self._uitvoeringsrapport.set_waarde(value, owner=self)

    @property
    def volumeCementgrout(self) -> KwantWrdInKubiekeMeterPerUurWaarden:
        """Volume van het cement per uur in kubieke meter."""
        return self._volumeCementgrout.get_waarde()

    @volumeCementgrout.setter
    def volumeCementgrout(self, value):
        self._volumeCementgrout.set_waarde(value, owner=self)
