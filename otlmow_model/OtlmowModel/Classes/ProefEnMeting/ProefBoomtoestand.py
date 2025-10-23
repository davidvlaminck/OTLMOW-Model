# coding=utf-8
from datetime import datetime
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from otlmow_model.OtlmowModel.BaseClasses.DateTimeField import DateTimeField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ...Datatypes.KlBoomConditiebeoordeling import KlBoomConditiebeoordeling
from ...Datatypes.KlBoomConditiewaarde import KlBoomConditiewaarde
from ...Datatypes.KlBoomConflicten import KlBoomConflicten
from ...Datatypes.KlBoomGebreken import KlBoomGebreken
from ...Datatypes.KlBoomOnderhoudstoestand import KlBoomOnderhoudstoestand
from ...Datatypes.KlBoomPlantwijzewaarde import KlBoomPlantwijzewaarde
from ...Datatypes.KlBoomStandplaatswaarde import KlBoomStandplaatswaarde
from ...Datatypes.KlBoomtoestandMeerwaardefactor import KlBoomtoestandMeerwaardefactor
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInEuro import KwantWrdInEuro, KwantWrdInEuroWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefBoomtoestand(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De toestand met waarnemingen per inspectie van een boom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.12.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom', direction='o', deprecated='2.12.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom', direction='o', deprecated='2.0.0')  # o = direction: outgoing

        self._basiswaarde = OTLAttribuut(field=KwantWrdInEuro,
                                         naam='basiswaarde',
                                         label='basiswaarde',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.basiswaarde',
                                         usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                         deprecated_version='2.12.0',
                                         definition='Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt.',
                                         owner=self)

        self._conditiebeoordeling = OTLAttribuut(field=KlBoomConditiebeoordeling,
                                                 naam='conditiebeoordeling',
                                                 label='conditiebeoordeling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conditiebeoordeling',
                                                 usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                                 deprecated_version='2.12.0',
                                                 definition='De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout.',
                                                 owner=self)

        self._conditiewaarde = OTLAttribuut(field=KlBoomConditiewaarde,
                                            naam='conditiewaarde',
                                            label='conditiewaarde',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conditiewaarde',
                                            usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                            deprecated_version='2.12.0',
                                            definition='Een coëfficiënt die iets vertelt over de gezondheidstoestand (vitaliteit, conditie) en de levensverwachting van een boom.',
                                            owner=self)

        self._conflicten = OTLAttribuut(field=KlBoomConflicten,
                                        naam='conflicten',
                                        label='conflicten',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conflicten',
                                        usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                        deprecated_version='2.12.0',
                                        definition='Mogelijke standplaatsconflicten die de condities of structuur van de boom negatief kunnen beïnvloeden.',
                                        owner=self)

        self._gebreken = OTLAttribuut(field=KlBoomGebreken,
                                      naam='gebreken',
                                      label='gebreken',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.gebreken',
                                      usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                      deprecated_version='2.12.0',
                                      kardinaliteit_max='*',
                                      definition='Een visueel defect aan een boom wat dient gemonitord te worden.',
                                      owner=self)

        self._kroonDiameter = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='kroonDiameter',
                                           label='kroondiameter',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.kroonDiameter',
                                           usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                           deprecated_version='2.12.0',
                                           definition='Diameter van de kroonprojectie in meter.',
                                           owner=self)

        self._krooninspectie = OTLAttribuut(field=DtcDocument,
                                            naam='krooninspectie',
                                            label='krooninspectie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.krooninspectie',
                                            usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                            deprecated_version='2.12.0',
                                            definition='Controle van gebrekssymptomen in de kroon.',
                                            owner=self)

        self._meerwaarde = OTLAttribuut(field=KlBoomtoestandMeerwaardefactor,
                                        naam='meerwaarde',
                                        label='meerwaarde',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.meerwaarde',
                                        usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                        deprecated_version='2.12.0',
                                        definition='Mogelijkheid om de boom een waarde toe te kennen op basis van hun uitzonderlijke ecologische of erfgoedwaarde .',
                                        owner=self)

        self._onderhoudstoestand = OTLAttribuut(field=KlBoomOnderhoudstoestand,
                                                naam='onderhoudstoestand',
                                                label='onderhoudstoestand',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.onderhoudstoestand',
                                                usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                                deprecated_version='2.12.0',
                                                definition='De toestand van een boom die de eventuele snoeiachterstand aangeeft.',
                                                owner=self)

        self._onderzoekVisueleBoomcontrole = OTLAttribuut(field=DtcDocument,
                                                          naam='onderzoekVisueleBoomcontrole',
                                                          label='onderzoek visuele boomcontrole',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.onderzoekVisueleBoomcontrole',
                                                          usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                                          deprecated_version='2.12.0',
                                                          definition='Visueel bepalen van de veiligheid en conditie van een boom.',
                                                          owner=self)

        self._plantwijzewaarde = OTLAttribuut(field=KlBoomPlantwijzewaarde,
                                              naam='plantwijzewaarde',
                                              label='plantwijzewaarde',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.plantwijzewaarde',
                                              usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                              deprecated_version='2.12.0',
                                              definition='Een factor die de ontwikkeling van het uiterlijk (de habitus) van een boom relateert met de manier waarop hij geplant wordt.',
                                              owner=self)

        self._rapportageOnderzoek = OTLAttribuut(field=DtcDocument,
                                                 naam='rapportageOnderzoek',
                                                 label='rapportage onderzoek',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.rapportageOnderzoek',
                                                 usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                                 deprecated_version='2.12.0',
                                                 definition='Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt.',
                                                 owner=self)

        self._soortwaarde = OTLAttribuut(field=FloatOrDecimalField,
                                         naam='soortwaarde',
                                         label='soortwaarde',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.soortwaarde',
                                         usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                         deprecated_version='2.12.0',
                                         definition='Geeft voor een bepaalde boomsoort of -variëteit de verhouding weer tussen de prijs per cm² van die soort en de eenheidsprijs.',
                                         owner=self)

        self._stamomtrek = OTLAttribuut(field=KwantWrdInCentimeter,
                                        naam='stamomtrek',
                                        label='stamomtrek',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.stamomtrek',
                                        usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                        deprecated_version='2.12.0',
                                        definition='Omtrek van de stam van de boom in cm, gemeten op 1 meter boven de grond.',
                                        owner=self)

        self._standplaatswaarde = OTLAttribuut(field=KlBoomStandplaatswaarde,
                                               naam='standplaatswaarde',
                                               label='standplaatswaarde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.standplaatswaarde',
                                               usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                               deprecated_version='2.12.0',
                                               definition='De waarde van de boom afhankelijk van de bebouwingsdichtheid en de aanplantingsmogelijkheden rondom en voor de boom.',
                                               owner=self)

        self._tijdstempelBoomtoestand = OTLAttribuut(field=DateTimeField,
                                                     naam='tijdstempelBoomtoestand',
                                                     label='tijdstempel boomtoestand',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.tijdstempelBoomtoestand',
                                                     usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                                     deprecated_version='2.12.0',
                                                     definition='Datum van laatste snoeibeurt.',
                                                     owner=self)

        self._uitgebreidPlaatsonderzoek = OTLAttribuut(field=DtcDocument,
                                                       naam='uitgebreidPlaatsonderzoek',
                                                       label='uitgebreid plaatsonderzoek',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.uitgebreidPlaatsonderzoek',
                                                       usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                                       deprecated_version='2.12.0',
                                                       definition='Grondige beoordeling van de textuur en structuur van de bodem, met als doel een voorstel tot conditieverbeterende maatregelen.',
                                                       owner=self)

        self._wortelonderzoek = OTLAttribuut(field=DtcDocument,
                                             naam='wortelonderzoek',
                                             label='Wortelonderzoek',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.wortelonderzoek',
                                             usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                             deprecated_version='2.12.0',
                                             definition='Bepalen van de kwaliteit van de wortels (bv. aantasting door schimmels) of het bepalen van de reikwijdte van de wortels (bv. om een wortelbeschermingszone op te zetten in de buurt van werken van de bomen).',
                                             owner=self)

    @property
    def basiswaarde(self) -> KwantWrdInEuroWaarden:
        """Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."""
        return self._basiswaarde.get_waarde()

    @basiswaarde.setter
    def basiswaarde(self, value):
        self._basiswaarde.set_waarde(value, owner=self)

    @property
    def conditiebeoordeling(self) -> str:
        """De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout."""
        return self._conditiebeoordeling.get_waarde()

    @conditiebeoordeling.setter
    def conditiebeoordeling(self, value):
        self._conditiebeoordeling.set_waarde(value, owner=self)

    @property
    def conditiewaarde(self) -> str:
        """Een coëfficiënt die iets vertelt over de gezondheidstoestand (vitaliteit, conditie) en de levensverwachting van een boom."""
        return self._conditiewaarde.get_waarde()

    @conditiewaarde.setter
    def conditiewaarde(self, value):
        self._conditiewaarde.set_waarde(value, owner=self)

    @property
    def conflicten(self) -> str:
        """Mogelijke standplaatsconflicten die de condities of structuur van de boom negatief kunnen beïnvloeden."""
        return self._conflicten.get_waarde()

    @conflicten.setter
    def conflicten(self, value):
        self._conflicten.set_waarde(value, owner=self)

    @property
    def gebreken(self) -> List[str]:
        """Een visueel defect aan een boom wat dient gemonitord te worden."""
        return self._gebreken.get_waarde()

    @gebreken.setter
    def gebreken(self, value):
        self._gebreken.set_waarde(value, owner=self)

    @property
    def kroonDiameter(self) -> KwantWrdInMeterWaarden:
        """Diameter van de kroonprojectie in meter."""
        return self._kroonDiameter.get_waarde()

    @kroonDiameter.setter
    def kroonDiameter(self, value):
        self._kroonDiameter.set_waarde(value, owner=self)

    @property
    def krooninspectie(self) -> DtcDocumentWaarden:
        """Controle van gebrekssymptomen in de kroon."""
        return self._krooninspectie.get_waarde()

    @krooninspectie.setter
    def krooninspectie(self, value):
        self._krooninspectie.set_waarde(value, owner=self)

    @property
    def meerwaarde(self) -> str:
        """Mogelijkheid om de boom een waarde toe te kennen op basis van hun uitzonderlijke ecologische of erfgoedwaarde ."""
        return self._meerwaarde.get_waarde()

    @meerwaarde.setter
    def meerwaarde(self, value):
        self._meerwaarde.set_waarde(value, owner=self)

    @property
    def onderhoudstoestand(self) -> str:
        """De toestand van een boom die de eventuele snoeiachterstand aangeeft."""
        return self._onderhoudstoestand.get_waarde()

    @onderhoudstoestand.setter
    def onderhoudstoestand(self, value):
        self._onderhoudstoestand.set_waarde(value, owner=self)

    @property
    def onderzoekVisueleBoomcontrole(self) -> DtcDocumentWaarden:
        """Visueel bepalen van de veiligheid en conditie van een boom."""
        return self._onderzoekVisueleBoomcontrole.get_waarde()

    @onderzoekVisueleBoomcontrole.setter
    def onderzoekVisueleBoomcontrole(self, value):
        self._onderzoekVisueleBoomcontrole.set_waarde(value, owner=self)

    @property
    def plantwijzewaarde(self) -> str:
        """Een factor die de ontwikkeling van het uiterlijk (de habitus) van een boom relateert met de manier waarop hij geplant wordt."""
        return self._plantwijzewaarde.get_waarde()

    @plantwijzewaarde.setter
    def plantwijzewaarde(self, value):
        self._plantwijzewaarde.set_waarde(value, owner=self)

    @property
    def rapportageOnderzoek(self) -> DtcDocumentWaarden:
        """Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."""
        return self._rapportageOnderzoek.get_waarde()

    @rapportageOnderzoek.setter
    def rapportageOnderzoek(self, value):
        self._rapportageOnderzoek.set_waarde(value, owner=self)

    @property
    def soortwaarde(self) -> float:
        """Geeft voor een bepaalde boomsoort of -variëteit de verhouding weer tussen de prijs per cm² van die soort en de eenheidsprijs."""
        return self._soortwaarde.get_waarde()

    @soortwaarde.setter
    def soortwaarde(self, value):
        self._soortwaarde.set_waarde(value, owner=self)

    @property
    def stamomtrek(self) -> KwantWrdInCentimeterWaarden:
        """Omtrek van de stam van de boom in cm, gemeten op 1 meter boven de grond."""
        return self._stamomtrek.get_waarde()

    @stamomtrek.setter
    def stamomtrek(self, value):
        self._stamomtrek.set_waarde(value, owner=self)

    @property
    def standplaatswaarde(self) -> str:
        """De waarde van de boom afhankelijk van de bebouwingsdichtheid en de aanplantingsmogelijkheden rondom en voor de boom."""
        return self._standplaatswaarde.get_waarde()

    @standplaatswaarde.setter
    def standplaatswaarde(self, value):
        self._standplaatswaarde.set_waarde(value, owner=self)

    @property
    def tijdstempelBoomtoestand(self) -> datetime:
        """Datum van laatste snoeibeurt."""
        return self._tijdstempelBoomtoestand.get_waarde()

    @tijdstempelBoomtoestand.setter
    def tijdstempelBoomtoestand(self, value):
        self._tijdstempelBoomtoestand.set_waarde(value, owner=self)

    @property
    def uitgebreidPlaatsonderzoek(self) -> DtcDocumentWaarden:
        """Grondige beoordeling van de textuur en structuur van de bodem, met als doel een voorstel tot conditieverbeterende maatregelen."""
        return self._uitgebreidPlaatsonderzoek.get_waarde()

    @uitgebreidPlaatsonderzoek.setter
    def uitgebreidPlaatsonderzoek(self, value):
        self._uitgebreidPlaatsonderzoek.set_waarde(value, owner=self)

    @property
    def wortelonderzoek(self) -> DtcDocumentWaarden:
        """Bepalen van de kwaliteit van de wortels (bv. aantasting door schimmels) of het bepalen van de reikwijdte van de wortels (bv. om een wortelbeschermingszone op te zetten in de buurt van werken van de bomen)."""
        return self._wortelonderzoek.get_waarde()

    @wortelonderzoek.setter
    def wortelonderzoek(self, value):
        self._wortelonderzoek.set_waarde(value, owner=self)
