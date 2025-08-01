# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabelgeleiding import Kabelgeleiding
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from ...Datatypes.KwantWrdInKilogramPerMeter import KwantWrdInKilogramPerMeter, KwantWrdInKilogramPerMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelgoot(Kabelgeleiding):
    """Een inrichting die ervoor zorgt dat een kabel beschermd is tegen beschadiging en/of op een gecontroleerde plaats blijft hangen of liggen. Een kabelgoot is doorgaans een halfopen constructie. Er bestaan ook kabelgoten die door een deksel gesloten kunnen worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding', direction='i')  # i = direction: incoming

        self._draagvermogen = OTLAttribuut(field=KwantWrdInKilogramPerMeter,
                                           naam='draagvermogen',
                                           label='draagvermogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot.draagvermogen',
                                           definition='Het draagvermogen per meter om kabels te ondersteunen.',
                                           owner=self)

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
    def draagvermogen(self) -> KwantWrdInKilogramPerMeterWaarden:
        """Het draagvermogen per meter om kabels te ondersteunen."""
        return self._draagvermogen.get_waarde()

    @draagvermogen.setter
    def draagvermogen(self, value):
        self._draagvermogen.set_waarde(value, owner=self)

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
