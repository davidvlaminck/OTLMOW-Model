# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalStraatkap import KlMateriaalStraatkap
from ...Datatypes.KlTypeNutsvoorziening import KlTypeNutsvoorziening
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Straatkap(AIMNaamObject, PuntGeometrie):
    """Een deksel waarvan de diameter of de zijde kleiner is dan 65 cm en dat gelijkgronds is geplaatst in het vlak van de wegbaan. Deze deksels dienen als merktekens en geven toegang tot onderliggende leidingen zoals communicatieleidingen of waterleidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkap'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._materiaalstraatkap = OTLAttribuut(field=KlMateriaalStraatkap,
                                                naam='materiaalstraatkap',
                                                label='materiaal straatkap',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkap.materiaalstraatkap',
                                                definition='Het materiaal van een straatkap verwijst naar de specifieke bouwstof of samenstelling waaruit het deksel bestaat.',
                                                owner=self)

        self._typenutsvoorziening = OTLAttribuut(field=KlTypeNutsvoorziening,
                                                 naam='typenutsvoorziening',
                                                 label='type nutsvoorziening',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkap.typenutsvoorziening',
                                                 definition='Het type nutsvoorziening van een straatkap verwijst naar de specifieke aard van de nutsinfrastructuur waartoe het deksel toegang biedt.',
                                                 owner=self)

    @property
    def materiaalstraatkap(self) -> str:
        """Het materiaal van een straatkap verwijst naar de specifieke bouwstof of samenstelling waaruit het deksel bestaat."""
        return self._materiaalstraatkap.get_waarde()

    @materiaalstraatkap.setter
    def materiaalstraatkap(self, value):
        self._materiaalstraatkap.set_waarde(value, owner=self)

    @property
    def typenutsvoorziening(self) -> str:
        """Het type nutsvoorziening van een straatkap verwijst naar de specifieke aard van de nutsinfrastructuur waartoe het deksel toegang biedt."""
        return self._typenutsvoorziening.get_waarde()

    @typenutsvoorziening.setter
    def typenutsvoorziening(self, value):
        self._typenutsvoorziening.set_waarde(value, owner=self)
