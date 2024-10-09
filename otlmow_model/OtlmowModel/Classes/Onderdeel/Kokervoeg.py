# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlTypeMateriaal import KlTypeMateriaal
from ...Datatypes.KlTypeVoeg import KlTypeVoeg
from ...Datatypes.KwantWrdInBar import KwantWrdInBar, KwantWrdInBarWaarden
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kokervoeg(AIMObject, LijnGeometrie):
    """De kokervoeg is de naad of overgang tussen twee verschillende of gelijke materialen zodat elementen van de koker vrij kunnen bewegen ten opzichte van elkaar zonder schade te veroorzaken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker', direction='o')  # o = direction: outgoing

        self._dilatatieCapaciteit = OTLAttribuut(field=KwantWrdInCentimeter,
                                                 naam='dilatatieCapaciteit',
                                                 label='dilatatie capaciteit',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg.dilatatieCapaciteit',
                                                 definition='Geeft de dilatatie capaciteit van de voeg weer in centimer.',
                                                 owner=self)

        self._drukWeerstand = OTLAttribuut(field=KwantWrdInBar,
                                           naam='drukWeerstand',
                                           label='druk weerstand',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg.drukWeerstand',
                                           definition='De druk die de voeg aankan in bar.',
                                           owner=self)

        self._etagDocument = OTLAttribuut(field=DtcDocument,
                                          naam='etagDocument',
                                          label='etag document',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg.etagDocument',
                                          definition='De richtlijn voor uitvoering van een voeg.',
                                          owner=self)

        self._heeftVerkeerOverVoeg = OTLAttribuut(field=BooleanField,
                                                  naam='heeftVerkeerOverVoeg',
                                                  label='heeft verkeer over voeg',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg.heeftVerkeerOverVoeg',
                                                  definition='Geeft weer of er al dan niet verkeer over de voeg passeert',
                                                  owner=self)

        self._materiaal = OTLAttribuut(field=KlTypeMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg.materiaal',
                                       definition='Geeft het materiaal weer dat gebruikt is voor de voegen in de koker.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg.technischeFiche',
                                             definition='Technische fiche van de voeg',
                                             owner=self)

        self._typeKokervoeg = OTLAttribuut(field=KlTypeVoeg,
                                           naam='typeKokervoeg',
                                           label='type kokervoeg',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg.typeKokervoeg',
                                           definition='Geeft het type weer van de voeg tussen de koker elementen.',
                                           owner=self)

    @property
    def dilatatieCapaciteit(self) -> KwantWrdInCentimeterWaarden:
        """Geeft de dilatatie capaciteit van de voeg weer in centimer."""
        return self._dilatatieCapaciteit.get_waarde()

    @dilatatieCapaciteit.setter
    def dilatatieCapaciteit(self, value):
        self._dilatatieCapaciteit.set_waarde(value, owner=self)

    @property
    def drukWeerstand(self) -> KwantWrdInBarWaarden:
        """De druk die de voeg aankan in bar."""
        return self._drukWeerstand.get_waarde()

    @drukWeerstand.setter
    def drukWeerstand(self, value):
        self._drukWeerstand.set_waarde(value, owner=self)

    @property
    def etagDocument(self) -> DtcDocumentWaarden:
        """De richtlijn voor uitvoering van een voeg."""
        return self._etagDocument.get_waarde()

    @etagDocument.setter
    def etagDocument(self, value):
        self._etagDocument.set_waarde(value, owner=self)

    @property
    def heeftVerkeerOverVoeg(self) -> bool:
        """Geeft weer of er al dan niet verkeer over de voeg passeert"""
        return self._heeftVerkeerOverVoeg.get_waarde()

    @heeftVerkeerOverVoeg.setter
    def heeftVerkeerOverVoeg(self, value):
        self._heeftVerkeerOverVoeg.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Geeft het materiaal weer dat gebruikt is voor de voegen in de koker."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Technische fiche van de voeg"""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def typeKokervoeg(self) -> str:
        """Geeft het type weer van de voeg tussen de koker elementen."""
        return self._typeKokervoeg.get_waarde()

    @typeKokervoeg.setter
    def typeKokervoeg(self, value):
        self._typeKokervoeg.set_waarde(value, owner=self)
