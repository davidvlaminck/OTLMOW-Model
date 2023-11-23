# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Grasland import Grasland
from ...Datatypes.KlNSB import KlNSB
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SoortenrijkSchraalGraslandGraslandfase5(Grasland, VlakGeometrie):
    """G5 - Een fijn, soortenrijk mozaïek van geel-, grijs- en blauwgroene laagblijvende schijngrassen (zeggen en russen) en kruiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SoortenrijkSchraalGraslandGraslandfase5'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._huidigNatuurbeeld = OTLAttribuut(field=KlNSB,
                                               naam='huidigNatuurbeeld',
                                               label='huidig natuurbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SoortenrijkSchraalGraslandGraslandfase5.huidigNatuurbeeld',
                                               definition='Bepaling van het vegetatietype op basis van terreininventarisatie.',
                                               owner=self)

    @property
    def huidigNatuurbeeld(self) -> str:
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
        return self._huidigNatuurbeeld.get_waarde()

    @huidigNatuurbeeld.setter
    def huidigNatuurbeeld(self, value):
        self._huidigNatuurbeeld.set_waarde(value, owner=self)
