# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Onderdeel.Grasland import Grasland
from otlmow_model.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class GrasKruidenmixGraslandfase3(Grasland):
    """G3 - Fijn mozaïek van grassen en kruiden zoals: beemdlangbloem, gewone berenklauw, gewoon duizendblad, gewoon reukgras, glanshaver, grasmuur, grote vossenstaart, hopklaver, kleine klaver, pastinaak, peen, rietzwenkgras, rode klaver, rood zwenkgras, scherpe boterbloem, sint-Janskruid, smalle weegbree, timotee, veldbeemdgras, veldzuring, gewoon biggenkruid, kamgras, veldgerst, vijfvingerkruid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrasKruidenmixGraslandfase3'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._huidigNatuurbeeld = OTLAttribuut(field=KlNSB,
                                               naam='huidigNatuurbeeld',
                                               label='huidig natuurbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrasKruidenmixGraslandfase3.huidigNatuurbeeld',
                                               definition='Bepaling van het vegetatietype op basis van terreininventarisatie.',
                                               owner=self)

    @property
    def huidigNatuurbeeld(self) -> str:
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
        return self._huidigNatuurbeeld.get_waarde()

    @huidigNatuurbeeld.setter
    def huidigNatuurbeeld(self, value):
        self._huidigNatuurbeeld.set_waarde(value, owner=self)
