# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlTypeSchachtHeipaal import KlTypeSchachtHeipaal
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenHeipaal(BetonnenConstructieElement, Funderingspaal):
    """Betonnen paal die in de grond wordt gebracht door deze in een hei-installatie te plaatsen waarna men er een zwaar gewicht (heiblok) op laat vallen. De grond onder de paal wordt samengeperst waardoor de draagkracht groter wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal'
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

        self._diameterPaalschacht = OTLAttribuut(field=KwantWrdInMillimeter,
                                                 naam='diameterPaalschacht',
                                                 label='diameter paalschacht',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.diameterPaalschacht',
                                                 definition='Doorsnede in millimeter van de schacht van de paal.',
                                                 owner=self)

        self._heeftVerbredeVoet = OTLAttribuut(field=BooleanField,
                                               naam='heeftVerbredeVoet',
                                               label='heeft verbrede voet',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.heeftVerbredeVoet',
                                               definition='Geeft aan of de voet breder is gemaakt, al dan niet.',
                                               owner=self)

        self._heeftVerlorenVoerbuis = OTLAttribuut(field=BooleanField,
                                                   naam='heeftVerlorenVoerbuis',
                                                   label='heeft verloren voerbuis',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.heeftVerlorenVoerbuis',
                                                   definition='Aanduiding of de heipaal een verloren voerbuis heeft.',
                                                   owner=self)

        self._nuttigeLengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='nuttigeLengte',
                                           label='nuttige lengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.nuttigeLengte',
                                           definition='Afstand gemeten, in meter, volgens de as van de heipaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het bovenpeil) en het aanzetpeil (definitief funderingspeil).',
                                           owner=self)

        self._typeSchacht = OTLAttribuut(field=KlTypeSchachtHeipaal,
                                         naam='typeSchacht',
                                         label='type schacht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.typeSchacht',
                                         definition='De soort schacht van de heipaal.',
                                         owner=self)

    @property
    def diameterPaalschacht(self) -> KwantWrdInMillimeterWaarden:
        """Doorsnede in millimeter van de schacht van de paal."""
        return self._diameterPaalschacht.get_waarde()

    @diameterPaalschacht.setter
    def diameterPaalschacht(self, value):
        self._diameterPaalschacht.set_waarde(value, owner=self)

    @property
    def heeftVerbredeVoet(self) -> bool:
        """Geeft aan of de voet breder is gemaakt, al dan niet."""
        return self._heeftVerbredeVoet.get_waarde()

    @heeftVerbredeVoet.setter
    def heeftVerbredeVoet(self, value):
        self._heeftVerbredeVoet.set_waarde(value, owner=self)

    @property
    def heeftVerlorenVoerbuis(self) -> bool:
        """Aanduiding of de heipaal een verloren voerbuis heeft."""
        return self._heeftVerlorenVoerbuis.get_waarde()

    @heeftVerlorenVoerbuis.setter
    def heeftVerlorenVoerbuis(self, value):
        self._heeftVerlorenVoerbuis.set_waarde(value, owner=self)

    @property
    def nuttigeLengte(self) -> KwantWrdInMeterWaarden:
        """Afstand gemeten, in meter, volgens de as van de heipaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het bovenpeil) en het aanzetpeil (definitief funderingspeil)."""
        return self._nuttigeLengte.get_waarde()

    @nuttigeLengte.setter
    def nuttigeLengte(self, value):
        self._nuttigeLengte.set_waarde(value, owner=self)

    @property
    def typeSchacht(self) -> str:
        """De soort schacht van de heipaal."""
        return self._typeSchacht.get_waarde()

    @typeSchacht.setter
    def typeSchacht(self, value):
        self._typeSchacht.set_waarde(value, owner=self)
