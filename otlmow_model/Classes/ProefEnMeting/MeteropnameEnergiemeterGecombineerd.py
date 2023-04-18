# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ProefEnMeting.MeteropnameEnergiemeter import MeteropnameEnergiemeter
from otlmow_model.Datatypes.KwantWrdInKiloWatt import KwantWrdInKiloWatt, KwantWrdInKiloWattWaarden
from otlmow_model.Datatypes.KwantWrdInkVARh import KwantWrdInkVARh, KwantWrdInkVARhWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class MeteropnameEnergiemeterGecombineerd(MeteropnameEnergiemeter):
    """Resultaten van een meteropname van een gecombineerde energiemeter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._meterstandPiek = OTLAttribuut(field=KwantWrdInKiloWatt,
                                            naam='meterstandPiek',
                                            label='meterstand piek',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandPiek',
                                            definition='De stand van de energiemeter waarmee het piekvermogen gemeten wordt.',
                                            owner=self)

        self._meterstandReactiefVermogenDag = OTLAttribuut(field=KwantWrdInkVARh,
                                                           naam='meterstandReactiefVermogenDag',
                                                           label='dag-meterstand reactief vermogen',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandReactiefVermogenDag',
                                                           definition='De stand van de dag-energiemeter waarmee het reactief vermogen gemeten wordt.',
                                                           owner=self)

        self._meterstandReactiefVermogenNacht = OTLAttribuut(field=KwantWrdInkVARh,
                                                             naam='meterstandReactiefVermogenNacht',
                                                             label='nacht-meterstand reactief vermogen',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandReactiefVermogenNacht',
                                                             definition='De stand van de nacht-energiemeter waarmee het reactief vermogen gemeten wordt.',
                                                             owner=self)

    @property
    def meterstandPiek(self) -> KwantWrdInKiloWattWaarden:
        """De stand van de energiemeter waarmee het piekvermogen gemeten wordt."""
        return self._meterstandPiek.get_waarde()

    @meterstandPiek.setter
    def meterstandPiek(self, value):
        self._meterstandPiek.set_waarde(value, owner=self)

    @property
    def meterstandReactiefVermogenDag(self) -> KwantWrdInkVARhWaarden:
        """De stand van de dag-energiemeter waarmee het reactief vermogen gemeten wordt."""
        return self._meterstandReactiefVermogenDag.get_waarde()

    @meterstandReactiefVermogenDag.setter
    def meterstandReactiefVermogenDag(self, value):
        self._meterstandReactiefVermogenDag.set_waarde(value, owner=self)

    @property
    def meterstandReactiefVermogenNacht(self) -> KwantWrdInkVARhWaarden:
        """De stand van de nacht-energiemeter waarmee het reactief vermogen gemeten wordt."""
        return self._meterstandReactiefVermogenNacht.get_waarde()

    @meterstandReactiefVermogenNacht.setter
    def meterstandReactiefVermogenNacht(self, value):
        self._meterstandReactiefVermogenNacht.set_waarde(value, owner=self)
