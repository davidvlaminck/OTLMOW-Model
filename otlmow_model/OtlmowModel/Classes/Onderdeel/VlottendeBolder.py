# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VlottendeBolder(AanhorigheidSluisStuw, AIMNaamObject, PuntGeometrie):
    """De vlottende bolder is een bolder die meebeweegt met het veranderend waterniveau."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlottendeBolder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftStopper = OTLAttribuut(field=BooleanField,
                                          naam='heeftStopper',
                                          label='heeft stopper',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlottendeBolder.heeftStopper',
                                          definition='Geeft aan of er een stopper aanwezig is.',
                                          owner=self)

        self._hoogteTovWaterlijn = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='hoogteTovWaterlijn',
                                                label='hoogte t.o.v. waterlijn',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlottendeBolder.hoogteTovWaterlijn',
                                                definition='Hoogte boven waterlijn.',
                                                owner=self)

        self._materiaalVlottendeBolder = OTLAttribuut(field=StringField,
                                                      naam='materiaalVlottendeBolder',
                                                      label='materiaal vlottende bolder',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlottendeBolder.materiaalVlottendeBolder',
                                                      definition='Het gebruikte materiaal voor de vlottende bolder (Bijv: S355,..).',
                                                      owner=self)

        self._maximaleTroskracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                naam='maximaleTroskracht',
                                                label='maximale troskracht',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlottendeBolder.maximaleTroskracht',
                                                definition='De maximale troskracht, uitgedrukt in kN (Karakteristieke waarde).',
                                                owner=self)

    @property
    def heeftStopper(self) -> bool:
        """Geeft aan of er een stopper aanwezig is."""
        return self._heeftStopper.get_waarde()

    @heeftStopper.setter
    def heeftStopper(self, value):
        self._heeftStopper.set_waarde(value, owner=self)

    @property
    def hoogteTovWaterlijn(self) -> KwantWrdInMeterWaarden:
        """Hoogte boven waterlijn."""
        return self._hoogteTovWaterlijn.get_waarde()

    @hoogteTovWaterlijn.setter
    def hoogteTovWaterlijn(self, value):
        self._hoogteTovWaterlijn.set_waarde(value, owner=self)

    @property
    def materiaalVlottendeBolder(self) -> str:
        """Het gebruikte materiaal voor de vlottende bolder (Bijv: S355,..)."""
        return self._materiaalVlottendeBolder.get_waarde()

    @materiaalVlottendeBolder.setter
    def materiaalVlottendeBolder(self, value):
        self._materiaalVlottendeBolder.set_waarde(value, owner=self)

    @property
    def maximaleTroskracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De maximale troskracht, uitgedrukt in kN (Karakteristieke waarde)."""
        return self._maximaleTroskracht.get_waarde()

    @maximaleTroskracht.setter
    def maximaleTroskracht(self, value):
        self._maximaleTroskracht.set_waarde(value, owner=self)
