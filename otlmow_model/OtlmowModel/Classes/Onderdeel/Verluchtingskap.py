# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verluchtingskap(AIMObject, PuntGeometrie):
    """Onderdeel dat tot doel heeft natuurlijke verluchting te bekomen in een gesloten ruimte zodat er geen opeenstapeling is van giftige stoffen en bescherming biedt tegen regen en vuil."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verluchtingskap'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ventilatiekanaal', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing

        self._diameterAansluiting = OTLAttribuut(field=KwantWrdInMillimeter,
                                                 naam='diameterAansluiting',
                                                 label='diameter aansluiting',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verluchtingskap.diameterAansluiting',
                                                 definition='De diameter van de verluchtingskap voor de aansluiting van een verluchtingsbuis of -leiding.',
                                                 owner=self)

    @property
    def diameterAansluiting(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de verluchtingskap voor de aansluiting van een verluchtingsbuis of -leiding."""
        return self._diameterAansluiting.get_waarde()

    @diameterAansluiting.setter
    def diameterAansluiting(self, value):
        self._diameterAansluiting.set_waarde(value, owner=self)
