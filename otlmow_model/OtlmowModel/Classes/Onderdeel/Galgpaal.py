# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.VRIDraagconstructie import VRIDraagconstructie
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ...Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Galgpaal(VRIDraagconstructie, PuntGeometrie):
    """De galgpalen zijn bestemd voor het bevestigen van verkeerslichten, signaalborden, wegwijzers boven het wegdek. Bovendien laten zij het bevestigen toe van één of meerdere lantaarns van het type 200 op de paalschacht. De draagwijdte van de arm moet kunnen reiken tot 9 m. De galgpalen beantwoorden aan SB270-51-6.15"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerafsluiting', direction='o')  # o = direction: outgoing

        self._aantalLiggers = OTLAttribuut(field=FloatOrDecimalField,
                                           naam='aantalLiggers',
                                           label='aantal liggers',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.aantalLiggers',
                                           definition='Het aantal liggers waarmee de arm van de galgpaal is uitgevoerd.',
                                           owner=self)

        self._armlengte = OTLAttribuut(field=KwantWrdInMeter,
                                       naam='armlengte',
                                       label='armlengte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.armlengte',
                                       definition='Lengte van de arm van een galgpaal in meter.',
                                       owner=self)

        self._berekeningsnota = OTLAttribuut(field=DtcDocument,
                                             naam='berekeningsnota',
                                             label='berekeningsnota',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.berekeningsnota',
                                             definition='Een bijlage met daarin de berekeningsnota voor de galgpaal.',
                                             owner=self)

        self._dwarsdoorsnede = OTLAttribuut(field=KlDraagconstructieDwarsdoorsnede,
                                            naam='dwarsdoorsnede',
                                            label='dwarsdoorsnede',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.dwarsdoorsnede',
                                            definition='De vorm van de dwarsdoorsnede van het opstaande deel van de galgpaal.',
                                            owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.technischeFiche',
                                             definition='Een bijlage waarin de detailtekeningen van de galgpaal zijn opgenomen.',
                                             owner=self)

    @property
    def aantalLiggers(self) -> float:
        """Het aantal liggers waarmee de arm van de galgpaal is uitgevoerd."""
        return self._aantalLiggers.get_waarde()

    @aantalLiggers.setter
    def aantalLiggers(self, value):
        self._aantalLiggers.set_waarde(value, owner=self)

    @property
    def armlengte(self) -> KwantWrdInMeterWaarden:
        """Lengte van de arm van een galgpaal in meter."""
        return self._armlengte.get_waarde()

    @armlengte.setter
    def armlengte(self, value):
        self._armlengte.set_waarde(value, owner=self)

    @property
    def berekeningsnota(self) -> DtcDocumentWaarden:
        """Een bijlage met daarin de berekeningsnota voor de galgpaal."""
        return self._berekeningsnota.get_waarde()

    @berekeningsnota.setter
    def berekeningsnota(self, value):
        self._berekeningsnota.set_waarde(value, owner=self)

    @property
    def dwarsdoorsnede(self) -> str:
        """De vorm van de dwarsdoorsnede van het opstaande deel van de galgpaal."""
        return self._dwarsdoorsnede.get_waarde()

    @dwarsdoorsnede.setter
    def dwarsdoorsnede(self, value):
        self._dwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Een bijlage waarin de detailtekeningen van de galgpaal zijn opgenomen."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
