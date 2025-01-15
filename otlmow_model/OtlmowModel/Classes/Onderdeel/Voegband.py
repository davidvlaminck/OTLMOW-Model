# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlMateriaalVoegband import KlMateriaalVoegband
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voegband(AIMNaamObject, PuntGeometrie):
    """Een flexibel afdichtingselement dat wordt geplaatst in voegen van betonconstructies. Het doel van de voegband is om grond- en waterdichtheid te bieden en om een zekere (thermische) vervorming van de constructie op te vangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegband'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur', direction='u')  # u = unidirectional

        self._isGeinjecteerd = OTLAttribuut(field=BooleanField,
                                            naam='isGeinjecteerd',
                                            label='is geïnjecteerd',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegband.isGeinjecteerd',
                                            definition='Geeft aan of de voegband al dan niet geïnjecteerd is.',
                                            owner=self)

        self._materiaalVoegband = OTLAttribuut(field=KlMateriaalVoegband,
                                               naam='materiaalVoegband',
                                               label='materiaal voegband',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegband.materiaalVoegband',
                                               definition='De verschillende opties van materiaal voor voegbanden.',
                                               owner=self)

    @property
    def isGeinjecteerd(self) -> bool:
        """Geeft aan of de voegband al dan niet geïnjecteerd is."""
        return self._isGeinjecteerd.get_waarde()

    @isGeinjecteerd.setter
    def isGeinjecteerd(self, value):
        self._isGeinjecteerd.set_waarde(value, owner=self)

    @property
    def materiaalVoegband(self) -> str:
        """De verschillende opties van materiaal voor voegbanden."""
        return self._materiaalVoegband.get_waarde()

    @materiaalVoegband.setter
    def materiaalVoegband(self, value):
        self._materiaalVoegband.set_waarde(value, owner=self)
