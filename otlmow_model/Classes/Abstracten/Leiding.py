# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.KabelgeleidingEnLeidingBevestiging import KabelgeleidingEnLeidingBevestiging
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Leiding(KabelgeleidingEnLeidingBevestiging, AIMNaamObject, LijnGeometrie):
    """Abstracte om de gemeenschappelijke eigenschappen en relaties van de verschillende soorten leidingen onder één noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising')

        self._buitendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding.buitendiameter',
                                            definition='De buitendiameter van de leiding in millimeter. Indien de leiding geen cirkelvormige doorsnede heeft, dan gaat het hier om de diameter van de omgeschreven cirkel.',
                                            owner=self)

        self._isRisicovol = OTLAttribuut(field=BooleanField,
                                         naam='isRisicovol',
                                         label='is risicovol',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding.isRisicovol',
                                         definition='Geeft aan of werken aan of rond de leiding een verhoogd risico met zich meebrengen omwille van de aard van de betrokken leiding.',
                                         owner=self)

    @property
    def buitendiameter(self) -> KwantWrdInMillimeterWaarden:
        """De buitendiameter van de leiding in millimeter. Indien de leiding geen cirkelvormige doorsnede heeft, dan gaat het hier om de diameter van de omgeschreven cirkel."""
        return self._buitendiameter.get_waarde()

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def isRisicovol(self) -> bool:
        """Geeft aan of werken aan of rond de leiding een verhoogd risico met zich meebrengen omwille van de aard van de betrokken leiding."""
        return self._isRisicovol.get_waarde()

    @isRisicovol.setter
    def isRisicovol(self, value):
        self._isRisicovol.set_waarde(value, owner=self)
