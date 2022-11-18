# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.DtuAfmetingVerkeersbord import DtuAfmetingVerkeersbord, DtuAfmetingVerkeersbordWaarden
from otlmow_model.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from otlmow_model.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbord(PuntGeometrie):
    """Abstracte klasse voor borden die een fysieke drager van verkeerstekens kunnen zijn waarvan de betekenis bepaald wordt door een verkeersbordconcept."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling')

        self._aanzicht = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                      naam='aanzicht',
                                      label='aanzicht',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.aanzicht',
                                      usagenote='In radialen of graden ten opzichte van het noorden in wijzerzin.',
                                      definition='De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as (het ware noorden). De hoek wordt gemeten in radialen of graden ten opzichte van het noorden in wijzerzin.',
                                      owner=self)

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.afbeelding',
                                        kardinaliteit_max='*',
                                        definition='De afbeelding van het verkeersbord.',
                                        owner=self)

        self._afmeting = OTLAttribuut(field=DtuAfmetingVerkeersbord,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.afmeting',
                                      definition='De afmeting(en) van het verkeersbord.',
                                      owner=self)

        self._fabricagevoorschrift = OTLAttribuut(field=StringField,
                                                  naam='fabricagevoorschrift',
                                                  label='fabricagevoorschrift',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.fabricagevoorschrift',
                                                  definition='Het fabricagevoorschrift op het verkeersbord.',
                                                  owner=self)

        self._operationeleStatus = OTLAttribuut(field=KlOperationeleStatus,
                                                naam='operationeleStatus',
                                                label='operationele status',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.operationeleStatus',
                                                usagenote="Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                definition='De operationele status van het verkeersbord.',
                                                owner=self)

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.opstelhoogte',
                                          definition='Afstand tussen het maaiveld en de onderrand van het bord.',
                                          owner=self)

    @property
    def aanzicht(self) -> KwantWrdInDecimaleGradenWaarden:
        """De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as (het ware noorden). De hoek wordt gemeten in radialen of graden ten opzichte van het noorden in wijzerzin."""
        return self._aanzicht.get_waarde()

    @aanzicht.setter
    def aanzicht(self, value):
        self._aanzicht.set_waarde(value, owner=self)

    @property
    def afbeelding(self) -> List[DtcDocumentWaarden]:
        """De afbeelding van het verkeersbord."""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def afmeting(self) -> DtuAfmetingVerkeersbordWaarden:
        """De afmeting(en) van het verkeersbord."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def fabricagevoorschrift(self) -> str:
        """Het fabricagevoorschrift op het verkeersbord."""
        return self._fabricagevoorschrift.get_waarde()

    @fabricagevoorschrift.setter
    def fabricagevoorschrift(self, value):
        self._fabricagevoorschrift.set_waarde(value, owner=self)

    @property
    def operationeleStatus(self) -> str:
        """De operationele status van het verkeersbord."""
        return self._operationeleStatus.get_waarde()

    @operationeleStatus.setter
    def operationeleStatus(self, value):
        self._operationeleStatus.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self) -> KwantWrdInMeterWaarden:
        """Afstand tussen het maaiveld en de onderrand van het bord."""
        return self._opstelhoogte.get_waarde()

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)
