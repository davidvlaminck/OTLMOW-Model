# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlVerkenmerkType import KlVerkenmerkType
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkenmerk(AanhorighedenBrug, AIMNaamObject, PuntGeometrie):
    """Een (roestvast) verkenmerk is geplaatst op een kunstwerk. Het periodiek opmeten maakt mogelijk de vervormingen van het kunstwerk te bepalen en de evolutie ervan na te gaan t.o.v. de begintoestand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkenmerk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AanhorighedenBrug.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdek')

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
