# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlConstructiestaalsoort import KlConstructiestaalsoort
from ..Datatypes.KlTypeVerankeringDekzerkprofiel import KlTypeVerankeringDekzerkprofiel


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVerankeringDekzerkprofielWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._materiaalVerankering = OTLAttribuut(field=KlConstructiestaalsoort,
                                                  naam='materiaalVerankering',
                                                  label='materiaal verankering',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVerankeringDekzerkprofiel.materiaalVerankering',
                                                  definition='Het materiaal waaruit de verankering van het dekzerkprofiel bestaat.',
                                                  owner=self)

        self._typeVerankering = OTLAttribuut(field=KlTypeVerankeringDekzerkprofiel,
                                             naam='typeVerankering',
                                             label='type verankering',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVerankeringDekzerkprofiel.typeVerankering',
                                             definition='De verschillende opties van verankering voor dekzerkprofielen.',
                                             owner=self)

    @property
    def materiaalVerankering(self) -> str:
        """Het materiaal waaruit de verankering van het dekzerkprofiel bestaat."""
        return self._materiaalVerankering.get_waarde()

    @materiaalVerankering.setter
    def materiaalVerankering(self, value):
        self._materiaalVerankering.set_waarde(value, owner=self._parent)

    @property
    def typeVerankering(self) -> str:
        """De verschillende opties van verankering voor dekzerkprofielen."""
        return self._typeVerankering.get_waarde()

    @typeVerankering.setter
    def typeVerankering(self, value):
        self._typeVerankering.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVerankeringDekzerkprofiel(ComplexField):
    """Complexdatatype met informatie over de verankering van een dekzerkprofiel"""
    naam = 'DtcVerankeringDekzerkprofiel'
    label = 'verankering dekzerkprofiel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVerankeringDekzerkprofiel'
    definition = 'Complexdatatype met informatie over de verankering van een dekzerkprofiel'
    waardeObject = DtcVerankeringDekzerkprofielWaarden

    def __str__(self):
        return ComplexField.__str__(self)

