# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Kabelgeleiding import Kabelgeleiding
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelgoot(Kabelgeleiding, VlakGeometrie):
    """Een inrichting die ervoor zorgt dat een kabel beschermd is tegen beschadiging en/of op een gecontroleerde plaats blijft hangen of liggen. Een kabelgoot is doorgaans een halfopen constructie. Er bestaan ook kabelgoten die door een deksel gesloten kunnen worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isGesloten = OTLAttribuut(field=BooleanField,
                                        naam='isGesloten',
                                        label='is gesloten',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot.isGesloten',
                                        definition='Geeft aan of de goot volledig gesloten is.',
                                        owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot.materiaal',
                                       definition='Het materiaal waaruit de kabelgoot (hoofdzakelijk) is gemaakt.',
                                       owner=self)

    @property
    def isGesloten(self) -> bool:
        """Geeft aan of de goot volledig gesloten is."""
        return self._isGesloten.get_waarde()

    @isGesloten.setter
    def isGesloten(self, value):
        self._isGesloten.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de kabelgoot (hoofdzakelijk) is gemaakt."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
