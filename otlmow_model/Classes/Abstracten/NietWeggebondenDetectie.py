# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Detectie import Detectie
from otlmow_model.Classes.Abstracten.FirmwareObject import FirmwareObject
from otlmow_model.Datatypes.KwantWrdInVolt import KwantWrdInVolt, KwantWrdInVoltWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietWeggebondenDetectie(Detectie, FirmwareObject, PuntGeometrie):
    """Abstracte voor niet weggebonden detectoren. Deze bevinden zich niet in het wegoppervlak en worden aangewend voor volgende doeleinden: *nabij de stoplijnen van kruispunten als kruispuntdetectoren waardoor de verkeersafhankelijke werking van de verkeersregelaar mogelijk wordt (zogenaamde microregeling); *op willekeurige plaatsen in het verkeersnet, als selectieve detectoren voor het registreren van een aanvraag voor prioritaire doorgang vanwege het openbaar vervoer (bussen of tramrijtuigen) teneinde de afloop van de cyclus op de kruispunten te beïnvloeden"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')

        self._voedingsspanning = OTLAttribuut(field=KwantWrdInVolt,
                                              naam='voedingsspanning',
                                              label='voedingsspanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie.voedingsspanning',
                                              definition='Spanning waarmee de detectoren gevoed worden.',
                                              owner=self)

    @property
    def voedingsspanning(self) -> KwantWrdInVoltWaarden:
        """Spanning waarmee de detectoren gevoed worden."""
        return self._voedingsspanning.get_waarde()

    @voedingsspanning.setter
    def voedingsspanning(self, value):
        self._voedingsspanning.set_waarde(value, owner=self)
