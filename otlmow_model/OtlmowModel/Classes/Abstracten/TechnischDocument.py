# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from ...Datatypes.DtcTechnischDocument import DtcTechnischDocument, DtcTechnischDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class TechnischDocument(ABC):
    """Abstracte met technisch document"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TechnischDocument'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._technischDocument = OTLAttribuut(field=DtcTechnischDocument,
                                               naam='technischDocument',
                                               label='technisch document',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TechnischDocument.technischDocument',
                                               kardinaliteit_max='*',
                                               definition='Een technisch document zoals een detailplan, een technische fiche en/of een rekennota.',
                                               owner=self)

    @property
    def technischDocument(self) -> List[DtcTechnischDocumentWaarden]:
        """Een technisch document zoals een detailplan, een technische fiche en/of een rekennota."""
        return self._technischDocument.get_waarde()

    @technischDocument.setter
    def technischDocument(self, value):
        self._technischDocument.set_waarde(value, owner=self)
