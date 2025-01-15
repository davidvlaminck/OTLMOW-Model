# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlVerkenmerkType import KlVerkenmerkType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkenmerk(AanhorighedenBrug, AanhorigheidKoker, AanhorigheidSluisStuw, AIMNaamObject, PuntGeometrie):
    """Een (roestvast) verkenmerk is geplaatst op een kunstwerk. Het periodiek opmeten maakt mogelijk de vervormingen van het kunstwerk te bepalen en de evolutie ervan na te gaan t.o.v. de begintoestand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkenmerk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdek', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkenmerk.technischeFiche',
                                             definition='De technische fiche van het verkenmerk.',
                                             owner=self)

        self._typeVerkenmerk = OTLAttribuut(field=KlVerkenmerkType,
                                            naam='typeVerkenmerk',
                                            label='type verkenmerk',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkenmerk.typeVerkenmerk',
                                            definition='Het type van verkenmerk.',
                                            owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van het verkenmerk."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def typeVerkenmerk(self) -> str:
        """Het type van verkenmerk."""
        return self._typeVerkenmerk.get_waarde()

    @typeVerkenmerk.setter
    def typeVerkenmerk(self, value):
        self._typeVerkenmerk.set_waarde(value, owner=self)
