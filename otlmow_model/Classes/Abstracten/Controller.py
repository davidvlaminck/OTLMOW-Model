# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Controller(AIMNaamObject, PuntGeometrie):
    """Abstracte voor allerlei types van controllers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._batchnummer = OTLAttribuut(field=StringField,
                                         naam='batchnummer',
                                         label='batchnummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.batchnummer',
                                         definition='Nummer van de productiebatch van de leverancier.',
                                         owner=self)

        self._dNSNaam = OTLAttribuut(field=StringField,
                                     naam='dNSNaam',
                                     label='DNS-naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.dNSNaam',
                                     definition='DNS-naam van de controller.',
                                     owner=self)

        self._firmwareversie = OTLAttribuut(field=StringField,
                                            naam='firmwareversie',
                                            label='firmwareversie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.firmwareversie',
                                            definition='Firmwareversie van de controller.',
                                            owner=self)

        self._iPAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='iPAdres',
                                     label='IP-adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.iPAdres',
                                     definition='IP-adres van de controller.',
                                     owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

    @property
    def batchnummer(self) -> str:
        """Nummer van de productiebatch van de leverancier."""
        return self._batchnummer.get_waarde()

    @batchnummer.setter
    def batchnummer(self, value):
        self._batchnummer.set_waarde(value, owner=self)

    @property
    def dNSNaam(self) -> str:
        """DNS-naam van de controller."""
        return self._dNSNaam.get_waarde()

    @dNSNaam.setter
    def dNSNaam(self, value):
        self._dNSNaam.set_waarde(value, owner=self)

    @property
    def firmwareversie(self) -> str:
        """Firmwareversie van de controller."""
        return self._firmwareversie.get_waarde()

    @firmwareversie.setter
    def firmwareversie(self, value):
        self._firmwareversie.set_waarde(value, owner=self)

    @property
    def iPAdres(self) -> DteIPv4AdresWaarden:
        """IP-adres van de controller."""
        return self._iPAdres.get_waarde()

    @iPAdres.setter
    def iPAdres(self, value):
        self._iPAdres.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
