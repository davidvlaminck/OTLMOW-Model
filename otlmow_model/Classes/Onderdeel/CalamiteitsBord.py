# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from otlmow_model.Datatypes.KlCalamiteitsbordType import KlCalamiteitsbordType
from otlmow_model.Datatypes.KlCalamiteitsbordVorm import KlCalamiteitsbordVorm


# Generated with OTLClassCreator. To modify: extend, do not edit
class CalamiteitsBord(RetroreflecterendVerkeersbord):
    """De aanwijzingsborden ter plaatse van een startpunt, een aantakpunt, een wissel- of koppelpunt van een omleggingsroute bij calamiteiten zijn geïntegreerd in een één-bordsysteem met een scharnierende plaat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._calamiteitsbordType = OTLAttribuut(field=KlCalamiteitsbordType,
                                                 naam='calamiteitsbordType',
                                                 label='calamiteitsbord type',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord.calamiteitsbordType',
                                                 definition='Het type van calamiteitsbord (bv. draaiend of dragend).',
                                                 owner=self)

        self._vorm = OTLAttribuut(field=KlCalamiteitsbordVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord.vorm',
                                  definition='De vorm van het calamiteitsbord.',
                                  owner=self)

    @property
    def calamiteitsbordType(self) -> str:
        """Het type van calamiteitsbord (bv. draaiend of dragend)."""
        return self._calamiteitsbordType.get_waarde()

    @calamiteitsbordType.setter
    def calamiteitsbordType(self, value):
        self._calamiteitsbordType.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """De vorm van het calamiteitsbord."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
