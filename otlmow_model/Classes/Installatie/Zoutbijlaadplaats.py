# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zoutbijlaadplaats(AIMNaamObject, VlakGeometrie):
    """Site in het beheer van een district, waar strooiwagens zout of pekel kunnen bijladen, wanneer ze tijdens de winterdienst hun strooiroute afleggen. De leverancier kan toegang krijgen (batch of codeklavier) om de tanks of de silo’s terug te vullen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._opstellingsplan = OTLAttribuut(field=DtcDocument,
                                             naam='opstellingsplan',
                                             label='opstellingsplan',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats.opstellingsplan',
                                             definition='Een plan dat de opstelling van alle infrastructuurelementen op de site aangeeft.',
                                             owner=self)

    @property
    def opstellingsplan(self) -> DtcDocumentWaarden:
        """Een plan dat de opstelling van alle infrastructuurelementen op de site aangeeft."""
        return self._opstellingsplan.get_waarde()

    @opstellingsplan.setter
    def opstellingsplan(self, value):
        self._opstellingsplan.set_waarde(value, owner=self)
