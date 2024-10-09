# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlMateriaalLoopvloer import KlMateriaalLoopvloer
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInKiloNewtonPerVierkanteMeter import KwantWrdInKiloNewtonPerVierkanteMeter, KwantWrdInKiloNewtonPerVierkanteMeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Loopvloer(AanhorigheidKoker, AanhorigheidSluisStuw, AIMNaamObject, VlakGeometrie):
    """Een vloer die ligt op,in of nabij een constructie die wordt gebruikt om deze op een veilige manier te betreden of bereiken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning', direction='u')  # u = unidirectional

        self._isDemonteerbaar = OTLAttribuut(field=BooleanField,
                                             naam='isDemonteerbaar',
                                             label='is demonteerbaar',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer.isDemonteerbaar',
                                             definition='Geeft aan of de loopvloer al dan niet demonteerbaar is.',
                                             owner=self)

        self._karakteristiekeGebruiksbelasting = OTLAttribuut(field=KwantWrdInKiloNewtonPerVierkanteMeter,
                                                              naam='karakteristiekeGebruiksbelasting',
                                                              label='karakteristieke gebruiksbelasting',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer.karakteristiekeGebruiksbelasting',
                                                              definition='De karakteristieke gebruiksbelasting.',
                                                              owner=self)

        self._karakteristiekePuntbelasting = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                          naam='karakteristiekePuntbelasting',
                                                          label='karakteristieke puntbelasting',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer.karakteristiekePuntbelasting',
                                                          definition='De karakteristieke puntbelasting.',
                                                          owner=self)

        self._materiaal = OTLAttribuut(field=KlMateriaalLoopvloer,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer.materiaal',
                                       definition='De mogelijke materialen van een loopvloer.',
                                       owner=self)

        self._nuttigeBreedte = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='nuttigeBreedte',
                                            label='nuttige breedte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer.nuttigeBreedte',
                                            definition='De nuttige breedte van de loopvloer zoals bepaald door de smalste breedte.',
                                            owner=self)

    @property
    def isDemonteerbaar(self) -> bool:
        """Geeft aan of de loopvloer al dan niet demonteerbaar is."""
        return self._isDemonteerbaar.get_waarde()

    @isDemonteerbaar.setter
    def isDemonteerbaar(self, value):
        self._isDemonteerbaar.set_waarde(value, owner=self)

    @property
    def karakteristiekeGebruiksbelasting(self) -> KwantWrdInKiloNewtonPerVierkanteMeterWaarden:
        """De karakteristieke gebruiksbelasting."""
        return self._karakteristiekeGebruiksbelasting.get_waarde()

    @karakteristiekeGebruiksbelasting.setter
    def karakteristiekeGebruiksbelasting(self, value):
        self._karakteristiekeGebruiksbelasting.set_waarde(value, owner=self)

    @property
    def karakteristiekePuntbelasting(self) -> KwantWrdInKiloNewtonWaarden:
        """De karakteristieke puntbelasting."""
        return self._karakteristiekePuntbelasting.get_waarde()

    @karakteristiekePuntbelasting.setter
    def karakteristiekePuntbelasting(self, value):
        self._karakteristiekePuntbelasting.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """De mogelijke materialen van een loopvloer."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def nuttigeBreedte(self) -> KwantWrdInMeterWaarden:
        """De nuttige breedte van de loopvloer zoals bepaald door de smalste breedte."""
        return self._nuttigeBreedte.get_waarde()

    @nuttigeBreedte.setter
    def nuttigeBreedte(self, value):
        self._nuttigeBreedte.set_waarde(value, owner=self)
