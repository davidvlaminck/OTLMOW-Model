# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Hoppinzuil import Hoppinzuil
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlHoppinzuilType import KlHoppinzuilType


# Generated with OTLClassCreator. To modify: extend, do not edit
class AnalogeHoppinzuil(Hoppinzuil):
    """Een hoppinzuil is een informatiezuil, die als doel heeft de reizigers te informeren omtrent de vervoersmogelijkheden en diensten die op de locatie van de zuil voorhanden zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel')

        self._macrokaart = OTLAttribuut(field=DtcDocument,
                                        naam='macrokaart',
                                        label='macrokaart',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil.macrokaart',
                                        definition='Cartografische weergave van het hoppinpunt en de omliggende hoppinpunten met daarop aangeduid de attractiepolen in de omgeving.',
                                        owner=self)

        self._microkaart = OTLAttribuut(field=DtcDocument,
                                        naam='microkaart',
                                        label='microkaart',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil.microkaart',
                                        definition='Cartografische weergave van het hoppinpunt en de omliggende straten met daarop de hoppinzuil, de verschillende beschikbare vervoersmodi en diensten aangeduid.',
                                        owner=self)

        self._type = OTLAttribuut(field=KlHoppinzuilType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil.type',
                                  definition='De mogelijke types van een analoge hoppinzuil.',
                                  owner=self)

    @property
    def macrokaart(self) -> DtcDocumentWaarden:
        """Cartografische weergave van het hoppinpunt en de omliggende hoppinpunten met daarop aangeduid de attractiepolen in de omgeving."""
        return self._macrokaart.get_waarde()

    @macrokaart.setter
    def macrokaart(self, value):
        self._macrokaart.set_waarde(value, owner=self)

    @property
    def microkaart(self) -> DtcDocumentWaarden:
        """Cartografische weergave van het hoppinpunt en de omliggende straten met daarop de hoppinzuil, de verschillende beschikbare vervoersmodi en diensten aangeduid."""
        return self._microkaart.get_waarde()

    @microkaart.setter
    def microkaart(self, value):
        self._microkaart.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De mogelijke types van een analoge hoppinzuil."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
