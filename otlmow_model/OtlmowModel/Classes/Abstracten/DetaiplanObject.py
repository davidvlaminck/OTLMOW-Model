# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class DetaiplanObject(ABC):
    """Abstracte dat het attribuut detailplan bevat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DetaiplanObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._detailplan = OTLAttribuut(field=DtcDocument,
                                        naam='detailplan',
                                        label='detailplan',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DetaiplanObject.detailplan',
                                        definition='Dit plan bevat o.a. informatie over de materiaalkwaliteit, conservering en het verankeringssysteem.',
                                        owner=self)

    @property
    def detailplan(self) -> DtcDocumentWaarden:
        """Dit plan bevat o.a. informatie over de materiaalkwaliteit, conservering en het verankeringssysteem."""
        return self._detailplan.get_waarde()

    @detailplan.setter
    def detailplan(self, value):
        self._detailplan.set_waarde(value, owner=self)
