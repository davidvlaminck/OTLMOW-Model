# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DteTekstblok import DteTekstblok, DteTekstblokWaarden
from ...Datatypes.KlRioleringVorm import KlRioleringVorm
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...Datatypes.KwantWrdInPromille import KwantWrdInPromille, KwantWrdInPromilleWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buis(AIMObject, LijnGeometrie):
    """Abstracte om de gemeenschappelijke eigenschappen en relaties van de verschillende soorten buizen onder één noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='o', deprecated='2.8.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding', direction='o', deprecated='2.8.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis', direction='o', deprecated='2.8.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis', direction='o', deprecated='2.8.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding', direction='o', deprecated='2.8.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis', direction='o', deprecated='2.8.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PompSchroefEnWaaier', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Waterweg', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluitkraan', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandhaspel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flens', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Infiltratievoorziening', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis', direction='o', deprecated='2.8.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OntluchterBrandleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontluchtingsventiel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenInfiltratievoorziening', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Reservoir', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spaarbekken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voetbocht', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VulpuntBrandweer', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waaier', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waterloop', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wervel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenInfiltratievoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spaarbekken', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot', direction='i')  # i = direction: incoming

        self._bokAfwaarts = OTLAttribuut(field=KwantWrdInMeterTAW,
                                         naam='bokAfwaarts',
                                         label='bok afwaarts',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokAfwaarts',
                                         definition='Peil in meter-TAW van de vloei aan de afwaartse kant van de buis.',
                                         owner=self)

        self._bokOpwaarts = OTLAttribuut(field=KwantWrdInMeterTAW,
                                         naam='bokOpwaarts',
                                         label='bok opwaarts',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokOpwaarts',
                                         definition='Peil in meter-TAW van de vloei aan de opwaartse kant van de buis.',
                                         owner=self)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedte',
                                     usagenote='Attribuut uit gebruik sinds versie 2.1.0 ',
                                     deprecated_version='2.1.0',
                                     definition='De breedte van de buis in millimeter.',
                                     owner=self)

        self._breedteBinnenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='breedteBinnenzijde',
                                                label='breedte binnenzijde',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBinnenzijde',
                                                definition='De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter.',
                                                owner=self)

        self._breedteBuitenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='breedteBuitenzijde',
                                                label='breedte buitenzijde',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBuitenzijde',
                                                definition='De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter.',
                                                owner=self)

        self._diepteAfwaarts = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='diepteAfwaarts',
                                            label='diepte afwaarts',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteAfwaarts',
                                            definition='Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel.',
                                            owner=self)

        self._diepteOpwaarts = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='diepteOpwaarts',
                                            label='diepte opwaarts',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteOpwaarts',
                                            definition='De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel.',
                                            owner=self)

        self._helling = OTLAttribuut(field=KwantWrdInPromille,
                                     naam='helling',
                                     label='helling',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.helling',
                                     definition='De helling van de buis in de lengterichting, uitgedrukt in promille.',
                                     owner=self)

        self._hoogteBinnenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='hoogteBinnenzijde',
                                               label='hoogte binnenzijde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBinnenzijde',
                                               definition='De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter.',
                                               owner=self)

        self._hoogteBuitenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='hoogteBuitenzijde',
                                               label='hoogte buitenzijde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBuitenzijde',
                                               definition='De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter.',
                                               owner=self)

        self._isManToegankelijk = OTLAttribuut(field=BooleanField,
                                               naam='isManToegankelijk',
                                               label='is man toegankelijk',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isManToegankelijk',
                                               definition='Bepaalt of de buis toegankelijk is voor een persoon.',
                                               owner=self)

        self._isOpgevuld = OTLAttribuut(field=BooleanField,
                                        naam='isOpgevuld',
                                        label='is opgevuld',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isOpgevuld',
                                        definition='Geeft aan of de buis gestabiliseerd/opgevuld is of niet.',
                                        owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',
                                    definition='De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',
                                    owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.technischeFiche',
                                             usagenote='Bestanden van het type xlsx of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de buis.',
                                             owner=self)

        self._toestandBuis = OTLAttribuut(field=DteTekstblok,
                                          naam='toestandBuis',
                                          label='toestand buis',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',
                                          definition='Opmerkingen van de toestand en staat van de buis.',
                                          owner=self)

        self._vorm = OTLAttribuut(field=KlRioleringVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.vorm',
                                  definition='Bepaalt de vorm van de buis.',
                                  owner=self)

    @property
    def bokAfwaarts(self) -> KwantWrdInMeterTAWWaarden:
        """Peil in meter-TAW van de vloei aan de afwaartse kant van de buis."""
        return self._bokAfwaarts.get_waarde()

    @bokAfwaarts.setter
    def bokAfwaarts(self, value):
        self._bokAfwaarts.set_waarde(value, owner=self)

    @property
    def bokOpwaarts(self) -> KwantWrdInMeterTAWWaarden:
        """Peil in meter-TAW van de vloei aan de opwaartse kant van de buis."""
        return self._bokOpwaarts.get_waarde()

    @bokOpwaarts.setter
    def bokOpwaarts(self, value):
        self._bokOpwaarts.set_waarde(value, owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van de buis in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def breedteBinnenzijde(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        return self._breedteBinnenzijde.get_waarde()

    @breedteBinnenzijde.setter
    def breedteBinnenzijde(self, value):
        self._breedteBinnenzijde.set_waarde(value, owner=self)

    @property
    def breedteBuitenzijde(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        return self._breedteBuitenzijde.get_waarde()

    @breedteBuitenzijde.setter
    def breedteBuitenzijde(self, value):
        self._breedteBuitenzijde.set_waarde(value, owner=self)

    @property
    def diepteAfwaarts(self) -> KwantWrdInMeterWaarden:
        """Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        return self._diepteAfwaarts.get_waarde()

    @diepteAfwaarts.setter
    def diepteAfwaarts(self, value):
        self._diepteAfwaarts.set_waarde(value, owner=self)

    @property
    def diepteOpwaarts(self) -> KwantWrdInMeterWaarden:
        """De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        return self._diepteOpwaarts.get_waarde()

    @diepteOpwaarts.setter
    def diepteOpwaarts(self, value):
        self._diepteOpwaarts.set_waarde(value, owner=self)

    @property
    def helling(self) -> KwantWrdInPromilleWaarden:
        """De helling van de buis in de lengterichting, uitgedrukt in promille."""
        return self._helling.get_waarde()

    @helling.setter
    def helling(self, value):
        self._helling.set_waarde(value, owner=self)

    @property
    def hoogteBinnenzijde(self) -> KwantWrdInMillimeterWaarden:
        """De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        return self._hoogteBinnenzijde.get_waarde()

    @hoogteBinnenzijde.setter
    def hoogteBinnenzijde(self, value):
        self._hoogteBinnenzijde.set_waarde(value, owner=self)

    @property
    def hoogteBuitenzijde(self) -> KwantWrdInMillimeterWaarden:
        """De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        return self._hoogteBuitenzijde.get_waarde()

    @hoogteBuitenzijde.setter
    def hoogteBuitenzijde(self, value):
        self._hoogteBuitenzijde.set_waarde(value, owner=self)

    @property
    def isManToegankelijk(self) -> bool:
        """Bepaalt of de buis toegankelijk is voor een persoon."""
        return self._isManToegankelijk.get_waarde()

    @isManToegankelijk.setter
    def isManToegankelijk(self, value):
        self._isManToegankelijk.set_waarde(value, owner=self)

    @property
    def isOpgevuld(self) -> bool:
        """Geeft aan of de buis gestabiliseerd/opgevuld is of niet."""
        return self._isOpgevuld.get_waarde()

    @isOpgevuld.setter
    def isOpgevuld(self, value):
        self._isOpgevuld.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """De technische fiche van de buis."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def toestandBuis(self) -> DteTekstblokWaarden:
        """Opmerkingen van de toestand en staat van de buis."""
        return self._toestandBuis.get_waarde()

    @toestandBuis.setter
    def toestandBuis(self, value):
        self._toestandBuis.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """Bepaalt de vorm van de buis."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
