# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voetbocht(LinkendElement, PuntGeometrie):
    """Een leiding die een bocht vertoont. Het ene deel van de leiding is rechtstreeks aangesloten op het pomplichaam, staat horizontaal en steunt op de grond. Het andere deel is verticaal opgesteld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voetbocht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pompgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._diameterVerticaal = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='diameterVerticaal',
                                               label='diameter verticaal',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voetbocht.diameterVerticaal',
                                               definition='De diameter van het deel van de leiding dat verticaal is opgesteld.',
                                               owner=self)

    @property
    def diameterVerticaal(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van het deel van de leiding dat verticaal is opgesteld."""
        return self._diameterVerticaal.get_waarde()

    @diameterVerticaal.setter
    def diameterVerticaal(self, value):
        self._diameterVerticaal.set_waarde(value, owner=self)
