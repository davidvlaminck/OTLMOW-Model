# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.VRIDraagconstructie import VRIDraagconstructie
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.Datatypes.KlSeinbrugRijrichting import KlSeinbrugRijrichting
from otlmow_model.Datatypes.KlSeinbrugType import KlSeinbrugType
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Seinbrug(VRIDraagconstructie, LijnGeometrie, VlakGeometrie):
    """Metalen constructie bestaande uit twee of meer verticale steunen met voetplaat en uit een enkele of een dubbel uitgevoerde horizontale dwarsverbinding, allen kokervormig met rechthoekige doorsnede. Ook wel portiek of portaal genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VRIDraagconstructie.__init__(self)
        LijnGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug')

        self._aantalLadders = OTLAttribuut(field=FloatOrDecimalField,
                                           naam='aantalLadders',
                                           label='aantal ladders',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.aantalLadders',
                                           definition='Het aantal ladders waarmee de seinbrug toegankelijk is.',
                                           owner=self)

        self._aantalSteunen = OTLAttribuut(field=FloatOrDecimalField,
                                           naam='aantalSteunen',
                                           label='aantal steunen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.aantalSteunen',
                                           definition='Het aantal steunen waarmee de seinbrug gedragen wordt. ',
                                           owner=self)

        self._berekeningsnota = OTLAttribuut(field=DtcDocument,
                                             naam='berekeningsnota',
                                             label='berekeningsnota',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.berekeningsnota',
                                             definition='Een bijlage met de berekeningsnota voor de seinbrug.',
                                             owner=self)

        self._controlemetingEBS = OTLAttribuut(field=DtcDocument,
                                               naam='controlemetingEBS',
                                               label='controlemeting EBS',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.controlemetingEBS',
                                               definition='Een bijlage met het verslag van de controlemeting uitgevoerd door het Expertisecentrum Beton en Staal.',
                                               owner=self)

        self._heeftLooproosters = OTLAttribuut(field=BooleanField,
                                               naam='heeftLooproosters',
                                               label='heeft looproosters',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.heeftLooproosters',
                                               definition='Geeft aan of de seinbrug is uitgerust met looproosters.',
                                               owner=self)

        self._hoogteVerticaleSteun = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='hoogteVerticaleSteun',
                                                  label='hoogte verticale steun',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.hoogteVerticaleSteun',
                                                  definition='Verticale afstand (in meter) tussen de bovenkant van het wegdek en de bovenkant van het hoogste constructiedeel van de seinbrug.',
                                                  owner=self)

        self._overspanning = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='overspanning',
                                          label='overspanning',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.overspanning',
                                          definition='De afstand tussen de twee steunpunten van de seinbrug.',
                                          owner=self)

        self._rijrichting = OTLAttribuut(field=KlSeinbrugRijrichting,
                                         naam='rijrichting',
                                         label='rijrichting',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.rijrichting',
                                         definition='Geeft aan of de seinbrug één of beide rijrichtingen overspant.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.technischeFiche',
                                             definition='Een bijlage waarin de detailtekeningen van de seinbrug.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlSeinbrugType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.type',
                                  definition='Het type van de seinbrug volgens de aard van de constructie.',
                                  owner=self)

        self._vrijeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='vrijeHoogte',
                                         label='vrije hoogte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.vrijeHoogte',
                                         definition='De verticale afstand (in meter) tussen de bovenkant van het wegdek en de onderkant van het laagste, daarboven gelegen constructiedeel van de seinbrug.',
                                         owner=self)

    @property
    def aantalLadders(self) -> float:
        """Het aantal ladders waarmee de seinbrug toegankelijk is."""
        return self._aantalLadders.get_waarde()

    @aantalLadders.setter
    def aantalLadders(self, value):
        self._aantalLadders.set_waarde(value, owner=self)

    @property
    def aantalSteunen(self) -> float:
        """Het aantal steunen waarmee de seinbrug gedragen wordt. """
        return self._aantalSteunen.get_waarde()

    @aantalSteunen.setter
    def aantalSteunen(self, value):
        self._aantalSteunen.set_waarde(value, owner=self)

    @property
    def berekeningsnota(self) -> DtcDocumentWaarden:
        """Een bijlage met de berekeningsnota voor de seinbrug."""
        return self._berekeningsnota.get_waarde()

    @berekeningsnota.setter
    def berekeningsnota(self, value):
        self._berekeningsnota.set_waarde(value, owner=self)

    @property
    def controlemetingEBS(self) -> DtcDocumentWaarden:
        """Een bijlage met het verslag van de controlemeting uitgevoerd door het Expertisecentrum Beton en Staal."""
        return self._controlemetingEBS.get_waarde()

    @controlemetingEBS.setter
    def controlemetingEBS(self, value):
        self._controlemetingEBS.set_waarde(value, owner=self)

    @property
    def heeftLooproosters(self) -> bool:
        """Geeft aan of de seinbrug is uitgerust met looproosters."""
        return self._heeftLooproosters.get_waarde()

    @heeftLooproosters.setter
    def heeftLooproosters(self, value):
        self._heeftLooproosters.set_waarde(value, owner=self)

    @property
    def hoogteVerticaleSteun(self) -> KwantWrdInMeterWaarden:
        """Verticale afstand (in meter) tussen de bovenkant van het wegdek en de bovenkant van het hoogste constructiedeel van de seinbrug."""
        return self._hoogteVerticaleSteun.get_waarde()

    @hoogteVerticaleSteun.setter
    def hoogteVerticaleSteun(self, value):
        self._hoogteVerticaleSteun.set_waarde(value, owner=self)

    @property
    def overspanning(self) -> KwantWrdInMeterWaarden:
        """De afstand tussen de twee steunpunten van de seinbrug."""
        return self._overspanning.get_waarde()

    @overspanning.setter
    def overspanning(self, value):
        self._overspanning.set_waarde(value, owner=self)

    @property
    def rijrichting(self) -> str:
        """Geeft aan of de seinbrug één of beide rijrichtingen overspant."""
        return self._rijrichting.get_waarde()

    @rijrichting.setter
    def rijrichting(self, value):
        self._rijrichting.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Een bijlage waarin de detailtekeningen van de seinbrug."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van de seinbrug volgens de aard van de constructie."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vrijeHoogte(self) -> KwantWrdInMeterWaarden:
        """De verticale afstand (in meter) tussen de bovenkant van het wegdek en de onderkant van het laagste, daarboven gelegen constructiedeel van de seinbrug."""
        return self._vrijeHoogte.get_waarde()

    @vrijeHoogte.setter
    def vrijeHoogte(self, value):
        self._vrijeHoogte.set_waarde(value, owner=self)
