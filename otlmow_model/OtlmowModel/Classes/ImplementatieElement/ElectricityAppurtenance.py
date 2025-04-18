# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.Appurtenance import Appurtenance
from ...Datatypes.KlElectricityAppurtenanceType import KlElectricityAppurtenanceType
from ...Datatypes.KlElectricitySubthema import KlElectricitySubthema


# Generated with OTLClassCreator. To modify: extend, do not edit
class ElectricityAppurtenance(Appurtenance):
    """Appurtenance-objecten zijn “toebehoren” of accessoires, dus allerlei apparaten, toestellen en dergelijke,kortom diverse soorten leidingelementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityAppurtenance'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Z30Groep', direction='o')  # o = direction: outgoing

        self._appurtenanceType = OTLAttribuut(field=KlElectricityAppurtenanceType,
                                              naam='appurtenanceType',
                                              label='appurtenanceType',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityAppurtenance.appurtenanceType',
                                              definition='AppurtenanceType van de ElectricityAppurtenance.',
                                              owner=self)

        self._subthema = OTLAttribuut(field=KlElectricitySubthema,
                                      naam='subthema',
                                      label='subthema',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityAppurtenance.subthema',
                                      definition='Classificatie van de asset volgens zijn functie op basis van een vaste lijst.',
                                      owner=self)

    @property
    def appurtenanceType(self) -> str:
        """AppurtenanceType van de ElectricityAppurtenance."""
        return self._appurtenanceType.get_waarde()

    @appurtenanceType.setter
    def appurtenanceType(self, value):
        self._appurtenanceType.set_waarde(value, owner=self)

    @property
    def subthema(self) -> str:
        """Classificatie van de asset volgens zijn functie op basis van een vaste lijst."""
        return self._subthema.get_waarde()

    @subthema.setter
    def subthema(self, value):
        self._subthema.set_waarde(value, owner=self)
