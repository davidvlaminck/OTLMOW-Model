# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ConstructiefObject import ConstructiefObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ...Datatypes.KlMateriaalBWCTWC import KlMateriaalBWCTWC
from ...Datatypes.KlPlaatsingsmethodeTWC import KlPlaatsingsmethodeTWC
from ...Datatypes.KlTypeTWC import KlTypeTWC
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class TijdelijkeWaterkerendeConstructie(ConstructiefObject, VlakGeometrie):
    """Constructie, al dan niet opgebouwd uit meerdere op elkaar stapelbare elementen, voor het droogzetten van een (onderdeel van een) sluis of stuw."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
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
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanslagbalk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DraagstructuurBWCTWC', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuw', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenConstructieObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenConstructieObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._aantalElementen = OTLAttribuut(field=IntegerField,
                                             naam='aantalElementen',
                                             label='aantal elementen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.aantalElementen',
                                             definition='Het aantal elementen waaruit de tijdelijke waterkerende constructie bestaat',
                                             owner=self)

        self._bestaatUitVarierendeElementen = OTLAttribuut(field=BooleanField,
                                                           naam='bestaatUitVarierendeElementen',
                                                           label='bestaat uit varierende elementen',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.bestaatUitVarierendeElementen',
                                                           definition='Geeft aan of de tijdelijke waterkerende constructie al dan niet uit variërende elementen bestaat.',
                                                           owner=self)

        self._gewichtZwaarsteElement = OTLAttribuut(field=KwantWrdInTon,
                                                    naam='gewichtZwaarsteElement',
                                                    label='gewicht zwaarste element',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.gewichtZwaarsteElement',
                                                    definition='Het gewicht van het zwaarste element van de tijdelijke waterkerende constructie, uitgedrukt in ton.',
                                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlMateriaalBWCTWC,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.materiaal',
                                       definition='Geeft de verschillende mogelijkheden aan om te weten vanuit welk materiaal de tijdelijke waterkerende constructie is uitgevoerd.',
                                       owner=self)

        self._maximaalTeKerenWaterpeilverschil = OTLAttribuut(field=KwantWrdInMeter,
                                                              naam='maximaalTeKerenWaterpeilverschil',
                                                              label='maximaal te keren waterpeilverschil',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.maximaalTeKerenWaterpeilverschil',
                                                              definition='Het maximaal te keren waterpeil verschil uitgedrukt in meter.',
                                                              owner=self)

        self._oplegbreedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='oplegbreedte',
                                          label='oplegbreedte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.oplegbreedte',
                                          definition='Breedte van de oplegtand t.o.v. de sponning, uitgedrukt in centimeter.',
                                          owner=self)

        self._overspanning = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='overspanning',
                                          label='overspanning',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.overspanning',
                                          definition='De overspanning van de tijdelijke waterkerende constructie uitgedrukt in meter.',
                                          owner=self)

        self._plaatsingsmethode = OTLAttribuut(field=KlPlaatsingsmethodeTWC,
                                               naam='plaatsingsmethode',
                                               label='plaatsingsmethode',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.plaatsingsmethode',
                                               definition='De methode waarmee de tijdelijke waterkerende constructie geplaatst wordt.',
                                               owner=self)

        self._type = OTLAttribuut(field=KlTypeTWC,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie.type',
                                  definition='Het type tijdelijke waterkerende constructie.',
                                  owner=self)

    @property
    def aantalElementen(self) -> int:
        """Het aantal elementen waaruit de tijdelijke waterkerende constructie bestaat"""
        return self._aantalElementen.get_waarde()

    @aantalElementen.setter
    def aantalElementen(self, value):
        self._aantalElementen.set_waarde(value, owner=self)

    @property
    def bestaatUitVarierendeElementen(self) -> bool:
        """Geeft aan of de tijdelijke waterkerende constructie al dan niet uit variërende elementen bestaat."""
        return self._bestaatUitVarierendeElementen.get_waarde()

    @bestaatUitVarierendeElementen.setter
    def bestaatUitVarierendeElementen(self, value):
        self._bestaatUitVarierendeElementen.set_waarde(value, owner=self)

    @property
    def gewichtZwaarsteElement(self) -> KwantWrdInTonWaarden:
        """Het gewicht van het zwaarste element van de tijdelijke waterkerende constructie, uitgedrukt in ton."""
        return self._gewichtZwaarsteElement.get_waarde()

    @gewichtZwaarsteElement.setter
    def gewichtZwaarsteElement(self, value):
        self._gewichtZwaarsteElement.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Geeft de verschillende mogelijkheden aan om te weten vanuit welk materiaal de tijdelijke waterkerende constructie is uitgevoerd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def maximaalTeKerenWaterpeilverschil(self) -> KwantWrdInMeterWaarden:
        """Het maximaal te keren waterpeil verschil uitgedrukt in meter."""
        return self._maximaalTeKerenWaterpeilverschil.get_waarde()

    @maximaalTeKerenWaterpeilverschil.setter
    def maximaalTeKerenWaterpeilverschil(self, value):
        self._maximaalTeKerenWaterpeilverschil.set_waarde(value, owner=self)

    @property
    def oplegbreedte(self) -> KwantWrdInCentimeterWaarden:
        """Breedte van de oplegtand t.o.v. de sponning, uitgedrukt in centimeter."""
        return self._oplegbreedte.get_waarde()

    @oplegbreedte.setter
    def oplegbreedte(self, value):
        self._oplegbreedte.set_waarde(value, owner=self)

    @property
    def overspanning(self) -> KwantWrdInMeterWaarden:
        """De overspanning van de tijdelijke waterkerende constructie uitgedrukt in meter."""
        return self._overspanning.get_waarde()

    @overspanning.setter
    def overspanning(self, value):
        self._overspanning.set_waarde(value, owner=self)

    @property
    def plaatsingsmethode(self) -> str:
        """De methode waarmee de tijdelijke waterkerende constructie geplaatst wordt."""
        return self._plaatsingsmethode.get_waarde()

    @plaatsingsmethode.setter
    def plaatsingsmethode(self, value):
        self._plaatsingsmethode.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type tijdelijke waterkerende constructie."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
