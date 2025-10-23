# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.VegetatieElement import VegetatieElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcAanlegBoomvorm import DtcAanlegBoomvorm, DtcAanlegBoomvormWaarden
from ...Datatypes.KlBoomGroeifase import KlBoomGroeifase
from ...Datatypes.KlBoomspiegelInvulling import KlBoomspiegelInvulling
from ...Datatypes.KlEindbeeldOpgaandeBoom import KlEindbeeldOpgaandeBoom
from ...Datatypes.KlKlassePlantjaar import KlKlassePlantjaar
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class OpgaandeBoom(VegetatieElement, PuntGeometrie):
    """Een opgaande boom is een boom waarvan de vorm van de kruin overeenkomt met zijn natuurlijke, soortgebonden habitus. Opgaande bomen kunnen een hoge, lage, brede, smalle of een afwijkende groeivorm hebben, zoals zuil- en treurvormen. De boom kan zich op volstrekt natuurlijke wijze uitgezaaid hebben en zijn groeivorm kan bepaald zijn door de natuurlijke groeiomstandigheden (bv. natuurlijke snoei). Ontstond de boom in kunstmatige omstandigheden, dan is de groeivorm bepaald door de jeugdsnoei in de kwekerij en is het eindbeeld van de boom bepaald door de begeleidingssnoei of vormsnoei die wordt uitgevoerd vanaf het planten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm', direction='o', deprecated='2.0.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand', direction='i', deprecated='2.0.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf', direction='i', deprecated='2.0.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerderOnderzoekTrekproef', direction='i', deprecated='2.0.0')  # i = direction: incoming

        self._aanleg = OTLAttribuut(field=DtcAanlegBoomvorm,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.aanleg',
                                    usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                    deprecated_version='2.0.0',
                                    definition='De manier van aanplanten van individuele bomen.',
                                    owner=self)

        self._boomspiegel = OTLAttribuut(field=KlBoomspiegelInvulling,
                                         naam='boomspiegel',
                                         label='boomspiegel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.boomspiegel',
                                         usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                         deprecated_version='2.0.0',
                                         definition='Het stuk grond rondom de stam van een boom. Dit is in de ideale situatie minstens zo groot is als de kruin van de boom.',
                                         owner=self)

        self._boomverankeringszone = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='boomverankeringszone',
                                                  label='boomverankeringszone',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.boomverankeringszone',
                                                  usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                  deprecated_version='2.0.0',
                                                  definition='De straal van de cirkelvormige ruimte waarbinnen de wortels zich bevinden die instaan voor de stabiliteit van de boom uitgedrukt in meter.',
                                                  owner=self)

        self._doorwortelbaarVolume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                                  naam='doorwortelbaarVolume',
                                                  label='doorwortelbaar volume',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.doorwortelbaarVolume',
                                                  usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                  deprecated_version='2.0.0',
                                                  definition='Het bodemvolume met voldoende mineralen, water en zuurstof die bereikbaar zijn voor een boom om erin te wortelen.',
                                                  owner=self)

        self._eindbeeld = OTLAttribuut(field=KlEindbeeldOpgaandeBoom,
                                       naam='eindbeeld',
                                       label='eindbeeld',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.eindbeeld',
                                       usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                       deprecated_version='2.0.0',
                                       definition='Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats.',
                                       owner=self)

        self._geschatteKlassePlantjaar = OTLAttribuut(field=KlKlassePlantjaar,
                                                      naam='geschatteKlassePlantjaar',
                                                      label='geschatte klasse plantjaar',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.geschatteKlassePlantjaar',
                                                      usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                      deprecated_version='2.0.0',
                                                      definition='Dit attribuut geeft een interval weer van 20 jaar waarin de boom geplant werd.',
                                                      owner=self)

        self._groeifase = OTLAttribuut(field=KlBoomGroeifase,
                                       naam='groeifase',
                                       label='groeifase',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.groeifase',
                                       usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                       deprecated_version='2.0.0',
                                       definition='Fase van beheer volgens de verschillende levensfases van de boom.',
                                       owner=self)

        self._heeftBoomrooster = OTLAttribuut(field=BooleanField,
                                              naam='heeftBoomrooster',
                                              label='heeft boomrooster',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.heeftBoomrooster',
                                              usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                              deprecated_version='2.0.0',
                                              definition='Duidt aan of een horizontale structuur aanwezig is die zorgt voor een adequate bescherming van bomen tegen betreding van de boomspiegel door voetgangers of verkeer.',
                                              owner=self)

        self._heeftLuchtleiding = OTLAttribuut(field=BooleanField,
                                               naam='heeftLuchtleiding',
                                               label='heeft luchtleiding',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.heeftLuchtleiding',
                                               usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                               deprecated_version='2.0.0',
                                               definition='Bepaling of een bovengrondse nutsleiding aanwezig is die in conflict kan komen met de boom.',
                                               owner=self)

        self._isVerplant = OTLAttribuut(field=BooleanField,
                                        naam='isVerplant',
                                        label='is verplant',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.isVerplant',
                                        usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                        deprecated_version='2.0.0',
                                        definition='Aanduiding of de opgaande boom al dan niet van locatie veranderd is na een eerste aanplant binnen het openbaar domein.',
                                        owner=self)

        self._kroonDiameter = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='kroonDiameter',
                                           label='kroon diameter',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.kroonDiameter',
                                           usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                           deprecated_version='2.0.0',
                                           definition='Diameter van de kroonprojectie in meter.',
                                           owner=self)

        self._takvrijeStamlengte = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='takvrijeStamlengte',
                                                label='takvrije stamlengte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.takvrijeStamlengte',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                deprecated_version='2.0.0',
                                                definition='Tot aan de hoogte van de gewenste takvrije stamlengte wordt de boom zodanig gesnoeid dat er één doorgaande stam is.',
                                                owner=self)

        self._totaleBoombeschermingszone = OTLAttribuut(field=KwantWrdInCentimeter,
                                                        naam='totaleBoombeschermingszone',
                                                        label='totale boombeschermingszone',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.totaleBoombeschermingszone',
                                                        usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                        deprecated_version='2.0.0',
                                                        definition='De straal van de cirkelvormige ruimte rond de boom waar maatregelen genomen worden om de boom te beschermen tijdens projecten of manifestaties uitgedrukt in centimeters.',
                                                        owner=self)

        self._vrijeDoorrijhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='vrijeDoorrijhoogte',
                                                label='vrije doorrijhoogte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom.vrijeDoorrijhoogte',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                deprecated_version='2.0.0',
                                                definition='Vrij te houden hoogte in meter, voor het doorrijden van verkeer toe te laten.',
                                                owner=self)

    @property
    def aanleg(self) -> DtcAanlegBoomvormWaarden:
        """De manier van aanplanten van individuele bomen."""
        return self._aanleg.get_waarde()

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def boomspiegel(self) -> str:
        """Het stuk grond rondom de stam van een boom. Dit is in de ideale situatie minstens zo groot is als de kruin van de boom."""
        return self._boomspiegel.get_waarde()

    @boomspiegel.setter
    def boomspiegel(self, value):
        self._boomspiegel.set_waarde(value, owner=self)

    @property
    def boomverankeringszone(self) -> KwantWrdInMeterWaarden:
        """De straal van de cirkelvormige ruimte waarbinnen de wortels zich bevinden die instaan voor de stabiliteit van de boom uitgedrukt in meter."""
        return self._boomverankeringszone.get_waarde()

    @boomverankeringszone.setter
    def boomverankeringszone(self, value):
        self._boomverankeringszone.set_waarde(value, owner=self)

    @property
    def doorwortelbaarVolume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het bodemvolume met voldoende mineralen, water en zuurstof die bereikbaar zijn voor een boom om erin te wortelen."""
        return self._doorwortelbaarVolume.get_waarde()

    @doorwortelbaarVolume.setter
    def doorwortelbaarVolume(self, value):
        self._doorwortelbaarVolume.set_waarde(value, owner=self)

    @property
    def eindbeeld(self) -> str:
        """Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats."""
        return self._eindbeeld.get_waarde()

    @eindbeeld.setter
    def eindbeeld(self, value):
        self._eindbeeld.set_waarde(value, owner=self)

    @property
    def geschatteKlassePlantjaar(self) -> str:
        """Dit attribuut geeft een interval weer van 20 jaar waarin de boom geplant werd."""
        return self._geschatteKlassePlantjaar.get_waarde()

    @geschatteKlassePlantjaar.setter
    def geschatteKlassePlantjaar(self, value):
        self._geschatteKlassePlantjaar.set_waarde(value, owner=self)

    @property
    def groeifase(self) -> str:
        """Fase van beheer volgens de verschillende levensfases van de boom."""
        return self._groeifase.get_waarde()

    @groeifase.setter
    def groeifase(self, value):
        self._groeifase.set_waarde(value, owner=self)

    @property
    def heeftBoomrooster(self) -> bool:
        """Duidt aan of een horizontale structuur aanwezig is die zorgt voor een adequate bescherming van bomen tegen betreding van de boomspiegel door voetgangers of verkeer."""
        return self._heeftBoomrooster.get_waarde()

    @heeftBoomrooster.setter
    def heeftBoomrooster(self, value):
        self._heeftBoomrooster.set_waarde(value, owner=self)

    @property
    def heeftLuchtleiding(self) -> bool:
        """Bepaling of een bovengrondse nutsleiding aanwezig is die in conflict kan komen met de boom."""
        return self._heeftLuchtleiding.get_waarde()

    @heeftLuchtleiding.setter
    def heeftLuchtleiding(self, value):
        self._heeftLuchtleiding.set_waarde(value, owner=self)

    @property
    def isVerplant(self) -> bool:
        """Aanduiding of de opgaande boom al dan niet van locatie veranderd is na een eerste aanplant binnen het openbaar domein."""
        return self._isVerplant.get_waarde()

    @isVerplant.setter
    def isVerplant(self, value):
        self._isVerplant.set_waarde(value, owner=self)

    @property
    def kroonDiameter(self) -> KwantWrdInMeterWaarden:
        """Diameter van de kroonprojectie in meter."""
        return self._kroonDiameter.get_waarde()

    @kroonDiameter.setter
    def kroonDiameter(self, value):
        self._kroonDiameter.set_waarde(value, owner=self)

    @property
    def takvrijeStamlengte(self) -> KwantWrdInMeterWaarden:
        """Tot aan de hoogte van de gewenste takvrije stamlengte wordt de boom zodanig gesnoeid dat er één doorgaande stam is."""
        return self._takvrijeStamlengte.get_waarde()

    @takvrijeStamlengte.setter
    def takvrijeStamlengte(self, value):
        self._takvrijeStamlengte.set_waarde(value, owner=self)

    @property
    def totaleBoombeschermingszone(self) -> KwantWrdInCentimeterWaarden:
        """De straal van de cirkelvormige ruimte rond de boom waar maatregelen genomen worden om de boom te beschermen tijdens projecten of manifestaties uitgedrukt in centimeters."""
        return self._totaleBoombeschermingszone.get_waarde()

    @totaleBoombeschermingszone.setter
    def totaleBoombeschermingszone(self, value):
        self._totaleBoombeschermingszone.set_waarde(value, owner=self)

    @property
    def vrijeDoorrijhoogte(self) -> KwantWrdInMeterWaarden:
        """Vrij te houden hoogte in meter, voor het doorrijden van verkeer toe te laten."""
        return self._vrijeDoorrijhoogte.get_waarde()

    @vrijeDoorrijhoogte.setter
    def vrijeDoorrijhoogte(self, value):
        self._vrijeDoorrijhoogte.set_waarde(value, owner=self)
