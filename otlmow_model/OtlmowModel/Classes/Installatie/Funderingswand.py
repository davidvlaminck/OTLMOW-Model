# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AxiaalDraagvermogen import AxiaalDraagvermogen
from ...Classes.Abstracten.AxiaalDraagvermogenWand import AxiaalDraagvermogenWand
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.Abstracten.WaterremmendeFunctie import WaterremmendeFunctie
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Funderingswand(AxiaalDraagvermogen, AxiaalDraagvermogenWand, Grondkeringen, WaterremmendeFunctie, AIMNaamObject):
    """Wand die dient om de belastingen van constructies/elementen op te vangen/over te brengen naar draagkrachtige lagen. Kan ook een grondkerende/waterkerende functie hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Funderingswand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfmetingenDiepCBWand', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming

        self._totaleLengteFunderingswand = OTLAttribuut(field=KwantWrdInMeter,
                                                        naam='totaleLengteFunderingswand',
                                                        label='totale lengte funderingswand',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Funderingswand.totaleLengteFunderingswand',
                                                        definition='De totale horizontale lengte van de gehele funderingswand in lopende meter.',
                                                        owner=self)

    @property
    def totaleLengteFunderingswand(self) -> KwantWrdInMeterWaarden:
        """De totale horizontale lengte van de gehele funderingswand in lopende meter."""
        return self._totaleLengteFunderingswand.get_waarde()

    @totaleLengteFunderingswand.setter
    def totaleLengteFunderingswand(self, value):
        self._totaleLengteFunderingswand.set_waarde(value, owner=self)
