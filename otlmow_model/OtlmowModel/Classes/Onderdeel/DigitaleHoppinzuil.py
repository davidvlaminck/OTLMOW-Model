# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Hoppinzuil import Hoppinzuil
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class DigitaleHoppinzuil(Hoppinzuil):
    """Een digitale hoppinzuil is een interactieve informatiezuil die als doel heeft reizigers, al dan niet in realtime, te informeren over de vervoersmogelijkheden en diensten die op de locatie van de zuil voorhanden zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DigitaleHoppinzuil'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._schermHoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='schermHoogte',
                                          label='scherm hoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DigitaleHoppinzuil.schermHoogte',
                                          definition='De afstand tussen de onderste zijde van het scherm en het maaiveld in cm.',
                                          owner=self)

    @property
    def schermHoogte(self) -> KwantWrdInCentimeterWaarden:
        """De afstand tussen de onderste zijde van het scherm en het maaiveld in cm."""
        return self._schermHoogte.get_waarde()

    @schermHoogte.setter
    def schermHoogte(self, value):
        self._schermHoogte.set_waarde(value, owner=self)
