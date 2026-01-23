# coding=utf-8
from typing import List
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Epoxydrain(AIMNaamObject, LijnGeometrie):
    """Een aangebracht drainagekanaal uit microepoxybeton bedoeld voor het afvoeren van water bovenop de afdichting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermlaag', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerlaag', direction='o')  # o = direction: outgoing

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain.breedte',
                                     definition='De breedte van de epoxydrain in centimeter.',
                                     owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain.dikte',
                                   definition='De dikte van de epoxydrain in centimeter.',
                                   owner=self)

        self._isGeprefabriceerd = OTLAttribuut(field=BooleanField,
                                               naam='isGeprefabriceerd',
                                               label='is geprefabriceerd',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain.isGeprefabriceerd',
                                               definition='Duidt aan of de epoxydrain geprefabriceerd is.',
                                               owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain.lengte',
                                    definition='De lengte van de epoxydrain in meter.',
                                    owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain.technischeFiche',
                                             usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de epoxydrain.',
                                             owner=self)

    @property
    def breedte(self) -> KwantWrdInCentimeterWaarden:
        """De breedte van de epoxydrain in centimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInCentimeterWaarden:
        """De dikte van de epoxydrain in centimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def isGeprefabriceerd(self) -> bool:
        """Duidt aan of de epoxydrain geprefabriceerd is."""
        return self._isGeprefabriceerd.get_waarde()

    @isGeprefabriceerd.setter
    def isGeprefabriceerd(self, value):
        self._isGeprefabriceerd.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de epoxydrain in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """De technische fiche van de epoxydrain."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
