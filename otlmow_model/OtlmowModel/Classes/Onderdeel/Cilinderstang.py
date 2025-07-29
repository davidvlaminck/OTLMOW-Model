# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlStangHydraulischeCilinderBekleding import KlStangHydraulischeCilinderBekleding
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cilinderstang(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Het onderdeel van de cilinder die in en uit de mantel schuift."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CilinderStangkop', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderzuiger', direction='u')  # u = unidirectional

        self._bekleding = OTLAttribuut(field=KlStangHydraulischeCilinderBekleding,
                                       naam='bekleding',
                                       label='bekleding',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang.bekleding',
                                       definition='De bekleding van de stang.',
                                       owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang.lengte',
                                    definition='De lengte van de hydraulische stang, uitgedrukt in millimeter. Indien de cilinder een tegenstang heeft, dan wordt die lengte erbij opgeteld.',
                                    owner=self)

        self._stangdiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='stangdiameter',
                                           label='stangdiameter',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang.stangdiameter',
                                           definition='De buitendiameter van de stang, uitgedrukt in millimeter.',
                                           owner=self)

    @property
    def bekleding(self) -> str:
        """De bekleding van de stang."""
        return self._bekleding.get_waarde()

    @bekleding.setter
    def bekleding(self, value):
        self._bekleding.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de hydraulische stang, uitgedrukt in millimeter. Indien de cilinder een tegenstang heeft, dan wordt die lengte erbij opgeteld."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def stangdiameter(self) -> KwantWrdInMillimeterWaarden:
        """De buitendiameter van de stang, uitgedrukt in millimeter."""
        return self._stangdiameter.get_waarde()

    @stangdiameter.setter
    def stangdiameter(self, value):
        self._stangdiameter.set_waarde(value, owner=self)
