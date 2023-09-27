# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.DtcAdres import DtcAdres, DtcAdresWaarden
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.DtcExterneReferentie import DtcExterneReferentie, DtcExterneReferentieWaarden
from otlmow_model.Datatypes.KlVerkeerstekenWettelijkeStatus import KlVerkeerstekenWettelijkeStatus
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersteken(AIMObject, GeenGeometrie):
    """Abstracte klasse voor aanwijzingen ten behoeve van de weggebruikers die verbonden wordt aan het aankondigen of opleggen van een bepaalde verkeersmaatregel zoals bepaald in de wegcode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken')

        self._adres = OTLAttribuut(field=DtcAdres,
                                   naam='adres',
                                   label='adres',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.adres',
                                   definition='Adres van het verkeersteken.',
                                   owner=self)

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.afbeelding',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='Foto van het verkeersteken.',
                                        owner=self)

        self._mobiliteitsMaatregel = OTLAttribuut(field=DtcExterneReferentie,
                                                  naam='mobiliteitsMaatregel',
                                                  label='mobiliteitsmaatregel',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.mobiliteitsMaatregel',
                                                  kardinaliteit_min='0',
                                                  kardinaliteit_max='*',
                                                  definition='Externe referentie naar een maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren.',
                                                  owner=self)

        self._plaatsbeschrijving = OTLAttribuut(field=StringField,
                                                naam='plaatsbeschrijving',
                                                label='plaatsbeschrijving',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.plaatsbeschrijving',
                                                definition='Tekstuele beschrijving waar het verkeersteken zal komen.',
                                                owner=self)

        self._signalisatieVergunning = OTLAttribuut(field=DtcExterneReferentie,
                                                    naam='signalisatieVergunning',
                                                    label='signalisatievergunning',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.signalisatieVergunning',
                                                    kardinaliteit_min='0',
                                                    kardinaliteit_max='*',
                                                    definition='Externe referentie naar een vergunning voor het tijdelijk aanbrengen of wijzigen van signalisatie op het openbaar domein of privaat domein met openbaar karakter.',
                                                    owner=self)

        self._variabelOpschrift = OTLAttribuut(field=StringField,
                                               naam='variabelOpschrift',
                                               label='variabel opschrift',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.variabelOpschrift',
                                               definition='Variabele tekst die op het verkeersbordconcept komt te staan.',
                                               owner=self)

        self._wettelijkeStatus = OTLAttribuut(field=KlVerkeerstekenWettelijkeStatus,
                                              naam='wettelijkeStatus',
                                              label='wettelijke status',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.wettelijkeStatus',
                                              usagenote='Bijvoorbeeld: vergund, niet-vergund, in ontwerp',
                                              definition='Duidt de wettelijke status aan van het verkeersteken.',
                                              owner=self)

    @property
    def adres(self) -> DtcAdresWaarden:
        """Adres van het verkeersteken."""
        return self._adres.get_waarde()

    @adres.setter
    def adres(self, value):
        self._adres.set_waarde(value, owner=self)

    @property
    def afbeelding(self) -> List[DtcDocumentWaarden]:
        """Foto van het verkeersteken."""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def mobiliteitsMaatregel(self) -> List[DtcExterneReferentieWaarden]:
        """Externe referentie naar een maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren."""
        return self._mobiliteitsMaatregel.get_waarde()

    @mobiliteitsMaatregel.setter
    def mobiliteitsMaatregel(self, value):
        self._mobiliteitsMaatregel.set_waarde(value, owner=self)

    @property
    def plaatsbeschrijving(self) -> str:
        """Tekstuele beschrijving waar het verkeersteken zal komen."""
        return self._plaatsbeschrijving.get_waarde()

    @plaatsbeschrijving.setter
    def plaatsbeschrijving(self, value):
        self._plaatsbeschrijving.set_waarde(value, owner=self)

    @property
    def signalisatieVergunning(self) -> List[DtcExterneReferentieWaarden]:
        """Externe referentie naar een vergunning voor het tijdelijk aanbrengen of wijzigen van signalisatie op het openbaar domein of privaat domein met openbaar karakter."""
        return self._signalisatieVergunning.get_waarde()

    @signalisatieVergunning.setter
    def signalisatieVergunning(self, value):
        self._signalisatieVergunning.set_waarde(value, owner=self)

    @property
    def variabelOpschrift(self) -> str:
        """Variabele tekst die op het verkeersbordconcept komt te staan."""
        return self._variabelOpschrift.get_waarde()

    @variabelOpschrift.setter
    def variabelOpschrift(self, value):
        self._variabelOpschrift.set_waarde(value, owner=self)

    @property
    def wettelijkeStatus(self) -> str:
        """Duidt de wettelijke status aan van het verkeersteken."""
        return self._wettelijkeStatus.get_waarde()

    @wettelijkeStatus.setter
    def wettelijkeStatus(self, value):
        self._wettelijkeStatus.set_waarde(value, owner=self)
