# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeGrendel import KlTypeGrendel
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grendel(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een mechanisch onderdeel dat toelaat om een constructie of bewegend element in een gewenste positie te vergrendelen, meestal door middel van een schuif-, klem- of draaibeweging.
"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grendel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Grendelmechanisme', direction='o')  # o = direction: outgoing

        self._typeGrendel = OTLAttribuut(field=KlTypeGrendel,
                                         naam='typeGrendel',
                                         label='type grendel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grendel.typeGrendel',
                                         definition='Het type grendel.',
                                         owner=self)

    @property
    def typeGrendel(self) -> str:
        """Het type grendel."""
        return self._typeGrendel.get_waarde()

    @typeGrendel.setter
    def typeGrendel(self, value):
        self._typeGrendel.set_waarde(value, owner=self)
