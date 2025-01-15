# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Gewichtsmuur(Grondkeringen, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Kerende constructie die stabiliteit ontleent aan zijn eigen gewicht. Onder stabiliteit dient verstaan te worden: glijden, omkantelen en verticaal draagvermogen. De muur is (meestal) onderaan breder dan bovenaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gewichtsmuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenConstructieObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk', direction='i')  # i = direction: incoming

        self._isUitgevoerdAlsBlokkenmuur = OTLAttribuut(field=BooleanField,
                                                        naam='isUitgevoerdAlsBlokkenmuur',
                                                        label='is uitgevoerd als blokkenmuur',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gewichtsmuur.isUitgevoerdAlsBlokkenmuur',
                                                        definition='Geeft aan of de gewichtsmuur uitgevoerd is als blokkenmuur of niet.',
                                                        owner=self)

        self._technischeFicheGewichtsmuur = OTLAttribuut(field=DtcDocument,
                                                         naam='technischeFicheGewichtsmuur',
                                                         label='technische fiche gewichtsmuur',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gewichtsmuur.technischeFicheGewichtsmuur',
                                                         definition='Technische fiche dat technische details bijhoudt van de gewichtsmuur.',
                                                         owner=self)

    @property
    def isUitgevoerdAlsBlokkenmuur(self) -> bool:
        """Geeft aan of de gewichtsmuur uitgevoerd is als blokkenmuur of niet."""
        return self._isUitgevoerdAlsBlokkenmuur.get_waarde()

    @isUitgevoerdAlsBlokkenmuur.setter
    def isUitgevoerdAlsBlokkenmuur(self, value):
        self._isUitgevoerdAlsBlokkenmuur.set_waarde(value, owner=self)

    @property
    def technischeFicheGewichtsmuur(self) -> DtcDocumentWaarden:
        """Technische fiche dat technische details bijhoudt van de gewichtsmuur."""
        return self._technischeFicheGewichtsmuur.get_waarde()

    @technischeFicheGewichtsmuur.setter
    def technischeFicheGewichtsmuur(self, value):
        self._technischeFicheGewichtsmuur.set_waarde(value, owner=self)
