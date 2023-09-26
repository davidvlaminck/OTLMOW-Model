# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.VegetatieElement import VegetatieElement
from otlmow_model.Datatypes.KlVegetatieWortel import KlVegetatieWortel
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SolitaireHeester(VegetatieElement, PuntGeometrie):
    """Afzonderlijk te onderscheiden heester. Heesters zijn houtachtige planten die in of dicht bij de grond vertakken. Anders dan een boom vormen ze in het algemeen geen duidelijke stam, maar komen de meeste soorten met een aantal takken uit de grond, die dan ook grondtakken genoemd worden. Voorwaarde is wel dat de plant in zijn eventuele stam en takken houtweefsel vormt, hoewel dat niet tot in het hart hoeft te zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SolitaireHeester'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._wortelAanplant = OTLAttribuut(field=KlVegetatieWortel,
                                            naam='wortelAanplant',
                                            label='wortel aanplant',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SolitaireHeester.wortelAanplant',
                                            definition='De manier van levering en aanplanting van het wortelgestel van de boom of plant.',
                                            owner=self)

    @property
    def wortelAanplant(self) -> str:
        """De manier van levering en aanplanting van het wortelgestel van de boom of plant."""
        return self._wortelAanplant.get_waarde()

    @wortelAanplant.setter
    def wortelAanplant(self, value):
        self._wortelAanplant.set_waarde(value, owner=self)
