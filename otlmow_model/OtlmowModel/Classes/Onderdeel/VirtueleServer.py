# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.HardwareToegang import HardwareToegang
from ...Datatypes.KlVirtueleServerMerk import KlVirtueleServerMerk
from ...Datatypes.KlVirtueleServerModelnaam import KlVirtueleServerModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VirtueleServer(HardwareToegang, GeenGeometrie):
    """Gedeelte van een fysieke server, dat zich met behulp van software gedraagt als een 'echte' server."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster', direction='o')  # o = direction: outgoing

        self._merk = OTLAttribuut(field=KlVirtueleServerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer.merk',
                                  definition='Het merk van de virtuele server.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVirtueleServerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer.modelnaam',
                                       definition='De modelnaam van de virtuele server.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de virtuele server."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de virtuele server."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
