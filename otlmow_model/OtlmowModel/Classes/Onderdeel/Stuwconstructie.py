# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stuwconstructie(AIMNaamObject, LijnGeometrie):
    """Een debietbegrenzende constructie waarbij het af te voeren water in zijn geheel door een (knijp)opening stroomt bij normale afvoer. Bij hevige regenval, wanneer de watertoevoer niet meer kan worden verwerkt, wordt een buffer opgebouwd tot aan de overstort."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuwconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='o')  # o = direction: outgoing

        self._breedteUitsparing = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='breedteUitsparing',
                                               label='breedte uitsparing',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuwconstructie.breedteUitsparing',
                                               definition='De breedte van het uitgesneden deel dat de functie heeft van overstort in millimeter.',
                                               owner=self)

        self._diameterKnijpopening = OTLAttribuut(field=KwantWrdInMillimeter,
                                                  naam='diameterKnijpopening',
                                                  label='diameter knijpopening',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuwconstructie.diameterKnijpopening',
                                                  definition='De diameter van de opening onderaan de cascade die zorgt voor een vertraagde waterafvoer bij hevige regenval of overvloedige toevoer van water in millimeter.',
                                                  owner=self)

        self._overstortpeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                           naam='overstortpeil',
                                           label='overstortpeil',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuwconstructie.overstortpeil',
                                           definition='Drempelpeil van de overstort. Uitgedrukt in meter-TAW gemeten in het midden van de drempel.',
                                           owner=self)

    @property
    def breedteUitsparing(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van het uitgesneden deel dat de functie heeft van overstort in millimeter."""
        return self._breedteUitsparing.get_waarde()

    @breedteUitsparing.setter
    def breedteUitsparing(self, value):
        self._breedteUitsparing.set_waarde(value, owner=self)

    @property
    def diameterKnijpopening(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de opening onderaan de cascade die zorgt voor een vertraagde waterafvoer bij hevige regenval of overvloedige toevoer van water in millimeter."""
        return self._diameterKnijpopening.get_waarde()

    @diameterKnijpopening.setter
    def diameterKnijpopening(self, value):
        self._diameterKnijpopening.set_waarde(value, owner=self)

    @property
    def overstortpeil(self) -> KwantWrdInMeterTAWWaarden:
        """Drempelpeil van de overstort. Uitgedrukt in meter-TAW gemeten in het midden van de drempel."""
        return self._overstortpeil.get_waarde()

    @overstortpeil.setter
    def overstortpeil(self, value):
        self._overstortpeil.set_waarde(value, owner=self)
