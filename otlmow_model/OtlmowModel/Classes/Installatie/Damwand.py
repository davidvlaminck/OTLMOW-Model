# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ConstructieElement import ConstructieElement
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.Abstracten.WaterremmendeFunctie import WaterremmendeFunctie
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAansluitingDamwandBestaandeConstructie import KlAansluitingDamwandBestaandeConstructie
from ...Datatypes.KlDamwandMateriaal import KlDamwandMateriaal
from ...Datatypes.KlSlotvullingDamwand import KlSlotvullingDamwand
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Damwand(ConstructieElement, Grondkeringen, WaterremmendeFunctie, LijnGeometrie, VlakGeometrie):
    """Een grond- en/of waterkerende constructie,die bestaat uit een verticaal in de grond geplaatste wand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DamplankAbstracte', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._aansluitingBestaandeConstructie = OTLAttribuut(field=KlAansluitingDamwandBestaandeConstructie,
                                                             naam='aansluitingBestaandeConstructie',
                                                             label='aansluiting bestaande constructie',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.aansluitingBestaandeConstructie',
                                                             kardinaliteit_max='2',
                                                             definition='Hoe de aansluiting van de hele damwand op een bestaande constructie tot stand komt.',
                                                             owner=self)

        self._isWaterdicht = OTLAttribuut(field=BooleanField,
                                          naam='isWaterdicht',
                                          label='is waterdicht',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.isWaterdicht',
                                          definition='Geeft aan of de damwand al dan niet waterdicht is.',
                                          owner=self)

        self._materiaal = OTLAttribuut(field=KlDamwandMateriaal,
                                       naam='materiaal',
                                       label='damwand materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.materiaal',
                                       usagenote='Attribuut uit gebruik sinds versie 2.14.0 ',
                                       deprecated_version='2.14.0',
                                       definition='Het materiaal waaruit de damwand bestaat.',
                                       owner=self)

        self._ontwerpMaaiveldAchterDeKering = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                           naam='ontwerpMaaiveldAchterDeKering',
                                                           label='ontwerp maaiveld achter de kering',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.ontwerpMaaiveldAchterDeKering',
                                                           definition='De overschrijdingsfrequentie van de waterstand die de damwand moet kunnen keren.',
                                                           owner=self)

        self._ontwerpMaaiveldVoorDeKering = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                         naam='ontwerpMaaiveldVoorDeKering',
                                                         label='ontwerp maaiveld voor de kering',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.ontwerpMaaiveldVoorDeKering',
                                                         definition='De overschrijdingsfrequentie van het maaiveld die de damwand moet kunnen keren.',
                                                         owner=self)

        self._ontwerpwaterpeilAchterDeKering = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                            naam='ontwerpwaterpeilAchterDeKering',
                                                            label='ontwerp waterpeil achter de kering',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.ontwerpwaterpeilAchterDeKering',
                                                            definition='De overschrijdingsfrequentie van het waterpeil die de damwand moet kunnen keren.',
                                                            owner=self)

        self._ontwerpwaterpeilVoorDeKering = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                          naam='ontwerpwaterpeilVoorDeKering',
                                                          label='ontwerp waterpeil voor de kering',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.ontwerpwaterpeilVoorDeKering',
                                                          definition='De overschrijdingsfrequentie van het waterpeil die de damwand moet kunnen keren.',
                                                          owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.oppervlakte',
                                         definition='De totale oppervlakte van de damwandconstructie in vierkante meter.',
                                         owner=self)

        self._planzicht = OTLAttribuut(field=DtcDocument,
                                       naam='planzicht',
                                       label='planzicht',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.planzicht',
                                       definition='Het overzicht, in een plan, van de gehele damwand.',
                                       owner=self)

        self._profiellengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='profiellengte',
                                           label='profiellengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.profiellengte',
                                           definition='De lengte van één damwandprofiel.',
                                           owner=self)

        self._slotvulling = OTLAttribuut(field=KlSlotvullingDamwand,
                                         naam='slotvulling',
                                         label='slotvulling',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.slotvulling',
                                         definition='De vulling van het slot van de damwand.',
                                         owner=self)

        self._totaleHorizontaleLengteDamwand = OTLAttribuut(field=KwantWrdInMeter,
                                                            naam='totaleHorizontaleLengteDamwand',
                                                            label='totale horizontale lengte damwand',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.totaleHorizontaleLengteDamwand',
                                                            definition='De totale horizontale lengte van de damwand in lopende meter.',
                                                            owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand.totaleLengte',
                                          definition='De totale lengte van de damwandconstructie in lopende meter.',
                                          owner=self)

    @property
    def aansluitingBestaandeConstructie(self) -> List[str]:
        """Hoe de aansluiting van de hele damwand op een bestaande constructie tot stand komt."""
        return self._aansluitingBestaandeConstructie.get_waarde()

    @aansluitingBestaandeConstructie.setter
    def aansluitingBestaandeConstructie(self, value):
        self._aansluitingBestaandeConstructie.set_waarde(value, owner=self)

    @property
    def isWaterdicht(self) -> bool:
        """Geeft aan of de damwand al dan niet waterdicht is."""
        return self._isWaterdicht.get_waarde()

    @isWaterdicht.setter
    def isWaterdicht(self, value):
        self._isWaterdicht.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de damwand bestaat."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def ontwerpMaaiveldAchterDeKering(self) -> KwantWrdInMeterTAWWaarden:
        """De overschrijdingsfrequentie van de waterstand die de damwand moet kunnen keren."""
        return self._ontwerpMaaiveldAchterDeKering.get_waarde()

    @ontwerpMaaiveldAchterDeKering.setter
    def ontwerpMaaiveldAchterDeKering(self, value):
        self._ontwerpMaaiveldAchterDeKering.set_waarde(value, owner=self)

    @property
    def ontwerpMaaiveldVoorDeKering(self) -> KwantWrdInMeterTAWWaarden:
        """De overschrijdingsfrequentie van het maaiveld die de damwand moet kunnen keren."""
        return self._ontwerpMaaiveldVoorDeKering.get_waarde()

    @ontwerpMaaiveldVoorDeKering.setter
    def ontwerpMaaiveldVoorDeKering(self, value):
        self._ontwerpMaaiveldVoorDeKering.set_waarde(value, owner=self)

    @property
    def ontwerpwaterpeilAchterDeKering(self) -> KwantWrdInMeterTAWWaarden:
        """De overschrijdingsfrequentie van het waterpeil die de damwand moet kunnen keren."""
        return self._ontwerpwaterpeilAchterDeKering.get_waarde()

    @ontwerpwaterpeilAchterDeKering.setter
    def ontwerpwaterpeilAchterDeKering(self, value):
        self._ontwerpwaterpeilAchterDeKering.set_waarde(value, owner=self)

    @property
    def ontwerpwaterpeilVoorDeKering(self) -> KwantWrdInMeterTAWWaarden:
        """De overschrijdingsfrequentie van het waterpeil die de damwand moet kunnen keren."""
        return self._ontwerpwaterpeilVoorDeKering.get_waarde()

    @ontwerpwaterpeilVoorDeKering.setter
    def ontwerpwaterpeilVoorDeKering(self, value):
        self._ontwerpwaterpeilVoorDeKering.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De totale oppervlakte van de damwandconstructie in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def planzicht(self) -> DtcDocumentWaarden:
        """Het overzicht, in een plan, van de gehele damwand."""
        return self._planzicht.get_waarde()

    @planzicht.setter
    def planzicht(self, value):
        self._planzicht.set_waarde(value, owner=self)

    @property
    def profiellengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van één damwandprofiel."""
        return self._profiellengte.get_waarde()

    @profiellengte.setter
    def profiellengte(self, value):
        self._profiellengte.set_waarde(value, owner=self)

    @property
    def slotvulling(self) -> str:
        """De vulling van het slot van de damwand."""
        return self._slotvulling.get_waarde()

    @slotvulling.setter
    def slotvulling(self, value):
        self._slotvulling.set_waarde(value, owner=self)

    @property
    def totaleHorizontaleLengteDamwand(self) -> KwantWrdInMeterWaarden:
        """De totale horizontale lengte van de damwand in lopende meter."""
        return self._totaleHorizontaleLengteDamwand.get_waarde()

    @totaleHorizontaleLengteDamwand.setter
    def totaleHorizontaleLengteDamwand(self, value):
        self._totaleHorizontaleLengteDamwand.set_waarde(value, owner=self)

    @property
    def totaleLengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van de damwandconstructie in lopende meter."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)
