# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Signalisatie import Signalisatie
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.DtcExterneReferentie import DtcExterneReferentie, DtcExterneReferentieWaarden
from otlmow_model.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from otlmow_model.Datatypes.KlPositieSoort import KlPositieSoort
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordopstelling(Signalisatie, AIMObject, PuntGeometrie):
    """Het geheel van verticale verkeerssignalisatie die bevestigd is aan één of meerdere draagconstructies op éénzelfde geolocatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.afbeelding',
                                        usagenote='Een bestand dat een afbeelding weergeeft.',
                                        kardinaliteit_max='*',
                                        definition='Grafische weergave van de opstelling geplaatst op het openbaar domein.',
                                        owner=self)

        self._isBotsvriendelijk = OTLAttribuut(field=BooleanField,
                                               naam='isBotsvriendelijk',
                                               label='is botsvriendelijk',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.isBotsvriendelijk',
                                               definition='Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert.',
                                               owner=self)

        self._operationeleStatus = OTLAttribuut(field=KlOperationeleStatus,
                                                naam='operationeleStatus',
                                                label='operationele status',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.operationeleStatus',
                                                usagenote="Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                definition='Operationele status van de Verkeersbordopstelling volgens keuzelijst.',
                                                owner=self)

        self._positieTovRijweg = OTLAttribuut(field=KlPositieSoort,
                                              naam='positieTovRijweg',
                                              label='positie ten opzichte van de rijweg',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.positieTovRijweg',
                                              usagenote='Bijvoorbeeld: boven, rechts, links',
                                              definition='De plaatsing van de opstelling ten aanzien van de rijbaan.',
                                              owner=self)

        self._wegSegment = OTLAttribuut(field=DtcExterneReferentie,
                                        naam='wegSegment',
                                        label='wegsegment',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.wegSegment',
                                        usagenote='Dit is niet noodzakelijk het wegsegment waarop het verkeersbord van toepassing is.',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='Wegsegment waarbij de verkeersbordopstelling geplaatst is.',
                                        owner=self)

    @property
    def afbeelding(self) -> List[DtcDocumentWaarden]:
        """Grafische weergave van de opstelling geplaatst op het openbaar domein."""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def isBotsvriendelijk(self) -> bool:
        """Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert."""
        return self._isBotsvriendelijk.get_waarde()

    @isBotsvriendelijk.setter
    def isBotsvriendelijk(self, value):
        self._isBotsvriendelijk.set_waarde(value, owner=self)

    @property
    def operationeleStatus(self) -> str:
        """Operationele status van de Verkeersbordopstelling volgens keuzelijst."""
        return self._operationeleStatus.get_waarde()

    @operationeleStatus.setter
    def operationeleStatus(self, value):
        self._operationeleStatus.set_waarde(value, owner=self)

    @property
    def positieTovRijweg(self) -> str:
        """De plaatsing van de opstelling ten aanzien van de rijbaan."""
        return self._positieTovRijweg.get_waarde()

    @positieTovRijweg.setter
    def positieTovRijweg(self, value):
        self._positieTovRijweg.set_waarde(value, owner=self)

    @property
    def wegSegment(self) -> List[DtcExterneReferentieWaarden]:
        """Wegsegment waarbij de verkeersbordopstelling geplaatst is."""
        return self._wegSegment.get_waarde()

    @wegSegment.setter
    def wegSegment(self, value):
        self._wegSegment.set_waarde(value, owner=self)
