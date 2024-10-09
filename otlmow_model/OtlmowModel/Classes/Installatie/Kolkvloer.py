# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kolkvloer(AIMNaamObject, VlakGeometrie):
    """De vloer van de kolk. De vloer dient opgesplitst te worden per moot, elke moot heeft een aparte vloer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerlaag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sluisvloertegel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen', direction='i')  # i = direction: incoming

        self._bodemPeilKolkvloer = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                naam='bodemPeilKolkvloer',
                                                label='bodempeil kolkvloer',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer.bodemPeilKolkvloer',
                                                definition='Het peil van de bovenkant van de vloer',
                                                owner=self)

        self._detailPlanDrainageOpeningen = OTLAttribuut(field=DtcDocument,
                                                         naam='detailPlanDrainageOpeningen',
                                                         label='detailplan drainageopeningen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer.detailPlanDrainageOpeningen',
                                                         definition='Het detailplan van de drainageopeningen, inclusief de filterconstructie, van de vloer.',
                                                         owner=self)

        self._isConstructief = OTLAttribuut(field=BooleanField,
                                            naam='isConstructief',
                                            label='is constructief',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer.isConstructief',
                                            definition='Geeft aan of de kolkvloer al dan niet constructief is.',
                                            owner=self)

        self._isDrainerend = OTLAttribuut(field=BooleanField,
                                          naam='isDrainerend',
                                          label='is drainerend',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer.isDrainerend',
                                          definition='Geeft aan of de kolkvloer al dan niet drainerend is.',
                                          owner=self)

    @property
    def bodemPeilKolkvloer(self) -> KwantWrdInMeterTAWWaarden:
        """Het peil van de bovenkant van de vloer"""
        return self._bodemPeilKolkvloer.get_waarde()

    @bodemPeilKolkvloer.setter
    def bodemPeilKolkvloer(self, value):
        self._bodemPeilKolkvloer.set_waarde(value, owner=self)

    @property
    def detailPlanDrainageOpeningen(self) -> DtcDocumentWaarden:
        """Het detailplan van de drainageopeningen, inclusief de filterconstructie, van de vloer."""
        return self._detailPlanDrainageOpeningen.get_waarde()

    @detailPlanDrainageOpeningen.setter
    def detailPlanDrainageOpeningen(self, value):
        self._detailPlanDrainageOpeningen.set_waarde(value, owner=self)

    @property
    def isConstructief(self) -> bool:
        """Geeft aan of de kolkvloer al dan niet constructief is."""
        return self._isConstructief.get_waarde()

    @isConstructief.setter
    def isConstructief(self, value):
        self._isConstructief.set_waarde(value, owner=self)

    @property
    def isDrainerend(self) -> bool:
        """Geeft aan of de kolkvloer al dan niet drainerend is."""
        return self._isDrainerend.get_waarde()

    @isDrainerend.setter
    def isDrainerend(self, value):
        self._isDrainerend.set_waarde(value, owner=self)
