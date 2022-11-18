# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Onderdeel.Software import Software
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlIVRIBaseline import KlIVRIBaseline


# Generated with OTLClassCreator. To modify: extend, do not edit
class IVRIComponent(Software):
    """Abstracte die eigenschappen van de iVRI (intelligente verkeersregelaar) component bundelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor')

        self._baseline = OTLAttribuut(field=KlIVRIBaseline,
                                      naam='baseline',
                                      label='baseline',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.baseline',
                                      definition='Specificatieversie van het protocol waarop de iVRI component werkt.',
                                      owner=self)

        self._certificaat = OTLAttribuut(field=DtcDocument,
                                         naam='certificaat',
                                         label='certificaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.certificaat',
                                         definition='Certificaat van de keuringsinstantie dat wordt uitgereikt aan een iVRI (intelligente verkeersregelaar) component. ',
                                         owner=self)

    @property
    def baseline(self) -> str:
        """Specificatieversie van het protocol waarop de iVRI component werkt."""
        return self._baseline.get_waarde()

    @baseline.setter
    def baseline(self, value):
        self._baseline.set_waarde(value, owner=self)

    @property
    def certificaat(self) -> DtcDocumentWaarden:
        """Certificaat van de keuringsinstantie dat wordt uitgereikt aan een iVRI (intelligente verkeersregelaar) component. """
        return self._certificaat.get_waarde()

    @certificaat.setter
    def certificaat(self, value):
        self._certificaat.set_waarde(value, owner=self)
