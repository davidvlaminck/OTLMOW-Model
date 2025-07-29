# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalTaatsmechanisme import KlMateriaalTaatsmechanisme
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taatspot(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een onderdeel van het taatsmechanisme dat bevestigd is aan het vast gedeelte van de bouwkundige constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme', direction='o')  # o = direction: outgoing

        self._materiaalTaatspot = OTLAttribuut(field=KlMateriaalTaatsmechanisme,
                                               naam='materiaalTaatspot',
                                               label='materiaal taatspot',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspot.materiaalTaatspot',
                                               definition='Het materiaal van de taatspot.',
                                               owner=self)

    @property
    def materiaalTaatspot(self) -> str:
        """Het materiaal van de taatspot."""
        return self._materiaalTaatspot.get_waarde()

    @materiaalTaatspot.setter
    def materiaalTaatspot(self, value):
        self._materiaalTaatspot.set_waarde(value, owner=self)
