# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlPenetratiegraad import KlPenetratiegraad
from ...Datatypes.KlStortsteenpenetratieMateriaal import KlStortsteenpenetratieMateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stortsteenpenetratie(AIMNaamObject, VlakGeometrie):
    """Materiaal dat gebruikt wordt om de breuksteen te penetreren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteenpenetratie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen', direction='o')  # o = direction: outgoing

        self._penetratieMateriaal = OTLAttribuut(field=KlStortsteenpenetratieMateriaal,
                                                 naam='penetratieMateriaal',
                                                 label='penetratie materiaal',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteenpenetratie.penetratieMateriaal',
                                                 definition='Het materiaal met welk de stortstenen worden gepenetreerd.',
                                                 owner=self)

        self._penetratiegraad = OTLAttribuut(field=KlPenetratiegraad,
                                             naam='penetratiegraad',
                                             label='penetratiegraad',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteenpenetratie.penetratiegraad',
                                             definition='De graad van penetratie.',
                                             owner=self)

    @property
    def penetratieMateriaal(self) -> str:
        """Het materiaal met welk de stortstenen worden gepenetreerd."""
        return self._penetratieMateriaal.get_waarde()

    @penetratieMateriaal.setter
    def penetratieMateriaal(self, value):
        self._penetratieMateriaal.set_waarde(value, owner=self)

    @property
    def penetratiegraad(self) -> str:
        """De graad van penetratie."""
        return self._penetratiegraad.get_waarde()

    @penetratiegraad.setter
    def penetratiegraad(self, value):
        self._penetratiegraad.set_waarde(value, owner=self)
