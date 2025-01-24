# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlTypeAfwateringsgeul import KlTypeAfwateringsgeul
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afwateringsgeul(AIMObject, LijnGeometrie):
    """Een geul of goot die deel uitmaakt van de weginrichting en geplaatst werd met het oog op de afwatering van oppervlaktewater."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul', direction='o')  # o = direction: outgoing

        self._aantalZandvangers = OTLAttribuut(field=NonNegIntegerField,
                                               naam='aantalZandvangers',
                                               label='aantal zandvangers',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul.aantalZandvangers',
                                               definition='Het aantal zandvangers aanwezig in de totale lengte van de afwateringsgeul.',
                                               owner=self)

        self._isConform = OTLAttribuut(field=BooleanField,
                                       naam='isConform',
                                       label='is conform',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul.isConform',
                                       definition='Duidt aan of de afwateringsgeul voldoet aan de norm zoals beschreven in Standaardbestek 250.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul.technischeFiche',
                                             definition='De technische fiche van de afwateringsgeul.',
                                             owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul.totaleLengte',
                                          definition='De totale lengte van de geprefabriceerde elementen in lopende meter.',
                                          owner=self)

        self._type = OTLAttribuut(field=KlTypeAfwateringsgeul,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afwateringsgeul.type',
                                  definition='Het type van de afwateringsgeul.',
                                  owner=self)

    @property
    def aantalZandvangers(self) -> int:
        """Het aantal zandvangers aanwezig in de totale lengte van de afwateringsgeul."""
        return self._aantalZandvangers.get_waarde()

    @aantalZandvangers.setter
    def aantalZandvangers(self, value):
        self._aantalZandvangers.set_waarde(value, owner=self)

    @property
    def isConform(self) -> bool:
        """Duidt aan of de afwateringsgeul voldoet aan de norm zoals beschreven in Standaardbestek 250."""
        return self._isConform.get_waarde()

    @isConform.setter
    def isConform(self, value):
        self._isConform.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de afwateringsgeul."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def totaleLengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van de geprefabriceerde elementen in lopende meter."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van de afwateringsgeul."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
