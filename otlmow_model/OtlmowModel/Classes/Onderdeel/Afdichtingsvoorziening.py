# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAfdichtingsvoorzieningtype import KlAfdichtingsvoorzieningtype
from ...Datatypes.KlMateriaalAfdichtingsvoorziening import KlMateriaalAfdichtingsvoorziening
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afdichtingsvoorziening(AIMNaamObject, PuntGeometrie):
    """Voorziening om te zorgen dat er geen water lekt tussen verschillende onderdelen van een beweegbare waterkerende constructie alsook tussen beweegbare en vaste waterbouwkundige constructies."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanslagbalk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BeweegbareWaterkerendeConstructie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie', direction='o')  # o = direction: outgoing

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.lengte',
                                    definition='De lengte van de afdichtingsvoorziening, uitgedrukt in meter',
                                    owner=self)

        self._materiaalAfdichtingsvoorziening = OTLAttribuut(field=KlMateriaalAfdichtingsvoorziening,
                                                             naam='materiaalAfdichtingsvoorziening',
                                                             label='materiaal afdichtingsvoorziening',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.materiaalAfdichtingsvoorziening',
                                                             definition='De verschillende materialen die worden gebruikt voor het maken van afdichtingsvoorzieningen.',
                                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.technischeFiche',
                                             definition='De technische fiche van de afdichtingsvoorziening.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlAfdichtingsvoorzieningtype,
                                  naam='type',
                                  label='type afdichtingsvoorziening',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.type',
                                  definition='De verschillende types afdichtingsvoorzieningen.',
                                  owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de afdichtingsvoorziening, uitgedrukt in meter"""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaalAfdichtingsvoorziening(self) -> str:
        """De verschillende materialen die worden gebruikt voor het maken van afdichtingsvoorzieningen."""
        return self._materiaalAfdichtingsvoorziening.get_waarde()

    @materiaalAfdichtingsvoorziening.setter
    def materiaalAfdichtingsvoorziening(self, value):
        self._materiaalAfdichtingsvoorziening.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de afdichtingsvoorziening."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De verschillende types afdichtingsvoorzieningen."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
