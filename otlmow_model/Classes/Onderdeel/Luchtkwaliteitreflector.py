# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Luchtkwaliteittoestel import Luchtkwaliteittoestel
from otlmow_model.BaseClasses.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteitreflector(Luchtkwaliteittoestel):
    """Onderdeel van de luchtkwaliteitsensor dat het signaal uitgestuurd door de LuchtkwaliteitZenderOntvanger reflecteert om de luchtkwaliteit tussen beiden onderdelen te kunnen meten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luchtkwaliteitreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Luchtkwaliteitsensor')

        self._isBeschermd = OTLAttribuut(field=BooleanField,
                                         naam='isBeschermd',
                                         label='is beschermd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luchtkwaliteitreflector.isBeschermd',
                                         definition='Geeft aan of de sensor beschermd is tegen beschadiging, bv. door een aanrijding.',
                                         owner=self)

    @property
    def isBeschermd(self) -> bool:
        """Geeft aan of de sensor beschermd is tegen beschadiging, bv. door een aanrijding."""
        return self._isBeschermd.get_waarde()

    @isBeschermd.setter
    def isBeschermd(self, value):
        self._isBeschermd.set_waarde(value, owner=self)
