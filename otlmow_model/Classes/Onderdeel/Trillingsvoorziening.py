# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trillingsvoorziening(AIMNaamObject, PuntGeometrie):
    """De trillingsvoorziening zorgt ervoor dat de trillingen van het kunstwerk anders reageren (trillingen verminderen). Deze wordt vaak geleverd door een leverancier en zo in het kunstwerk gestoken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trillingsvoorziening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trillingsvoorziening.technischeFiche',
                                             definition='De technische fiche van de trillingsvoorziening. De productietekening is hierbij opgenomen.',
                                             owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de trillingsvoorziening. De productietekening is hierbij opgenomen."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
