# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Datatypes.KlTerugslagklepType import KlTerugslagklepType
from ...Datatypes.KlTsklepAfsluiterMateriaal import KlTsklepAfsluiterMateriaal
from ...Datatypes.KlVormTerugslagklep import KlVormTerugslagklep
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Terugslagklep(LinkendElement, PuntGeometrie):
    """Een terugslagklep is een klep die dient om water, vloeistof, granulaat, poeder of gas in één richting door te laten. Meestal duwt het medium de klep bij het heenstromen open en sluit een veer of de zwaartekracht de klep."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WaterdoorvoerendeDuiker', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._breedteOpening = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='breedteOpening',
                                            label='breedte opening',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.breedteOpening',
                                            definition='Breedte van de opening die door de terugslagklep wordt afgesloten in millimeter.',
                                            owner=self)

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.diameter',
                                      definition='De diameter van de terugslagklep in millimeter.',
                                      owner=self)

        self._hoogteOpening = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='hoogteOpening',
                                           label='hoogte opening',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.hoogteOpening',
                                           definition='De hoogte van de opening die door de terugslagklep wordt afgesloten in millimeter.',
                                           owner=self)

        self._materiaal = OTLAttribuut(field=KlTsklepAfsluiterMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.materiaal',
                                       definition='Het materiaal waaruit de terugslagklep is vervaardigd.',
                                       owner=self)

        self._peil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                  naam='peil',
                                  label='peil',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.peil',
                                  definition='Niveau van de doorlaatopening van de terugslagklep uitgedrukt in meter-TAW.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlTerugslagklepType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.type',
                                  definition='Bepaalt het type van terugslagklep.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=KlVormTerugslagklep,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.vorm',
                                  definition='De vorm van de terugslagklep.',
                                  owner=self)

    @property
    def breedteOpening(self) -> KwantWrdInMillimeterWaarden:
        """Breedte van de opening die door de terugslagklep wordt afgesloten in millimeter."""
        return self._breedteOpening.get_waarde()

    @breedteOpening.setter
    def breedteOpening(self, value):
        self._breedteOpening.set_waarde(value, owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de terugslagklep in millimeter."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def hoogteOpening(self) -> KwantWrdInMillimeterWaarden:
        """De hoogte van de opening die door de terugslagklep wordt afgesloten in millimeter."""
        return self._hoogteOpening.get_waarde()

    @hoogteOpening.setter
    def hoogteOpening(self, value):
        self._hoogteOpening.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de terugslagklep is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def peil(self) -> KwantWrdInMeterTAWWaarden:
        """Niveau van de doorlaatopening van de terugslagklep uitgedrukt in meter-TAW."""
        return self._peil.get_waarde()

    @peil.setter
    def peil(self, value):
        self._peil.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Bepaalt het type van terugslagklep."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """De vorm van de terugslagklep."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
