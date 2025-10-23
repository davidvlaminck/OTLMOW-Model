# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ContainerBuis(ABC):
    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.8.0'

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis', direction='o', deprecated='2.3.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis', direction='o', deprecated='2.3.0')  # o = direction: outgoing

        self._kleur = OTLAttribuut(field=StringField,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur',
                                   usagenote='Klasse uit gebruik sinds versie 2.8.0 ',
                                   deprecated_version='2.8.0',
                                   kardinaliteit_max='*',
                                   definition='De kleur van de coating.',
                                   owner=self)

    @property
    def kleur(self) -> List[str]:
        """De kleur van de coating."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)
