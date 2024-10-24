# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.PutRelatie import PutRelatie
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlKamerKlasse import KlKamerKlasse
from ...Datatypes.KlPutMateriaal import KlPutMateriaal
from ...Datatypes.KlRioleringVorm import KlRioleringVorm
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kamer(PutRelatie, VlakGeometrie):
    """Een kamer is een aanééngesloten ondergrondse constructie waarbinnen vrije stroming van water over de bodem mogelijk is. Een constructie of inspectieput kan één of meerdere kamers hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw', direction='u', deprecated='2.1.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.breedte',
                                     definition='De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter.',
                                     owner=self)

        self._diepte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.diepte',
                                    definition='De diepte van de putkamer in meter.',
                                    owner=self)

        self._heeftOlieAfscheidendeKamer = OTLAttribuut(field=BooleanField,
                                                        naam='heeftOlieAfscheidendeKamer',
                                                        label='heeft olieafscheidende kamer',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.heeftOlieAfscheidendeKamer',
                                                        definition='Geeft aan of er een olie afscheidende kamer aanwezig is',
                                                        owner=self)

        self._heeftZandvang = OTLAttribuut(field=BooleanField,
                                           naam='heeftZandvang',
                                           label='heeft zandvang',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.heeftZandvang',
                                           definition='Geeft aan of er een zandvang aanwezig is',
                                           owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.hoogte',
                                    definition='De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter.',
                                    owner=self)

        self._klasse = OTLAttribuut(field=KlKamerKlasse,
                                    naam='klasse',
                                    label='klasse',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.klasse',
                                    definition='De stabiliteitsklasse van de kamer.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlPutMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.materiaal',
                                       definition='Het materiaal waaruit de kamer opgebouwd is.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.technischeFiche',
                                             usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de kamer.',
                                             owner=self)

        self._vorm = OTLAttribuut(field=KlRioleringVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.vorm',
                                  definition='De vorm van de kamer.',
                                  owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diepte(self) -> KwantWrdInMeterWaarden:
        """De diepte van de putkamer in meter."""
        return self._diepte.get_waarde()

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def heeftOlieAfscheidendeKamer(self) -> bool:
        """Geeft aan of er een olie afscheidende kamer aanwezig is"""
        return self._heeftOlieAfscheidendeKamer.get_waarde()

    @heeftOlieAfscheidendeKamer.setter
    def heeftOlieAfscheidendeKamer(self, value):
        self._heeftOlieAfscheidendeKamer.set_waarde(value, owner=self)

    @property
    def heeftZandvang(self) -> bool:
        """Geeft aan of er een zandvang aanwezig is"""
        return self._heeftZandvang.get_waarde()

    @heeftZandvang.setter
    def heeftZandvang(self, value):
        self._heeftZandvang.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInMillimeterWaarden:
        """De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def klasse(self) -> str:
        """De stabiliteitsklasse van de kamer."""
        return self._klasse.get_waarde()

    @klasse.setter
    def klasse(self, value):
        self._klasse.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de kamer opgebouwd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """De technische fiche van de kamer."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """De vorm van de kamer."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
