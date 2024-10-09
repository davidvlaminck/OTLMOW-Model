# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LijnvormigElement import LijnvormigElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcGCMateriaalKarakteristiek import DtcGCMateriaalKarakteristiek, DtcGCMateriaalKarakteristiekWaarden
from ...Datatypes.DteKleurRAL import DteKleurRAL, DteKleurRALWaarden
from ...Datatypes.KlLEGCOpstelling import KlLEGCOpstelling
from ...Datatypes.KlLEGCSchermelementType import KlLEGCSchermelementType
from ...Datatypes.KlLEGCSchermtype import KlLEGCSchermtype
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInKiloNewtonPerVierkanteMeter import KwantWrdInKiloNewtonPerVierkanteMeter, KwantWrdInKiloNewtonPerVierkanteMeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GeluidswerendeConstructie(LijnvormigElement, LijnGeometrie):
    """Een geluidswerende wandvormige constructie bestaande uit een desgevallend geluidsisolerend materiaal en/of geluidsabsorberend materiaal en voorzien van de nodige structuren om de bouwkundige stabiliteit te verzekeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorgang', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtopening', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest', direction='i', deprecated='2.0.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie', direction='o', deprecated='2.0.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie', direction='i', deprecated='2.0.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie', direction='o', deprecated='2.0.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', direction='o', deprecated='2.0.0')  # o = direction: outgoing

        self._detailplan3dAsbuilt = OTLAttribuut(field=DtcDocument,
                                                 naam='detailplan3dAsbuilt',
                                                 label='detailplan  (3D - As-built)',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.detailplan3dAsbuilt',
                                                 usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                 deprecated_version='2.0.0',
                                                 definition='Detailplan als document bijlage (3D as-built DWG of DXF bestand).',
                                                 owner=self)

        self._heeftAfdeklatten = OTLAttribuut(field=BooleanField,
                                              naam='heeftAfdeklatten',
                                              label='heeft afdeklatten',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.heeftAfdeklatten',
                                              usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                              deprecated_version='2.0.0',
                                              definition='Bepaling of er boven- of onderaan latten gebruikt worden om de geluidswerende constructie te laten aansluiten op de tunnel.',
                                              owner=self)

        self._horizontaalRuimteBeslag = OTLAttribuut(field=KwantWrdInMeter,
                                                     naam='horizontaalRuimteBeslag',
                                                     label='horizontaal ruimte beslag',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.horizontaalRuimteBeslag',
                                                     usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                     deprecated_version='2.0.0',
                                                     definition='De totale dikte in dwarsdoorsnede die wordt ingenomen door de geluidswerende constructie.',
                                                     owner=self)

        self._individueleHoogteSchermelement = OTLAttribuut(field=KwantWrdInCentimeter,
                                                            naam='individueleHoogteSchermelement',
                                                            label='individuele hoogte schermelement',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.individueleHoogteSchermelement',
                                                            usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                            deprecated_version='2.0.0',
                                                            definition='De hoogte in centimeter van het schermelement, verticaal gemeten.',
                                                            owner=self)

        self._individueleLengteSchermelement = OTLAttribuut(field=KwantWrdInCentimeter,
                                                            naam='individueleLengteSchermelement',
                                                            label='individuele lengte schermelement',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.individueleLengteSchermelement',
                                                            usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                            deprecated_version='2.0.0',
                                                            definition='De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten.',
                                                            owner=self)

        self._isBeginOfEindConstructie = OTLAttribuut(field=BooleanField,
                                                      naam='isBeginOfEindConstructie',
                                                      label='is begin of eindconstructie',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.isBeginOfEindConstructie',
                                                      usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                      deprecated_version='2.0.0',
                                                      definition='Bepaling of het gaat om een begin- of eindconstructie.',
                                                      owner=self)

        self._kleur = OTLAttribuut(field=DteKleurRAL,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.kleur',
                                   usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                   deprecated_version='2.0.0',
                                   definition='De RAL kleur van de geluidswerende constructie.',
                                   owner=self)

        self._materiaalKarakteristiek = OTLAttribuut(field=DtcGCMateriaalKarakteristiek,
                                                     naam='materiaalKarakteristiek',
                                                     label='materiaal karakteristiek',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.materiaalKarakteristiek',
                                                     usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                     deprecated_version='2.0.0',
                                                     kardinaliteit_max='*',
                                                     definition='Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal.',
                                                     owner=self)

        self._maximaleDikteSchermelement = OTLAttribuut(field=KwantWrdInCentimeter,
                                                        naam='maximaleDikteSchermelement',
                                                        label='maximale dikte schermelement',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.maximaleDikteSchermelement',
                                                        usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                        deprecated_version='2.0.0',
                                                        definition='De maximale dikte van het schermelement in centimeter gemeten vanaf het verst uitstekende gedeelte aan de voorzijde tot het verst uitstekende gedeelte aan de achterzijde van het schermelement.',
                                                        owner=self)

        self._opstelling = OTLAttribuut(field=KlLEGCOpstelling,
                                        naam='opstelling',
                                        label='opstelling',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.opstelling',
                                        usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                        deprecated_version='2.0.0',
                                        definition='De wijze waarop de geluidswerende constructie is geplaatst ten opzichte van de weg.',
                                        owner=self)

        self._overzichtSchermhoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                                   naam='overzichtSchermhoogte',
                                                   label='overzicht schermhoogte',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.overzichtSchermhoogte',
                                                   usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                   deprecated_version='2.0.0',
                                                   definition='Hoogte gemeten van het maaiveld tot aan de top van de geluidswerende constructie.',
                                                   owner=self)

        self._schermelement = OTLAttribuut(field=KlLEGCSchermelementType,
                                           naam='schermelement',
                                           label='schermelement',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.schermelement',
                                           usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                           deprecated_version='2.0.0',
                                           kardinaliteit_max='*',
                                           definition='Het type van schermelement.',
                                           owner=self)

        self._schermtype = OTLAttribuut(field=KlLEGCSchermtype,
                                        naam='schermtype',
                                        label='schermtype',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.schermtype',
                                        usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                        deprecated_version='2.0.0',
                                        kardinaliteit_max='*',
                                        definition='Bepaling van een vlak of niet-vlak scherm. Een vlak scherm zijn alle schermtypes die getest kunnen worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.De niet-vlakke schermen zijn de schermen die niet kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.',
                                        owner=self)

        self._statischeBelasting = OTLAttribuut(field=KwantWrdInKiloNewtonPerVierkanteMeter,
                                                naam='statischeBelasting',
                                                label='statische belasting',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.statischeBelasting',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                deprecated_version='2.0.0',
                                                definition='Getal in kN/m2 voor de aanduiding van de belasting zonder dynamisch effect, bv. eigengewicht.',
                                                owner=self)

        self._testrapport = OTLAttribuut(field=DtcDocument,
                                         naam='testrapport',
                                         label='testrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.testrapport',
                                         usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                         deprecated_version='2.0.0',
                                         kardinaliteit_max='*',
                                         definition='De testresultaten van een geluidswerende constructie.',
                                         owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.totaleLengte',
                                          usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                          deprecated_version='2.0.0',
                                          definition='De totale lengte van de geluidswerende constructie in meter gemeten vanaf het beginpunt tot het eindpunt.',
                                          owner=self)

        self._totaleOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                               naam='totaleOppervlakte',
                                               label='totale oppervlakte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.totaleOppervlakte',
                                               usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                               deprecated_version='2.0.0',
                                               definition='De totale oppervlakte van alle geplaatste geluidswerende constructie elementen.',
                                               owner=self)

        self._videoVoertuigkering = OTLAttribuut(field=DtcDocument,
                                                 naam='videoVoertuigkering',
                                                 label='video voertuigkering',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.videoVoertuigkering',
                                                 usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                 deprecated_version='2.0.0',
                                                 kardinaliteit_max='*',
                                                 definition='Video van de testen op geluidswerende constructies.',
                                                 owner=self)

        self._windbelasting = OTLAttribuut(field=KwantWrdInKiloNewtonPerVierkanteMeter,
                                           naam='windbelasting',
                                           label='windbelasting',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie.windbelasting',
                                           usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                           deprecated_version='2.0.0',
                                           definition='Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4.',
                                           owner=self)

    @property
    def detailplan3dAsbuilt(self) -> DtcDocumentWaarden:
        """Detailplan als document bijlage (3D as-built DWG of DXF bestand)."""
        return self._detailplan3dAsbuilt.get_waarde()

    @detailplan3dAsbuilt.setter
    def detailplan3dAsbuilt(self, value):
        self._detailplan3dAsbuilt.set_waarde(value, owner=self)

    @property
    def heeftAfdeklatten(self) -> bool:
        """Bepaling of er boven- of onderaan latten gebruikt worden om de geluidswerende constructie te laten aansluiten op de tunnel."""
        return self._heeftAfdeklatten.get_waarde()

    @heeftAfdeklatten.setter
    def heeftAfdeklatten(self, value):
        self._heeftAfdeklatten.set_waarde(value, owner=self)

    @property
    def horizontaalRuimteBeslag(self) -> KwantWrdInMeterWaarden:
        """De totale dikte in dwarsdoorsnede die wordt ingenomen door de geluidswerende constructie."""
        return self._horizontaalRuimteBeslag.get_waarde()

    @horizontaalRuimteBeslag.setter
    def horizontaalRuimteBeslag(self, value):
        self._horizontaalRuimteBeslag.set_waarde(value, owner=self)

    @property
    def individueleHoogteSchermelement(self) -> KwantWrdInCentimeterWaarden:
        """De hoogte in centimeter van het schermelement, verticaal gemeten."""
        return self._individueleHoogteSchermelement.get_waarde()

    @individueleHoogteSchermelement.setter
    def individueleHoogteSchermelement(self, value):
        self._individueleHoogteSchermelement.set_waarde(value, owner=self)

    @property
    def individueleLengteSchermelement(self) -> KwantWrdInCentimeterWaarden:
        """De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten."""
        return self._individueleLengteSchermelement.get_waarde()

    @individueleLengteSchermelement.setter
    def individueleLengteSchermelement(self, value):
        self._individueleLengteSchermelement.set_waarde(value, owner=self)

    @property
    def isBeginOfEindConstructie(self) -> bool:
        """Bepaling of het gaat om een begin- of eindconstructie."""
        return self._isBeginOfEindConstructie.get_waarde()

    @isBeginOfEindConstructie.setter
    def isBeginOfEindConstructie(self, value):
        self._isBeginOfEindConstructie.set_waarde(value, owner=self)

    @property
    def kleur(self) -> DteKleurRALWaarden:
        """De RAL kleur van de geluidswerende constructie."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def materiaalKarakteristiek(self) -> List[DtcGCMateriaalKarakteristiekWaarden]:
        """Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal."""
        return self._materiaalKarakteristiek.get_waarde()

    @materiaalKarakteristiek.setter
    def materiaalKarakteristiek(self, value):
        self._materiaalKarakteristiek.set_waarde(value, owner=self)

    @property
    def maximaleDikteSchermelement(self) -> KwantWrdInCentimeterWaarden:
        """De maximale dikte van het schermelement in centimeter gemeten vanaf het verst uitstekende gedeelte aan de voorzijde tot het verst uitstekende gedeelte aan de achterzijde van het schermelement."""
        return self._maximaleDikteSchermelement.get_waarde()

    @maximaleDikteSchermelement.setter
    def maximaleDikteSchermelement(self, value):
        self._maximaleDikteSchermelement.set_waarde(value, owner=self)

    @property
    def opstelling(self) -> str:
        """De wijze waarop de geluidswerende constructie is geplaatst ten opzichte van de weg."""
        return self._opstelling.get_waarde()

    @opstelling.setter
    def opstelling(self, value):
        self._opstelling.set_waarde(value, owner=self)

    @property
    def overzichtSchermhoogte(self) -> KwantWrdInCentimeterWaarden:
        """Hoogte gemeten van het maaiveld tot aan de top van de geluidswerende constructie."""
        return self._overzichtSchermhoogte.get_waarde()

    @overzichtSchermhoogte.setter
    def overzichtSchermhoogte(self, value):
        self._overzichtSchermhoogte.set_waarde(value, owner=self)

    @property
    def schermelement(self) -> List[str]:
        """Het type van schermelement."""
        return self._schermelement.get_waarde()

    @schermelement.setter
    def schermelement(self, value):
        self._schermelement.set_waarde(value, owner=self)

    @property
    def schermtype(self) -> List[str]:
        """Bepaling van een vlak of niet-vlak scherm. Een vlak scherm zijn alle schermtypes die getest kunnen worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.
De niet-vlakke schermen zijn de schermen die niet kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2."""
        return self._schermtype.get_waarde()

    @schermtype.setter
    def schermtype(self, value):
        self._schermtype.set_waarde(value, owner=self)

    @property
    def statischeBelasting(self) -> KwantWrdInKiloNewtonPerVierkanteMeterWaarden:
        """Getal in kN/m2 voor de aanduiding van de belasting zonder dynamisch effect, bv. eigengewicht."""
        return self._statischeBelasting.get_waarde()

    @statischeBelasting.setter
    def statischeBelasting(self, value):
        self._statischeBelasting.set_waarde(value, owner=self)

    @property
    def testrapport(self) -> List[DtcDocumentWaarden]:
        """De testresultaten van een geluidswerende constructie."""
        return self._testrapport.get_waarde()

    @testrapport.setter
    def testrapport(self, value):
        self._testrapport.set_waarde(value, owner=self)

    @property
    def totaleLengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van de geluidswerende constructie in meter gemeten vanaf het beginpunt tot het eindpunt."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

    @property
    def totaleOppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De totale oppervlakte van alle geplaatste geluidswerende constructie elementen."""
        return self._totaleOppervlakte.get_waarde()

    @totaleOppervlakte.setter
    def totaleOppervlakte(self, value):
        self._totaleOppervlakte.set_waarde(value, owner=self)

    @property
    def videoVoertuigkering(self) -> List[DtcDocumentWaarden]:
        """Video van de testen op geluidswerende constructies."""
        return self._videoVoertuigkering.get_waarde()

    @videoVoertuigkering.setter
    def videoVoertuigkering(self, value):
        self._videoVoertuigkering.set_waarde(value, owner=self)

    @property
    def windbelasting(self) -> KwantWrdInKiloNewtonPerVierkanteMeterWaarden:
        """Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4."""
        return self._windbelasting.get_waarde()

    @windbelasting.setter
    def windbelasting(self, value):
        self._windbelasting.set_waarde(value, owner=self)
