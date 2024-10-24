# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.OntwerpwaterstandStreefpeil import OntwerpwaterstandStreefpeil
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stuw(OntwerpwaterstandStreefpeil, AIMNaamObject):
    """Beweegbare of vaste waterbouwkundige constructie tussen twee waterlichamen met als doel het waterpeil/waterdebiet te reguleren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie', direction='i')  # i = direction: incoming

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuw.breedte',
                                     definition='De afstand tussen de dagkanten van de vaste constructie.',
                                     owner=self)

        self._isRegelbaarheidAanwezig = OTLAttribuut(field=BooleanField,
                                                     naam='isRegelbaarheidAanwezig',
                                                     label='is regelbaarheid aanwezig',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuw.isRegelbaarheidAanwezig',
                                                     definition='Geeft aan of er regelbaarheid aanwezig is.',
                                                     owner=self)

        self._maximaalStuwPeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                              naam='maximaalStuwPeil',
                                              label='onderkant hoogste schutpeil',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuw.maximaalStuwPeil',
                                              definition='Het maximale waterpeil dat kan worden bereikt aan de stroomopwaartse zijde van de stuw, gemeten vanaf de onderkant van de stuwconstructie.',
                                              owner=self)

    @property
    def breedte(self) -> KwantWrdInMeterWaarden:
        """De afstand tussen de dagkanten van de vaste constructie."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def isRegelbaarheidAanwezig(self) -> bool:
        """Geeft aan of er regelbaarheid aanwezig is."""
        return self._isRegelbaarheidAanwezig.get_waarde()

    @isRegelbaarheidAanwezig.setter
    def isRegelbaarheidAanwezig(self, value):
        self._isRegelbaarheidAanwezig.set_waarde(value, owner=self)

    @property
    def maximaalStuwPeil(self) -> KwantWrdInMeterTAWWaarden:
        """Het maximale waterpeil dat kan worden bereikt aan de stroomopwaartse zijde van de stuw, gemeten vanaf de onderkant van de stuwconstructie."""
        return self._maximaalStuwPeil.get_waarde()

    @maximaalStuwPeil.setter
    def maximaalStuwPeil(self, value):
        self._maximaalStuwPeil.set_waarde(value, owner=self)
