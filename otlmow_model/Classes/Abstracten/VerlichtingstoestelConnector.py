# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.Datatypes.KlVerlichtingstoestelconnectorBesturingsconnector import KlVerlichtingstoestelconnectorBesturingsconnector


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelConnector(ABC):
    """Abstracte om een besturingsconnector toe te voegen aan een WV-toestel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerlichtingstoestelConnector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._besturingsconnector = OTLAttribuut(field=KlVerlichtingstoestelconnectorBesturingsconnector,
                                                 naam='besturingsconnector',
                                                 label='besturingsconnector',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerlichtingstoestelConnector.besturingsconnector',
                                                 definition='Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking.',
                                                 owner=self)

    @property
    def besturingsconnector(self) -> str:
        """Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking."""
        return self._besturingsconnector.get_waarde()

    @besturingsconnector.setter
    def besturingsconnector(self, value):
        self._besturingsconnector.set_waarde(value, owner=self)
