# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ConstructieElement import ConstructieElement
from ...Classes.Abstracten.HoutenConstructieElement import HoutenConstructieElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoutenConstructieprofiel(ConstructieElement, HoutenConstructieElement, PuntGeometrie, LijnGeometrie):
    """Houten enkelvoudig constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. De breedte is weer gelijk of kleiner dan de hoogte. Dit profiel heeft een dragende functie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructiefObject', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._detailDwarsdoorsnede = OTLAttribuut(field=DtcDocument,
                                                  naam='detailDwarsdoorsnede',
                                                  label='detail dwarsdoorsnede',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel.detailDwarsdoorsnede',
                                                  definition='Details van de afmetingen en van de dwarsdoorsnedes.',
                                                  owner=self)

        self._heeftGrondcontact = OTLAttribuut(field=BooleanField,
                                               naam='heeftGrondcontact',
                                               label='heeft grondcontact',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel.heeftGrondcontact',
                                               definition='Geeft aan of het houten profiel of een onderdeel ervan in contact staat met grond, al dan niet.',
                                               owner=self)

        self._heeftWatercontact = OTLAttribuut(field=BooleanField,
                                               naam='heeftWatercontact',
                                               label='heeft watercontact',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel.heeftWatercontact',
                                               definition='Geeft aan of het houten profiel of een onderdeel ervan in contact staat met water, al dan niet.',
                                               owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel.lengte',
                                    definition='De lengte, in lopende meter, van het profiel.',
                                    owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel.volume',
                                    definition='Het volume, uitgedrukt in kubieke meter, van het houten profiel in zijn geheel.',
                                    owner=self)

    @property
    def detailDwarsdoorsnede(self) -> DtcDocumentWaarden:
        """Details van de afmetingen en van de dwarsdoorsnedes."""
        return self._detailDwarsdoorsnede.get_waarde()

    @detailDwarsdoorsnede.setter
    def detailDwarsdoorsnede(self, value):
        self._detailDwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def heeftGrondcontact(self) -> bool:
        """Geeft aan of het houten profiel of een onderdeel ervan in contact staat met grond, al dan niet."""
        return self._heeftGrondcontact.get_waarde()

    @heeftGrondcontact.setter
    def heeftGrondcontact(self, value):
        self._heeftGrondcontact.set_waarde(value, owner=self)

    @property
    def heeftWatercontact(self) -> bool:
        """Geeft aan of het houten profiel of een onderdeel ervan in contact staat met water, al dan niet."""
        return self._heeftWatercontact.get_waarde()

    @heeftWatercontact.setter
    def heeftWatercontact(self, value):
        self._heeftWatercontact.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte, in lopende meter, van het profiel."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume, uitgedrukt in kubieke meter, van het houten profiel in zijn geheel."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
