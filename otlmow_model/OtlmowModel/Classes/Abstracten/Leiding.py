# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.KabelgeleidingEnLeidingBevestiging import (
    KabelgeleidingEnLeidingBevestiging,
)
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class Leiding(KabelgeleidingEnLeidingBevestiging, AIMNaamObject):
    """Abstracte om de gemeenschappelijke eigenschappen en relaties van de verschillende soorten leidingen onder één noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
