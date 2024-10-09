# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.Kast import Kast
from ...Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode
from ...Datatypes.KlBuitenkastVerfraaid import KlBuitenkastVerfraaid
from ...Datatypes.KwantWrdInJaar import KwantWrdInJaar, KwantWrdInJaarWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buitenkast(Kast):
    """Abstracte voor kasten die typisch buiten staan en daarom bestand moeten zijn tegen de elementen en verfraaiing kunnen krijgen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', direction='u')  # u = unidirectional

        self._ipKlasse = OTLAttribuut(field=KlAlgIngressProtectionCode,
                                      naam='ipKlasse',
                                      label='ingress protection klasse',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.ipKlasse',
                                      definition='De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.',
                                      owner=self)

        self._keuringsfrequentie = OTLAttribuut(field=KwantWrdInJaar,
                                                naam='keuringsfrequentie',
                                                label='keuringsfrequentie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.keuringsfrequentie',
                                                definition='Frequentie (in jaar) waarmee de kast moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle.',
                                                owner=self)

        self._verfraaid = OTLAttribuut(field=KlBuitenkastVerfraaid,
                                       naam='verfraaid',
                                       label='verfraaid',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.verfraaid',
                                       definition='Geeft aan of de wegkantkast voorzien van verfraaiing en of die al dan niet vergund is.',
                                       owner=self)

    @property
    def ipKlasse(self) -> str:
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
        return self._ipKlasse.get_waarde()

    @ipKlasse.setter
    def ipKlasse(self, value):
        self._ipKlasse.set_waarde(value, owner=self)

    @property
    def keuringsfrequentie(self) -> KwantWrdInJaarWaarden:
        """Frequentie (in jaar) waarmee de kast moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."""
        return self._keuringsfrequentie.get_waarde()

    @keuringsfrequentie.setter
    def keuringsfrequentie(self, value):
        self._keuringsfrequentie.set_waarde(value, owner=self)

    @property
    def verfraaid(self) -> str:
        """Geeft aan of de wegkantkast voorzien van verfraaiing en of die al dan niet vergund is."""
        return self._verfraaid.get_waarde()

    @verfraaid.setter
    def verfraaid(self, value):
        self._verfraaid.set_waarde(value, owner=self)
