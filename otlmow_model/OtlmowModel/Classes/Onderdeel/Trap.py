# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalTrap import KlMateriaalTrap
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trap(AanhorighedenBrug, AanhorigheidKoker, AanhorigheidSluisStuw, AIMNaamObject, VlakGeometrie):
    """Een constructie die een verbinding vormt tussen twee op verschillend niveau gelegen vlakken. Bestaande uit armen en bordessen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trap'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', direction='u')  # u = unidirectional

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trap.lengte',
                                    definition='De lengte van de trap in de lopende meters die trap aflegt.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlMateriaalTrap,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trap.materiaal',
                                       definition='Het materiaal waaruit de trap is vervaardigd.',
                                       owner=self)

        self._niveauverschil = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='niveauverschil',
                                            label='niveauverschil',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trap.niveauverschil',
                                            definition='Verschil in hoogte tussen 2 niveaus.',
                                            owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de trap in de lopende meters die trap aflegt."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de trap is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def niveauverschil(self) -> KwantWrdInMeterWaarden:
        """Verschil in hoogte tussen 2 niveaus."""
        return self._niveauverschil.get_waarde()

    @niveauverschil.setter
    def niveauverschil(self, value):
        self._niveauverschil.set_waarde(value, owner=self)
