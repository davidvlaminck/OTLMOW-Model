# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenSchroefpaal(BetonnenConstructieElement, Funderingspaal):
    """Met behulp van een schroefas in de grond gevormde, geluidsarme en trillingsvrije funderingspaal met volledige wegpersing van de grond over de volledige paallengte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenSchroefpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

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
