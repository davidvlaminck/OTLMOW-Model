# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bufferinstallatie(Geleidingsmechanisme, AIMNaamObject):
    """Een verzameling van elementen die gebruikt worden om krachten of schokken op te vangen en te dempen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelbewegingsmechanisme', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buffercilinder', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagstoel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukvat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Houdriem', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stootblok', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerhuis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verenpakket', direction='i')  # i = direction: incoming

        self._karakteristiekeToelaatbareBelasting = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                                 naam='karakteristiekeToelaatbareBelasting',
                                                                 label='karakteristieke toelaatbare belasting',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie.karakteristiekeToelaatbareBelasting',
                                                                 definition='De karakteristieke maximale toelaatbare belasting van de buffer, uitgedrukt in kilonewton.',
                                                                 owner=self)

    @property
    def karakteristiekeToelaatbareBelasting(self) -> KwantWrdInKiloNewtonWaarden:
        """De karakteristieke maximale toelaatbare belasting van de buffer, uitgedrukt in kilonewton."""
        return self._karakteristiekeToelaatbareBelasting.get_waarde()

    @karakteristiekeToelaatbareBelasting.setter
    def karakteristiekeToelaatbareBelasting(self, value):
        self._karakteristiekeToelaatbareBelasting.set_waarde(value, owner=self)
