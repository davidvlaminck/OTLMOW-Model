# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Bestrating import Bestrating
from otlmow_model.Datatypes.DtcAfmetingBxlInCm import DtcAfmetingBxlInCm, DtcAfmetingBxlInCmWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanKassei(Bestrating):
    """Bestrating van kasseien, in rij gelegd. Kasseien zijn bestratingselementen van porfier, kwartsiet, graniet, of van harde zandsteen die geen schilferige structuur heeft. Ze hebben een dicht aaneengesloten en homogene korrel, zonder steenkorst, kwade aders of kwakaders en vertonen geen diamantkop."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._afmetingVanBestratingselementBxl = OTLAttribuut(field=DtcAfmetingBxlInCm,
                                                              naam='afmetingVanBestratingselementBxl',
                                                              label='afmeting van bestratingselement bxl',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei.afmetingVanBestratingselementBxl',
                                                              definition='Afmeting van de breedte in cm (langste) en van de lengte in cm (kortste) van de kassei.',
                                                              owner=self)

    @property
    def afmetingVanBestratingselementBxl(self) -> DtcAfmetingBxlInCmWaarden:
        """Afmeting van de breedte in cm (langste) en van de lengte in cm (kortste) van de kassei."""
        return self._afmetingVanBestratingselementBxl.get_waarde()

    @afmetingVanBestratingselementBxl.setter
    def afmetingVanBestratingselementBxl(self, value):
        self._afmetingVanBestratingselementBxl.set_waarde(value, owner=self)
