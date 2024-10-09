# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GeluidwerendeConstructie(AIMNaamObject, LijnGeometrie):
    """Een geluidswerende wandvormige constructie bestaande uit een desgevallend geluidsisolerend materiaal en/of geluidsabsorberend materiaal en voorzien van de nodige structuren om de bouwkundige stabiliteit te verzekeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementenGC', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorgang', direction='i', deprecated='2.1.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtdeur', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtopening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest', direction='i')  # i = direction: incoming

        self._detailplanHoogteverloop = OTLAttribuut(field=DtcDocument,
                                                     naam='detailplanHoogteverloop',
                                                     label='detailplan hoogteverloop',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.detailplanHoogteverloop',
                                                     usagenote='Bestanden moeten van het type DWG of DXF zijn.',
                                                     definition='Dit is een detailplan in de vorm van een lijn waarin het verloop van de absolute hoogte van de top van de geluidswerende constructie wordt weergegeven. Minstens om de 10 meter wordt de hoogte van de top van de constructie bepaald. Het detailplan wordt gebruikt voor akoestische modellering.',
                                                     owner=self)

        self._horizontaalRuimtebeslag = OTLAttribuut(field=DtcDocument,
                                                     naam='horizontaalRuimtebeslag',
                                                     label='horizontaal ruimtebeslag',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.horizontaalRuimtebeslag',
                                                     definition='Document waarin de variatie in horizontaal ruimtebeslag over het verloop van de geluidswerende constructie is weergegeven. Het horizontaal ruimtebeslag is de breedte die de gehele constructie inneemt op het maaiveld, loodrecht op de richting waarin de schermelementen op elkaar aangesloten zijn. Er moet een nieuwe waarde ingegeven worden elke keer als de hoogte van de constructie wijzigt.',
                                                     owner=self)

        self._overzichtsafbeelding = OTLAttribuut(field=DtcDocument,
                                                  naam='overzichtsafbeelding',
                                                  label='overzichtsafbeelding',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.overzichtsafbeelding',
                                                  kardinaliteit_max='*',
                                                  definition='Dit een overzichtsfoto van de hele constructie. Op basis van deze afbeelding kan je snel bekijken hoe de kleur of hoogte varieert over het verloop van de geluidswerende constructie.',
                                                  owner=self)

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekennota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.rekennota',
                                       kardinaliteit_max='*',
                                       definition='Dit is een document waarin allerlei berekeningen bijgehouden worden omtrent de stabiliteit en sterkte van de geluidswerende constructie (oa de variatie in statische belasting en windbelasting over het verloop van geluidswerende constructie).',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='Dit document geeft volgende zaken mee: producent, productnaam (type), beschrijving van de geplaatste constructie, certificatie (CE en ISO), montage, akoestische karakteristieken, duurzaamheid en brandwerende kenmerken.',
                                             owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.totaleLengte',
                                          definition='De afstand in meter gemeten tussen het beginpunt en het eindpunt van de geluidswerende constructie.',
                                          owner=self)

        self._totaleOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                               naam='totaleOppervlakte',
                                               label='totale oppervlakte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.totaleOppervlakte',
                                               definition='De totale oppervlakte van het naar de weg gerichte vlak van alle geplaatste schermelementen van de geluidswerende constructie.',
                                               owner=self)

    @property
    def detailplanHoogteverloop(self) -> DtcDocumentWaarden:
        """Dit is een detailplan in de vorm van een lijn waarin het verloop van de absolute hoogte van de top van de geluidswerende constructie wordt weergegeven. Minstens om de 10 meter wordt de hoogte van de top van de constructie bepaald. Het detailplan wordt gebruikt voor akoestische modellering."""
        return self._detailplanHoogteverloop.get_waarde()

    @detailplanHoogteverloop.setter
    def detailplanHoogteverloop(self, value):
        self._detailplanHoogteverloop.set_waarde(value, owner=self)

    @property
    def horizontaalRuimtebeslag(self) -> DtcDocumentWaarden:
        """Document waarin de variatie in horizontaal ruimtebeslag over het verloop van de geluidswerende constructie is weergegeven. Het horizontaal ruimtebeslag is de breedte die de gehele constructie inneemt op het maaiveld, loodrecht op de richting waarin de schermelementen op elkaar aangesloten zijn. Er moet een nieuwe waarde ingegeven worden elke keer als de hoogte van de constructie wijzigt."""
        return self._horizontaalRuimtebeslag.get_waarde()

    @horizontaalRuimtebeslag.setter
    def horizontaalRuimtebeslag(self, value):
        self._horizontaalRuimtebeslag.set_waarde(value, owner=self)

    @property
    def overzichtsafbeelding(self) -> List[DtcDocumentWaarden]:
        """Dit een overzichtsfoto van de hele constructie. Op basis van deze afbeelding kan je snel bekijken hoe de kleur of hoogte varieert over het verloop van de geluidswerende constructie."""
        return self._overzichtsafbeelding.get_waarde()

    @overzichtsafbeelding.setter
    def overzichtsafbeelding(self, value):
        self._overzichtsafbeelding.set_waarde(value, owner=self)

    @property
    def rekennota(self) -> List[DtcDocumentWaarden]:
        """Dit is een document waarin allerlei berekeningen bijgehouden worden omtrent de stabiliteit en sterkte van de geluidswerende constructie (oa de variatie in statische belasting en windbelasting over het verloop van geluidswerende constructie)."""
        return self._rekennota.get_waarde()

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """Dit document geeft volgende zaken mee: producent, productnaam (type), beschrijving van de geplaatste constructie, certificatie (CE en ISO), montage, akoestische karakteristieken, duurzaamheid en brandwerende kenmerken."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def totaleLengte(self) -> KwantWrdInMeterWaarden:
        """De afstand in meter gemeten tussen het beginpunt en het eindpunt van de geluidswerende constructie."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

    @property
    def totaleOppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De totale oppervlakte van het naar de weg gerichte vlak van alle geplaatste schermelementen van de geluidswerende constructie."""
        return self._totaleOppervlakte.get_waarde()

    @totaleOppervlakte.setter
    def totaleOppervlakte(self, value):
        self._totaleOppervlakte.set_waarde(value, owner=self)
