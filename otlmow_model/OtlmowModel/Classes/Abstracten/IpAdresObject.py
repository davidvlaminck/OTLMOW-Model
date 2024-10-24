# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IpAdresObject(PuntGeometrie):
    """Abstracte klasse voor een IP4 adres."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IpAdresObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IpAdresObject.ipAdres',
                                     definition='Netwerkadresgegevens of ip-adres van het element.',
                                     owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """Netwerkadresgegevens of ip-adres van het element."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)
