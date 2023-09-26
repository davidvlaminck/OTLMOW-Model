# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BijlageVoertuigkering(ABC):
    """Abstracte om bestanden te bundelen omtrent voertuigkering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BijlageVoertuigkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._testrapportVoertuigkering = OTLAttribuut(field=DtcDocument,
                                                       naam='testrapportVoertuigkering',
                                                       label='testrapport voertuigkering',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BijlageVoertuigkering.testrapportVoertuigkering',
                                                       kardinaliteit_max='*',
                                                       definition='De testresultaten van de crashtesten die op de voertuigkerende constructie uitgevoerd zijn.',
                                                       owner=self)

        self._videoVoertuigkering = OTLAttribuut(field=DtcDocument,
                                                 naam='videoVoertuigkering',
                                                 label='video voertuigkering',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BijlageVoertuigkering.videoVoertuigkering',
                                                 kardinaliteit_max='*',
                                                 definition='Video-opname van de crashtesten op de voertuigkerende constructie.',
                                                 owner=self)

    @property
    def testrapportVoertuigkering(self) -> List[DtcDocumentWaarden]:
        """De testresultaten van de crashtesten die op de voertuigkerende constructie uitgevoerd zijn."""
        return self._testrapportVoertuigkering.get_waarde()

    @testrapportVoertuigkering.setter
    def testrapportVoertuigkering(self, value):
        self._testrapportVoertuigkering.set_waarde(value, owner=self)

    @property
    def videoVoertuigkering(self) -> List[DtcDocumentWaarden]:
        """Video-opname van de crashtesten op de voertuigkerende constructie."""
        return self._videoVoertuigkering.get_waarde()

    @videoVoertuigkering.setter
    def videoVoertuigkering(self, value):
        self._videoVoertuigkering.set_waarde(value, owner=self)
