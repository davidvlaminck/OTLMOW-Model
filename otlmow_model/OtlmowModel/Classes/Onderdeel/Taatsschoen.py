# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlMateriaalTaatsschoen import KlMateriaalTaatsschoen
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taatsschoen(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een onderdeel van het taatsmechanisme dat via een lager contact maakt met de taatspen en is bevestigd aan het beweegbare deel van een bouwkundige constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatsschoen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme', direction='o')  # o = direction: outgoing

        self._heeftDrukstoel = OTLAttribuut(field=BooleanField,
                                            naam='heeftDrukstoel',
                                            label='heeft drukstoel',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatsschoen.heeftDrukstoel',
                                            definition='Geeft aan of een drukstoel aanwezig is of niet.',
                                            owner=self)

        self._materiaalTaatsschoen = OTLAttribuut(field=KlMateriaalTaatsschoen,
                                                  naam='materiaalTaatsschoen',
                                                  label='materiaal taatsschoen',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatsschoen.materiaalTaatsschoen',
                                                  definition='Het materiaal van de taatsschoen.',
                                                  owner=self)

    @property
    def heeftDrukstoel(self) -> bool:
        """Geeft aan of een drukstoel aanwezig is of niet."""
        return self._heeftDrukstoel.get_waarde()

    @heeftDrukstoel.setter
    def heeftDrukstoel(self, value):
        self._heeftDrukstoel.set_waarde(value, owner=self)

    @property
    def materiaalTaatsschoen(self) -> str:
        """Het materiaal van de taatsschoen."""
        return self._materiaalTaatsschoen.get_waarde()

    @materiaalTaatsschoen.setter
    def materiaalTaatsschoen(self, value):
        self._materiaalTaatsschoen.set_waarde(value, owner=self)
