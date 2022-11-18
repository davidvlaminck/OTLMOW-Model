# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.BegroeidVoorkomen import BegroeidVoorkomen
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcHoutigeAanleg import DtcHoutigeAanleg, DtcHoutigeAanlegWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoutigeVegetatie(BegroeidVoorkomen):
    """Houtige planten of houtige gewassen (planta lignosa) zijn overblijvende planten die worden gekenmerkt door secundaire diktegroei, waardoor de takken, stammen en wortels veel hout bevatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie')

        self._aanleg = OTLAttribuut(field=DtcHoutigeAanleg,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.aanleg',
                                    kardinaliteit_max='*',
                                    definition='De manier van aanplanten van de houtige vegetatie.',
                                    owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.hoogte',
                                    definition='De hoogte in meter gemeten van de stamvoet tot de top of bovenste snoeivlak van de houtige vegetatie. ',
                                    owner=self)

        self._isVrijUitgroeiend = OTLAttribuut(field=BooleanField,
                                               naam='isVrijUitgroeiend',
                                               label='is vrij uitgroeiend',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.isVrijUitgroeiend',
                                               definition='Geeft aan of de vegetatie of begroeiing al dan niet snoei vereist.',
                                               owner=self)

        self._knipoppervlak = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                           naam='knipoppervlak',
                                           label='knipoppervlak',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.knipoppervlak',
                                           definition='De afmeting van de begroeiing in vierkante meter dat geschoren moet worden.',
                                           owner=self)

    @property
    def aanleg(self) -> List[DtcHoutigeAanlegWaarden]:
        """De manier van aanplanten van de houtige vegetatie."""
        return self._aanleg.get_waarde()

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte in meter gemeten van de stamvoet tot de top of bovenste snoeivlak van de houtige vegetatie. """
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isVrijUitgroeiend(self) -> bool:
        """Geeft aan of de vegetatie of begroeiing al dan niet snoei vereist."""
        return self._isVrijUitgroeiend.get_waarde()

    @isVrijUitgroeiend.setter
    def isVrijUitgroeiend(self, value):
        self._isVrijUitgroeiend.set_waarde(value, owner=self)

    @property
    def knipoppervlak(self) -> KwantWrdInVierkanteMeterWaarden:
        """De afmeting van de begroeiing in vierkante meter dat geschoren moet worden."""
        return self._knipoppervlak.get_waarde()

    @knipoppervlak.setter
    def knipoppervlak(self, value):
        self._knipoppervlak.set_waarde(value, owner=self)
