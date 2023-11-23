# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from ...Datatypes.DtcConstructiestaalspecificaties import DtcConstructiestaalspecificaties, DtcConstructiestaalspecificatiesWaarden
from ...Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenConstructieElement(ABC):
    """Bundeling van gemeenschappelijke eigenschappen van stalen constructie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._staalspecificaties = OTLAttribuut(field=DtcConstructiestaalspecificaties,
                                                naam='staalspecificaties',
                                                label='staalspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement.staalspecificaties',
                                                definition='Eigenschappen van het gebruikte constructiestaal.',
                                                owner=self)

        self._totaalGewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                           naam='totaalGewicht',
                                           label='totaal gewicht',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement.totaalGewicht',
                                           definition='Een kwantitatieve waarde in kilogram van het totale stalen element.',
                                           owner=self)

    @property
    def staalspecificaties(self) -> DtcConstructiestaalspecificatiesWaarden:
        """Eigenschappen van het gebruikte constructiestaal."""
        return self._staalspecificaties.get_waarde()

    @staalspecificaties.setter
    def staalspecificaties(self, value):
        self._staalspecificaties.set_waarde(value, owner=self)

    @property
    def totaalGewicht(self) -> KwantWrdInKilogramWaarden:
        """Een kwantitatieve waarde in kilogram van het totale stalen element."""
        return self._totaalGewicht.get_waarde()

    @totaalGewicht.setter
    def totaalGewicht(self, value):
        self._totaalGewicht.set_waarde(value, owner=self)
