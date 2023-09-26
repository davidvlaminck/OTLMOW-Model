# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Communicatieapparatuur import Communicatieapparatuur
from otlmow_model.Classes.Abstracten.FirmwareObject import FirmwareObject
from otlmow_model.Datatypes.KlZOToegangNetwerkTechniek import KlZOToegangNetwerkTechniek


# Generated with OTLClassCreator. To modify: extend, do not edit
class ZenderOntvangerToegang(Communicatieapparatuur, FirmwareObject):
    """Abstracte voor relaties van Zender,Ontvanger en Repeater met andere apparatuur."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector')

        self._netwerkTechniek = OTLAttribuut(field=KlZOToegangNetwerkTechniek,
                                             naam='netwerkTechniek',
                                             label='netwerk techniek',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang.netwerkTechniek',
                                             definition='De techniek of standaard waarmee signalen over het netwerk verstuurd worden.',
                                             owner=self)

    @property
    def netwerkTechniek(self) -> str:
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden."""
        return self._netwerkTechniek.get_waarde()

    @netwerkTechniek.setter
    def netwerkTechniek(self, value):
        self._netwerkTechniek.set_waarde(value, owner=self)
