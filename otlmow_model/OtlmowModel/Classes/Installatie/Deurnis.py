# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.UitsparingSluisdeur import UitsparingSluisdeur
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAfmetingBxhInM import DtcAfmetingBxhInM, DtcAfmetingBxhInMWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Deurnis(UitsparingSluisdeur, AIMNaamObject):
    """Compartiment van een waterbouwkundige constructie waartegen de deurtip van een roldeur of draaideur aansluit in beweging naar gesloten toestand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Deurnis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxhInM,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Deurnis.afmetingen',
                                        definition='De afmetingen van de deurkamer, breedte en lengte, uitgedrukt in meter',
                                        owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxhInMWaarden:
        """De afmetingen van de deurkamer, breedte en lengte, uitgedrukt in meter"""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)