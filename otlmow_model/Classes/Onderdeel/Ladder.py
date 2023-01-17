# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlMateriaalLadder import KlMateriaalLadder
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ladder(AIMNaamObject, AanhorighedenBrug, LijnGeometrie):
    """Een ladder is een constructie van verticale bomen met horizontale sporten die gebruikt wordt als klimmiddel/gereedschap."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AanhorighedenBrug.__init__(self)
        LijnGeometrie.__init__(self)

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

        self._uitschuiffbaarlengte = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='uitschuiffbaarlengte',
                                                  label='uitschuifbare lengte',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder.uitschuiffbaarlengte',
                                                  definition='De lengte, uitgedrukt in meter, tot waar de ladder uitschuifbaar is.',
                                                  owner=self)

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
    def uitschuiffbaarlengte(self) -> KwantWrdInMeterWaarden:
        """De lengte, uitgedrukt in meter, tot waar de ladder uitschuifbaar is."""
        return self._uitschuiffbaarlengte.get_waarde()

    @uitschuiffbaarlengte.setter
    def uitschuiffbaarlengte(self, value):
        self._uitschuiffbaarlengte.set_waarde(value, owner=self)
