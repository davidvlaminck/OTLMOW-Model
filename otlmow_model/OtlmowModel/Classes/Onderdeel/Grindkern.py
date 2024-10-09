# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInKilogramPerKubiekeMeter import KwantWrdInKilogramPerKubiekeMeter, KwantWrdInKilogramPerKubiekeMeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grindkern(Funderingspaal):
    """In de grond gevormd of vrijgestort cilindrisch element uit grind dat door heien of trillen wordt verdicht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindkern'
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

        self._hOhAfstand = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='hOhAfstand',
                                        label='h.o.h. afstand',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindkern.hOhAfstand',
                                        definition='Hart op hart afstand tussen elementen',
                                        owner=self)

        self._heeftCementstabilisatie = OTLAttribuut(field=BooleanField,
                                                     naam='heeftCementstabilisatie',
                                                     label='heeft cementstabilisatie',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindkern.heeftCementstabilisatie',
                                                     definition='Geeft aan of de grindkern/grindpaal een gedeeltelijke of volledige cementstabilisatie heeft, al dan niet.',
                                                     owner=self)

        self._hoeveelheidCement = OTLAttribuut(field=KwantWrdInKilogramPerKubiekeMeter,
                                               naam='hoeveelheidCement',
                                               label='hoeveelheid cement',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindkern.hoeveelheidCement',
                                               definition='Hoeveelheid cement per kubieke meter die gemend wordt met de grind.',
                                               owner=self)

        self._nuttigeLengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='nuttigeLengte',
                                           label='nuttige lengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindkern.nuttigeLengte',
                                           definition='De lengte, uitgedrukt in meter, van het aanzetpeil tot aan de funderingsaanzet van de buisleiding of constructie.',
                                           owner=self)

    @property
    def hOhAfstand(self) -> KwantWrdInMeterWaarden:
        """Hart op hart afstand tussen elementen"""
        return self._hOhAfstand.get_waarde()

    @hOhAfstand.setter
    def hOhAfstand(self, value):
        self._hOhAfstand.set_waarde(value, owner=self)

    @property
    def heeftCementstabilisatie(self) -> bool:
        """Geeft aan of de grindkern/grindpaal een gedeeltelijke of volledige cementstabilisatie heeft, al dan niet."""
        return self._heeftCementstabilisatie.get_waarde()

    @heeftCementstabilisatie.setter
    def heeftCementstabilisatie(self, value):
        self._heeftCementstabilisatie.set_waarde(value, owner=self)

    @property
    def hoeveelheidCement(self) -> KwantWrdInKilogramPerKubiekeMeterWaarden:
        """Hoeveelheid cement per kubieke meter die gemend wordt met de grind."""
        return self._hoeveelheidCement.get_waarde()

    @hoeveelheidCement.setter
    def hoeveelheidCement(self, value):
        self._hoeveelheidCement.set_waarde(value, owner=self)

    @property
    def nuttigeLengte(self) -> KwantWrdInMeterWaarden:
        """De lengte, uitgedrukt in meter, van het aanzetpeil tot aan de funderingsaanzet van de buisleiding of constructie."""
        return self._nuttigeLengte.get_waarde()

    @nuttigeLengte.setter
    def nuttigeLengte(self, value):
        self._nuttigeLengte.set_waarde(value, owner=self)
