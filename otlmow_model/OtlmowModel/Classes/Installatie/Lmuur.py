# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lmuur(Grondkeringen, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Grond- en/of waterkerend betonnen element bedoeld om een niveauverschil in het maaiveld op te vangen met een teen of voet aan de basis waaraan het zijn stabiliteit ontleent."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegband', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegplaat', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenConstructieObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk', direction='i')  # i = direction: incoming

        self._technischeFicheLmuur = OTLAttribuut(field=DtcDocument,
                                                  naam='technischeFicheLmuur',
                                                  label='technische fiche L-muur',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur.technischeFicheLmuur',
                                                  definition='De technische fiche waarin alle specificaties zijn opgenomen van de L-muur.',
                                                  owner=self)

        self._totaleBreedteVoet = OTLAttribuut(field=KwantWrdInCentimeter,
                                               naam='totaleBreedteVoet',
                                               label='totale breedte voet',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur.totaleBreedteVoet',
                                               definition='De totale breedte van de voet uitgedrukt in centimeter.',
                                               owner=self)

    @property
    def technischeFicheLmuur(self) -> DtcDocumentWaarden:
        """De technische fiche waarin alle specificaties zijn opgenomen van de L-muur."""
        return self._technischeFicheLmuur.get_waarde()

    @technischeFicheLmuur.setter
    def technischeFicheLmuur(self, value):
        self._technischeFicheLmuur.set_waarde(value, owner=self)

    @property
    def totaleBreedteVoet(self) -> KwantWrdInCentimeterWaarden:
        """De totale breedte van de voet uitgedrukt in centimeter."""
        return self._totaleBreedteVoet.get_waarde()

    @totaleBreedteVoet.setter
    def totaleBreedteVoet(self, value):
        self._totaleBreedteVoet.set_waarde(value, owner=self)
