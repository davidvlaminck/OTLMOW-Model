# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ConstructieElement import ConstructieElement
from otlmow_model.Datatypes.DtcBetonspecificaties import DtcBetonspecificaties, DtcBetonspecificatiesWaarden
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Breedplaat(ConstructieElement, VlakGeometrie):
    """Geprefabriceerd structuurelement dat over de volledige lengte voorzien is van minstens 2 driedimensionale tralieliggers en dat bestemd is om de meewerkende onderkant te vormen van een dragende brugdekplaat of van een bouwkundige constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Breedplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        ConstructieElement.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand')

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Breedplaat.dikte',
                                   definition='De dikte van de breedplaat, uitgedrukt in millimeter.',
                                   owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Breedplaat.oppervlakte',
                                         definition='De oppervlakte van de breedplaat, uitgedrukt in vierkante meter.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Breedplaat.technischeFiche',
                                             definition='De technische fiche van de breedplaat. Alle afmetingen en hoe het samengesteld is, is hierin opgenomen.',
                                             owner=self)

        self._typeBeton = OTLAttribuut(field=DtcBetonspecificaties,
                                       naam='typeBeton',
                                       label='type beton',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Breedplaat.typeBeton',
                                       definition='Type van het gebruikte beton.',
                                       owner=self)

    @property
    def dikte(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van de breedplaat, uitgedrukt in millimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de breedplaat, uitgedrukt in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de breedplaat. Alle afmetingen en hoe het samengesteld is, is hierin opgenomen."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def typeBeton(self) -> DtcBetonspecificatiesWaarden:
        """Type van het gebruikte beton."""
        return self._typeBeton.get_waarde()

    @typeBeton.setter
    def typeBeton(self, value):
        self._typeBeton.set_waarde(value, owner=self)
