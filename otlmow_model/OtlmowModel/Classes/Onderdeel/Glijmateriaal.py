# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeGlijmateriaal import KlTypeGlijmateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Glijmateriaal(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een slijtagegevoelig onderdeel dat direct contact maakt met een relatief bewegend onderdeel. Het dient vooral om slijtage, wrijving of schade aan de betrokken glijoppervlakken te beperken en om krachten over te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Glijmateriaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Centreervork', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rol', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Grendelmechanisme', direction='o')  # o = direction: outgoing

        self._typeGlijmateriaal = OTLAttribuut(field=KlTypeGlijmateriaal,
                                               naam='typeGlijmateriaal',
                                               label='type glijmateriaal',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Glijmateriaal.typeGlijmateriaal',
                                               definition='Het type glijmateriaal.',
                                               owner=self)

    @property
    def typeGlijmateriaal(self) -> str:
        """Het type glijmateriaal."""
        return self._typeGlijmateriaal.get_waarde()

    @typeGlijmateriaal.setter
    def typeGlijmateriaal(self, value):
        self._typeGlijmateriaal.set_waarde(value, owner=self)
