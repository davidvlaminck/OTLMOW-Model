# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ASTRIDInstallatie(AIMNaamObject, PuntGeometrie):
    """Een (radio)heruitzendingsinstallatie van radiosignalen (over TETRA in een hogere frequentieband van 380 tot 400 MHz) ondersteund door ASTRID als communicatiesysteem voor de hulpdiensten. Door de ontvangst- en  zendfrequenties verschillend te maken ontstaat tweerichtingscommunicatie over grote afstanden en op plaatsen, waar radiogolven normaal niet geraken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ASTRIDInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalSplitter')

        self._certificaat = OTLAttribuut(field=DtcDocument,
                                         naam='certificaat',
                                         label='certificaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ASTRIDInstallatie.certificaat',
                                         definition='Documenten van interne of externe organisaties, die de installatie goedkeuren of opmerkingen geven.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ASTRIDInstallatie.technischeFiche',
                                             definition='De technische fiche van de ASTRID installatie.',
                                             owner=self)

    @property
    def certificaat(self) -> DtcDocumentWaarden:
        """Documenten van interne of externe organisaties, die de installatie goedkeuren of opmerkingen geven."""
        return self._certificaat.get_waarde()

    @certificaat.setter
    def certificaat(self, value):
        self._certificaat.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de ASTRID installatie."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
