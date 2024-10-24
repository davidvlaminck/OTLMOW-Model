# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Laag import Laag
from ...Classes.Abstracten.LaagDikte import LaagDikte
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcGrondsoort import DtcGrondsoort, DtcGrondsoortWaarden
from ...Datatypes.DtcSoortVervuiling import DtcSoortVervuiling, DtcSoortVervuilingWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grond(Laag, LaagDikte):
    """Lithologisch hoofd- en nevenbestanddeel (als code) van de laag zoals gebruikt bij Databank Ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PiezometrischeBuis', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afdekking', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Afgraving', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bemesting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Bodemverbeteringsmiddel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Grondbewerking', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Ophoging', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Uitgraving', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', direction='i')  # i = direction: incoming

        self._grondsoort = OTLAttribuut(field=DtcGrondsoort,
                                        naam='grondsoort',
                                        label='soort grond',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond.grondsoort',
                                        definition='Lithologisch hoofd- en nevenbestanddeel (als code) van de laag zoals gebruikt bij databank ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering).',
                                        owner=self)

        self._milieuHygienischeCode = OTLAttribuut(field=NonNegIntegerField,
                                                   naam='milieuHygienischeCode',
                                                   label='milieuhygiënische code',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond.milieuHygienischeCode',
                                                   definition='Het 3-delig nummer dat gehanteerd wordt door de vzw grondbank om de milieuhygiënische mogelijkheden van een partij bodem of grond aan te geven.',
                                                   owner=self)

        self._soortVervuiling = OTLAttribuut(field=DtcSoortVervuiling,
                                             naam='soortVervuiling',
                                             label='soort vervuiling',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond.soortVervuiling',
                                             definition='De soort vervuiling die vastgesteld is op het pakket grond.',
                                             owner=self)

        self._technischVerslagBodemonderzoek = OTLAttribuut(field=DtcDocument,
                                                            naam='technischVerslagBodemonderzoek',
                                                            label='technisch verslag bodemonderzoek',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond.technischVerslagBodemonderzoek',
                                                            kardinaliteit_max='*',
                                                            definition='Het technisch verslag van een bodemonderzoek.',
                                                            owner=self)

        self._tot = OTLAttribuut(field=KwantWrdInMeter,
                                 naam='tot',
                                 label='tot',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond.tot',
                                 definition='Diepte van de onderkant van de laag in meter. https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/generiek/GeneriekeDataTypes.xsd (DiepteType).',
                                 owner=self)

        self._van = OTLAttribuut(field=KwantWrdInMeter,
                                 naam='van',
                                 label='van',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond.van',
                                 definition='Diepte van de bovenkant van de laag in meter. https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/generiek/GeneriekeDataTypes.xsd (DiepteType).',
                                 owner=self)

    @property
    def grondsoort(self) -> DtcGrondsoortWaarden:
        """Lithologisch hoofd- en nevenbestanddeel (als code) van de laag zoals gebruikt bij databank ondergrond Vlaanderen (gecodeerde lithologie en geotechnische codering)."""
        return self._grondsoort.get_waarde()

    @grondsoort.setter
    def grondsoort(self, value):
        self._grondsoort.set_waarde(value, owner=self)

    @property
    def milieuHygienischeCode(self) -> int:
        """Het 3-delig nummer dat gehanteerd wordt door de vzw grondbank om de milieuhygiënische mogelijkheden van een partij bodem of grond aan te geven."""
        return self._milieuHygienischeCode.get_waarde()

    @milieuHygienischeCode.setter
    def milieuHygienischeCode(self, value):
        self._milieuHygienischeCode.set_waarde(value, owner=self)

    @property
    def soortVervuiling(self) -> DtcSoortVervuilingWaarden:
        """De soort vervuiling die vastgesteld is op het pakket grond."""
        return self._soortVervuiling.get_waarde()

    @soortVervuiling.setter
    def soortVervuiling(self, value):
        self._soortVervuiling.set_waarde(value, owner=self)

    @property
    def technischVerslagBodemonderzoek(self) -> List[DtcDocumentWaarden]:
        """Het technisch verslag van een bodemonderzoek."""
        return self._technischVerslagBodemonderzoek.get_waarde()

    @technischVerslagBodemonderzoek.setter
    def technischVerslagBodemonderzoek(self, value):
        self._technischVerslagBodemonderzoek.set_waarde(value, owner=self)

    @property
    def tot(self) -> KwantWrdInMeterWaarden:
        """Diepte van de onderkant van de laag in meter. https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/generiek/GeneriekeDataTypes.xsd (DiepteType)."""
        return self._tot.get_waarde()

    @tot.setter
    def tot(self, value):
        self._tot.set_waarde(value, owner=self)

    @property
    def van(self) -> KwantWrdInMeterWaarden:
        """Diepte van de bovenkant van de laag in meter. https://www.dov.vlaanderen.be/xdov/schema/latest/xsd/kern/generiek/GeneriekeDataTypes.xsd (DiepteType)."""
        return self._van.get_waarde()

    @van.setter
    def van(self, value):
        self._van.set_waarde(value, owner=self)
