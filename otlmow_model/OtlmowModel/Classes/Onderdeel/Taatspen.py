# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlMateriaalDeklaag import KlMateriaalDeklaag
from ...Datatypes.KlMateriaalTaatsmechanisme import KlMateriaalTaatsmechanisme
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taatspen(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een onderdeel dat de verbinding maakt tussen de taatsschoen en taatspot binnen het taatsmechanisme."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspot', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme', direction='o')  # o = direction: outgoing

        self._heeftHouder = OTLAttribuut(field=BooleanField,
                                         naam='heeftHouder',
                                         label='heeft houder',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen.heeftHouder',
                                         definition='Geeft aan of de taatspen een houder heeft of niet.',
                                         owner=self)

        self._materiaalDeklaag = OTLAttribuut(field=KlMateriaalDeklaag,
                                              naam='materiaalDeklaag',
                                              label='materiaal deklaag',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen.materiaalDeklaag',
                                              definition='Het materiaal van het deklaag',
                                              owner=self)

        self._materiaalTaatspen = OTLAttribuut(field=KlMateriaalTaatsmechanisme,
                                               naam='materiaalTaatspen',
                                               label='materiaal taatspen',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen.materiaalTaatspen',
                                               definition='Het materiaal van de taatspen.',
                                               owner=self)

    @property
    def heeftHouder(self) -> bool:
        """Geeft aan of de taatspen een houder heeft of niet."""
        return self._heeftHouder.get_waarde()

    @heeftHouder.setter
    def heeftHouder(self, value):
        self._heeftHouder.set_waarde(value, owner=self)

    @property
    def materiaalDeklaag(self) -> str:
        """Het materiaal van het deklaag"""
        return self._materiaalDeklaag.get_waarde()

    @materiaalDeklaag.setter
    def materiaalDeklaag(self, value):
        self._materiaalDeklaag.set_waarde(value, owner=self)

    @property
    def materiaalTaatspen(self) -> str:
        """Het materiaal van de taatspen."""
        return self._materiaalTaatspen.get_waarde()

    @materiaalTaatspen.setter
    def materiaalTaatspen(self, value):
        self._materiaalTaatspen.set_waarde(value, owner=self)
