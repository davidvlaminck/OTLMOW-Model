# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from otlmow_model.Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenSchroefpaal(BetonnenConstructieElement, Funderingspaal):
    """Met behulp van een schroefas in de grond gevormde, geluidsarme en trillingsvrije funderingspaal met volledige wegpersing van de grond over de volledige paallengte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenSchroefpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')

        self._heeftVerlorenVoerbuis = OTLAttribuut(field=BooleanField,
                                                   naam='heeftVerlorenVoerbuis',
                                                   label='heeft verloren voerbuis',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenSchroefpaal.heeftVerlorenVoerbuis',
                                                   definition='Geeft aan of de betonnen schroefpaal een verloren schroefbuis heeft of niet.',
                                                   owner=self)

        self._nuttigeLengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='nuttigeLengte',
                                           label='nuttige lengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenSchroefpaal.nuttigeLengte',
                                           definition='Afstand gemeten, in meter, volgens de as van de schroefpaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het afkappeil) en het aanzetpeil (definitief funderingspeil).',
                                           owner=self)

    @property
    def heeftVerlorenVoerbuis(self) -> bool:
        """Geeft aan of de betonnen schroefpaal een verloren schroefbuis heeft of niet."""
        return self._heeftVerlorenVoerbuis.get_waarde()

    @heeftVerlorenVoerbuis.setter
    def heeftVerlorenVoerbuis(self, value):
        self._heeftVerlorenVoerbuis.set_waarde(value, owner=self)

    @property
    def nuttigeLengte(self) -> KwantWrdInMeterWaarden:
        """Afstand gemeten, in meter, volgens de as van de schroefpaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het afkappeil) en het aanzetpeil (definitief funderingspeil)."""
        return self._nuttigeLengte.get_waarde()

    @nuttigeLengte.setter
    def nuttigeLengte(self, value):
        self._nuttigeLengte.set_waarde(value, owner=self)
