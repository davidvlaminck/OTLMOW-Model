# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.Abstracten.DetaiplanObject import DetaiplanObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMateriaalLadder import KlMateriaalLadder
from ...Datatypes.KlTypeOpstellingLadder import KlTypeOpstellingLadder
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ladder(AanhorighedenBrug, AanhorigheidKoker, AanhorigheidSluisStuw, DetaiplanObject, AIMNaamObject, PuntGeometrie):
    """Een ladder is een constructie van verticale bomen met horizontale sporten die gebruikt wordt als klimmiddel/gereedschap."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing

        self._heeftBordes = OTLAttribuut(field=BooleanField,
                                         naam='heeftBordes',
                                         label='heeft bordes',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.heeftBordes',
                                         definition='Geeft aan of de ladder een bordes heeft, al dan niet. Een bordes wordt voorzien bij kooiladders vanaf 10 meter om iedere 6 meter de mogelijkheid te geven om te rusten.',
                                         owner=self)

        self._heeftRailMetAntivaltoestel = OTLAttribuut(field=BooleanField,
                                                        naam='heeftRailMetAntivaltoestel',
                                                        label='heeft rail met antivaltoestel',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.heeftRailMetAntivaltoestel',
                                                        definition='Geeft aan of de ladder, al dan niet, een rail heeft met een antivaltoestel.',
                                                        owner=self)

        self._heeftVeiligheidsinstap = OTLAttribuut(field=BooleanField,
                                                    naam='heeftVeiligheidsinstap',
                                                    label='heeft veiligheidsinstap',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.heeftVeiligheidsinstap',
                                                    definition='Geeft aan of de ladder een veiligheidsinstap heeft, al dan niet.',
                                                    owner=self)

        self._heeftVeiligheidskooi = OTLAttribuut(field=BooleanField,
                                                  naam='heeftVeiligheidskooi',
                                                  label='heeft veiligheidskooi',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.heeftVeiligheidskooi',
                                                  definition='Geeft aan of de ladder een veiligheidskooi heeft, al dan niet.',
                                                  owner=self)

        self._isBeveiligd = OTLAttribuut(field=BooleanField,
                                         naam='isBeveiligd',
                                         label='is beveiligd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.isBeveiligd',
                                         definition='Geeft aan of de ladder beveiligd is, al dan niet. Bijvoorbeeld: de ladder heeft een slot tegen vandalisme,...',
                                         owner=self)

        self._lopendeMeter = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='lopendeMeter',
                                          label='lopende meter',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.lopendeMeter',
                                          definition='De lopende meter van de ladder. De uitschuifbare ladderbomen worden hier niet bij in rekening gebracht.',
                                          owner=self)

        self._materiaalLadder = OTLAttribuut(field=KlMateriaalLadder,
                                             naam='materiaalLadder',
                                             label='materiaal ladder',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.materiaalLadder',
                                             definition='Het materiaal waaruit de ladder is opgebouwd.',
                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.technischeFiche',
                                             definition='De technische fiche van de ladder.',
                                             owner=self)

        self._typeOpstelling = OTLAttribuut(field=KlTypeOpstellingLadder,
                                            naam='typeOpstelling',
                                            label='type opstelling',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.typeOpstelling',
                                            definition='Geeft aan of de type van de ladder inbouw of opbouw is.',
                                            owner=self)

        self._uitschuiffbaarlengte = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='uitschuiffbaarlengte',
                                                  label='uitschuifbare lengte',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.uitschuiffbaarlengte',
                                                  definition='De lengte, uitgedrukt in meter, tot waar de ladder uitschuifbaar is.',
                                                  owner=self)

    @property
    def heeftBordes(self) -> bool:
        """Geeft aan of de ladder een bordes heeft, al dan niet. Een bordes wordt voorzien bij kooiladders vanaf 10 meter om iedere 6 meter de mogelijkheid te geven om te rusten."""
        return self._heeftBordes.get_waarde()

    @heeftBordes.setter
    def heeftBordes(self, value):
        self._heeftBordes.set_waarde(value, owner=self)

    @property
    def heeftRailMetAntivaltoestel(self) -> bool:
        """Geeft aan of de ladder, al dan niet, een rail heeft met een antivaltoestel."""
        return self._heeftRailMetAntivaltoestel.get_waarde()

    @heeftRailMetAntivaltoestel.setter
    def heeftRailMetAntivaltoestel(self, value):
        self._heeftRailMetAntivaltoestel.set_waarde(value, owner=self)

    @property
    def heeftVeiligheidsinstap(self) -> bool:
        """Geeft aan of de ladder een veiligheidsinstap heeft, al dan niet."""
        return self._heeftVeiligheidsinstap.get_waarde()

    @heeftVeiligheidsinstap.setter
    def heeftVeiligheidsinstap(self, value):
        self._heeftVeiligheidsinstap.set_waarde(value, owner=self)

    @property
    def heeftVeiligheidskooi(self) -> bool:
        """Geeft aan of de ladder een veiligheidskooi heeft, al dan niet."""
        return self._heeftVeiligheidskooi.get_waarde()

    @heeftVeiligheidskooi.setter
    def heeftVeiligheidskooi(self, value):
        self._heeftVeiligheidskooi.set_waarde(value, owner=self)

    @property
    def isBeveiligd(self) -> bool:
        """Geeft aan of de ladder beveiligd is, al dan niet. Bijvoorbeeld: de ladder heeft een slot tegen vandalisme,..."""
        return self._isBeveiligd.get_waarde()

    @isBeveiligd.setter
    def isBeveiligd(self, value):
        self._isBeveiligd.set_waarde(value, owner=self)

    @property
    def lopendeMeter(self) -> KwantWrdInMeterWaarden:
        """De lopende meter van de ladder. De uitschuifbare ladderbomen worden hier niet bij in rekening gebracht."""
        return self._lopendeMeter.get_waarde()

    @lopendeMeter.setter
    def lopendeMeter(self, value):
        self._lopendeMeter.set_waarde(value, owner=self)

    @property
    def materiaalLadder(self) -> str:
        """Het materiaal waaruit de ladder is opgebouwd."""
        return self._materiaalLadder.get_waarde()

    @materiaalLadder.setter
    def materiaalLadder(self, value):
        self._materiaalLadder.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de ladder."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def typeOpstelling(self) -> str:
        """Geeft aan of de type van de ladder inbouw of opbouw is."""
        return self._typeOpstelling.get_waarde()

    @typeOpstelling.setter
    def typeOpstelling(self, value):
        self._typeOpstelling.set_waarde(value, owner=self)

    @property
    def uitschuiffbaarlengte(self) -> KwantWrdInMeterWaarden:
        """De lengte, uitgedrukt in meter, tot waar de ladder uitschuifbaar is."""
        return self._uitschuiffbaarlengte.get_waarde()

    @uitschuiffbaarlengte.setter
    def uitschuiffbaarlengte(self, value):
        self._uitschuiffbaarlengte.set_waarde(value, owner=self)
