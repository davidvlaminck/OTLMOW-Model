# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.Datatypes.DtcBetonspecificaties import DtcBetonspecificaties, DtcBetonspecificatiesWaarden
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlUitvoeringsmethode import KlUitvoeringsmethode


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenConstructieElement(ABC):
    """Bundeling van gemeenschappelijke eigenschappen van betonnen constructie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._betonspecificaties = OTLAttribuut(field=DtcBetonspecificaties,
                                                naam='betonspecificaties',
                                                label='betonspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.betonspecificaties',
                                                definition='Eigenschappen van het gebruikte beton.',
                                                owner=self)

        self._uitvoeringsmethode = OTLAttribuut(field=KlUitvoeringsmethode,
                                                naam='uitvoeringsmethode',
                                                label='uitvoeringsmethode',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.uitvoeringsmethode',
                                                definition='Op welke manier het beton wordt aangebracht.',
                                                owner=self)

        self._wapeningsplan = OTLAttribuut(field=DtcDocument,
                                           naam='wapeningsplan',
                                           label='wapeningsplan',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.wapeningsplan',
                                           definition='Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters).',
                                           owner=self)

    @property
    def betonspecificaties(self) -> DtcBetonspecificatiesWaarden:
        """Eigenschappen van het gebruikte beton."""
        return self._betonspecificaties.get_waarde()

    @betonspecificaties.setter
    def betonspecificaties(self, value):
        self._betonspecificaties.set_waarde(value, owner=self)

    @property
    def uitvoeringsmethode(self) -> str:
        """Op welke manier het beton wordt aangebracht."""
        return self._uitvoeringsmethode.get_waarde()

    @uitvoeringsmethode.setter
    def uitvoeringsmethode(self, value):
        self._uitvoeringsmethode.set_waarde(value, owner=self)

    @property
    def wapeningsplan(self) -> DtcDocumentWaarden:
        """Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters)."""
        return self._wapeningsplan.get_waarde()

    @wapeningsplan.setter
    def wapeningsplan(self, value):
        self._wapeningsplan.set_waarde(value, owner=self)
