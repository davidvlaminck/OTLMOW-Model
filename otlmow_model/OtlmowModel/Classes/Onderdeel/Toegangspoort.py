# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Toegangselement import Toegangselement
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlToegangspoortMerk import KlToegangspoortMerk
from ...Datatypes.KlToegangspoortModelnaam import KlToegangspoortModelnaam
from ...Datatypes.KlToegangspoortType import KlToegangspoortType
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangspoort(Toegangselement, AIMNaamObject, PuntGeometrie):
    """Element dat een bredere doorgang in een constructie of hekwerk afsluit ."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangspoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeOpslagplaats', direction='o')  # o = direction: outgoing

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangspoort.hoogte',
                                    definition='De verticale afmeting van de poort gemeten van de onderkant van de poort tot de bovenkant.',
                                    owner=self)

        self._merk = OTLAttribuut(field=KlToegangspoortMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangspoort.merk',
                                  definition='De modelnaam van de toegangspoort volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlToegangspoortModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangspoort.modelnaam',
                                       definition='De modelnaam van de toegangspoort volgens de fabrikant.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangspoort.technischeFiche',
                                             definition='Bijkomende documentatie met de technische details van de toegangspoort en de concrete uitvoering.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlToegangspoortType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangspoort.type',
                                  definition='Typering van de toegangspoort volgens de manier waarop ze opent.',
                                  owner=self)

    @property
    def hoogte(self) -> KwantWrdInCentimeterWaarden:
        """De verticale afmeting van de poort gemeten van de onderkant van de poort tot de bovenkant."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """De modelnaam van de toegangspoort volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de toegangspoort volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Bijkomende documentatie met de technische details van de toegangspoort en de concrete uitvoering."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Typering van de toegangspoort volgens de manier waarop ze opent."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
