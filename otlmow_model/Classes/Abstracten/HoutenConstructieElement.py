# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Datatypes.DtcHoutspecificaties import DtcHoutspecificaties, DtcHoutspecificatiesWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoutenConstructieElement(LijnGeometrie):
    """Bundeling van gemeenschappelijke eigenschappen van houten constructie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutenConstructieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._houtspecificaties = OTLAttribuut(field=DtcHoutspecificaties,
                                               naam='houtspecificaties',
                                               label='houtspecificaties',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutenConstructieElement.houtspecificaties',
                                               definition='De eigenschappen van het gebruikte hout.',
                                               owner=self)

    @property
    def houtspecificaties(self) -> DtcHoutspecificatiesWaarden:
        """De eigenschappen van het gebruikte hout."""
        return self._houtspecificaties.get_waarde()

    @houtspecificaties.setter
    def houtspecificaties(self, value):
        self._houtspecificaties.set_waarde(value, owner=self)
