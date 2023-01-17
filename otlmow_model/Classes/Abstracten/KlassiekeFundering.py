# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from otlmow_model.Classes.Abstracten.Fundering import Fundering
from otlmow_model.Datatypes.DtuAfmetingGrondvlak import DtuAfmetingGrondvlak, DtuAfmetingGrondvlakWaarden
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class KlassiekeFundering(Fundering, BetonnenConstructieElement):
    """Abstracte voor ondiepe en halfdiepe funderingen. Fundering op staal en op putten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlassiekeFundering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Fundering.__init__(self)
        BetonnenConstructieElement.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')

        self._funderingshoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                              naam='funderingshoogte',
                                              label='funderingshoogte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlassiekeFundering.funderingshoogte',
                                              definition='De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering.',
                                              owner=self)

        self._grondvlakAfmeting = OTLAttribuut(field=DtuAfmetingGrondvlak,
                                               naam='grondvlakAfmeting',
                                               label='grondvlakafmeting',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlassiekeFundering.grondvlakAfmeting',
                                               definition='De afmetingen van het (grond)vlak, van de bovenkant van de fundering, volgens de vorm.',
                                               owner=self)

    @property
    def funderingshoogte(self) -> KwantWrdInCentimeterWaarden:
        """De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering."""
        return self._funderingshoogte.get_waarde()

    @funderingshoogte.setter
    def funderingshoogte(self, value):
        self._funderingshoogte.set_waarde(value, owner=self)

    @property
    def grondvlakAfmeting(self) -> DtuAfmetingGrondvlakWaarden:
        """De afmetingen van het (grond)vlak, van de bovenkant van de fundering, volgens de vorm."""
        return self._grondvlakAfmeting.get_waarde()

    @grondvlakAfmeting.setter
    def grondvlakAfmeting(self, value):
        self._grondvlakAfmeting.set_waarde(value, owner=self)
