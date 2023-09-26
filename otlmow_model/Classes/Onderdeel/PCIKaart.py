# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlPCIkaartMerk import KlPCIkaartMerk
from otlmow_model.Datatypes.KlPCIkaartModelnaam import KlPCIkaartModelnaam
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PCIKaart(AIMNaamObject, PuntGeometrie):
    """Peripheral Component Interconnect of uitbreidingssleuf."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang')

        self._merk = OTLAttribuut(field=KlPCIkaartMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart.merk',
                                  definition='Het merk van de PCI-kaart.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPCIkaartModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart.modelnaam',
                                       definition='De modelnaam van de PCI-kaart.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de PCI-kaart."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de PCI-kaart."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
