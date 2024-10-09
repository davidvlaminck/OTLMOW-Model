# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Persleiding import Persleiding
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInBar import KwantWrdInBar, KwantWrdInBarWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandleiding(Persleiding):
    """Segment uit de leiding die water aanvoert voor het blussen van een brand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i', deprecated='2.8.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._isGeisoleerd = OTLAttribuut(field=BooleanField,
                                          naam='isGeisoleerd',
                                          label='is geïsoleerd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding.isGeisoleerd',
                                          definition='Geeft aan of de brandleiding voorzien is van eigen isolatie.',
                                          owner=self)

        self._leidingdruk = OTLAttribuut(field=KwantWrdInBar,
                                         naam='leidingdruk',
                                         label='leidingdruk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding.leidingdruk',
                                         definition='De vastgelegde druk die moet voorzien worden op de leiding in functie van de aanvoer van bluswater.',
                                         owner=self)

    @property
    def isGeisoleerd(self) -> bool:
        """Geeft aan of de brandleiding voorzien is van eigen isolatie."""
        return self._isGeisoleerd.get_waarde()

    @isGeisoleerd.setter
    def isGeisoleerd(self, value):
        self._isGeisoleerd.set_waarde(value, owner=self)

    @property
    def leidingdruk(self) -> KwantWrdInBarWaarden:
        """De vastgelegde druk die moet voorzien worden op de leiding in functie van de aanvoer van bluswater."""
        return self._leidingdruk.get_waarde()

    @leidingdruk.setter
    def leidingdruk(self, value):
        self._leidingdruk.set_waarde(value, owner=self)
