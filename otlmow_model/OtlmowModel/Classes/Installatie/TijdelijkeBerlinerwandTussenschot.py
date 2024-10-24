# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalTussenschotBerlinerwand import KlMateriaalTussenschotBerlinerwand
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class TijdelijkeBerlinerwandTussenschot(AIMNaamObject, LijnGeometrie):
    """Het tussenschot (plaat of plank tussen profielen) voor een tijdelijke berlinerwand. Om een berlinerwand te definiëren die permanent in de grond blijft, moeten de specifieke (materiaal)onderdelen gebruikt worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeBerlinerwandTussenschot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand', direction='o')  # o = direction: outgoing

        self._aanzetpeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                        naam='aanzetpeil',
                                        label='aanzetpeil',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeBerlinerwandTussenschot.aanzetpeil',
                                        definition='Aanzetpeil van het element in mTaw.',
                                        owner=self)

        self._materiaal = OTLAttribuut(field=KlMateriaalTussenschotBerlinerwand,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeBerlinerwandTussenschot.materiaal',
                                       definition='Het materiaal voor het tijdelijke tussenschot.',
                                       owner=self)

    @property
    def aanzetpeil(self) -> KwantWrdInMeterTAWWaarden:
        """Aanzetpeil van het element in mTaw."""
        return self._aanzetpeil.get_waarde()

    @aanzetpeil.setter
    def aanzetpeil(self, value):
        self._aanzetpeil.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal voor het tijdelijke tussenschot."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
