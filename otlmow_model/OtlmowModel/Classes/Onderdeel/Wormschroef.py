# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.PompSchroefEnWaaier import PompSchroefEnWaaier
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wormschroef(PompSchroefEnWaaier, LijnGeometrie):
    """Een spiraalvormige schroef die toelaat vloeistoffen, sluries, of poeders te transporteren. De schroef, geplaatst in een gesloten of deels open buis, wordt aangedreven en draait rond zijn eigen as. Deze draaiende beweging leidt tot de verplaatsing van het te verplaatsen medium. Wanneer het medium in opwaartse richting getransporteerd wordt spreekt men van een pomp. Wanneer het medium in afwaartse richting beweegt en al doende de schroef doet draaien, spreekt men van een turbine. Wordt ook wel waterschroef, opvoerschroef, vijzelpomp, of een schroef van Archimedes genoemd. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef.gewicht',
                                     definition='Het gewicht van de wormschroef in kilogram.',
                                     owner=self)

        self._isAfgesloten = OTLAttribuut(field=BooleanField,
                                          naam='isAfgesloten',
                                          label='is afgesloten',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef.isAfgesloten',
                                          definition='Geeft aan of de schroef zich in een buis bevindt en dus afgesloten is.',
                                          owner=self)

        self._isVisvriendelijk = OTLAttribuut(field=BooleanField,
                                              naam='isVisvriendelijk',
                                              label='is visvriendelijk',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef.isVisvriendelijk',
                                              definition='Geeft aan of de wormschroef visvriendelijk is. Een schroef is visvriendelijk, als hij zodanig is ontworpen dat een vissen die worden meegeschept in leven blijven.',
                                              owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef.lengte',
                                    definition='De lengte van de wormschroef volgens zijn as.',
                                    owner=self)

        self._opvoerhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opvoerhoogte',
                                          label='opvoerhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef.opvoerhoogte',
                                          definition='De hoogte tot waarop het medium wordt opgepompt.',
                                          owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht van de wormschroef in kilogram."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def isAfgesloten(self) -> bool:
        """Geeft aan of de schroef zich in een buis bevindt en dus afgesloten is."""
        return self._isAfgesloten.get_waarde()

    @isAfgesloten.setter
    def isAfgesloten(self, value):
        self._isAfgesloten.set_waarde(value, owner=self)

    @property
    def isVisvriendelijk(self) -> bool:
        """Geeft aan of de wormschroef visvriendelijk is. Een schroef is visvriendelijk, als hij zodanig is ontworpen dat een vissen die worden meegeschept in leven blijven."""
        return self._isVisvriendelijk.get_waarde()

    @isVisvriendelijk.setter
    def isVisvriendelijk(self, value):
        self._isVisvriendelijk.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de wormschroef volgens zijn as."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def opvoerhoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte tot waarop het medium wordt opgepompt."""
        return self._opvoerhoogte.get_waarde()

    @opvoerhoogte.setter
    def opvoerhoogte(self, value):
        self._opvoerhoogte.set_waarde(value, owner=self)
