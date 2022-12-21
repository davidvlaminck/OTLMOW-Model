# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlGrondbewerking import KlGrondbewerking
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grondbewerking(AIMObject):
    """Omvat de profielbewerkingen en bouwvoorwerkzaamheden voor aanleg van beplaningen, graslanden, wegbermen en grasmatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Grondbewerking'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Grondbewerking.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te bewerken grond.',
                                         owner=self)

        self._soortGrondbewerking = OTLAttribuut(field=KlGrondbewerking,
                                                 naam='soortGrondbewerking',
                                                 label='soort grondbewerking',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Grondbewerking.soortGrondbewerking',
                                                 definition='Specificatie van het type profielbewerking en bouwvoorwerkzaamheden voor aanleg van beplantingen, graslanden, wegbermen en grasmatten.',
                                                 owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte in vierkante meter van de te bewerken grond."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortGrondbewerking(self) -> str:
        """Specificatie van het type profielbewerking en bouwvoorwerkzaamheden voor aanleg van beplantingen, graslanden, wegbermen en grasmatten."""
        return self._soortGrondbewerking.get_waarde()

    @soortGrondbewerking.setter
    def soortGrondbewerking(self, value):
        self._soortGrondbewerking.set_waarde(value, owner=self)
