# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloAmpereWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloAmpere.standaardEenheid',
                                              readonly=True,
                                              constraints='"kA"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kiloampère.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloAmpere.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self) -> str:
        """De standaard eenheid bij dit datatype is uitgedrukt in kiloampère."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self) -> float:
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloAmpere(OTLField):
    """Een kwantitatieve waarde die een getal in kiloampère uitdrukt."""
    naam = 'KwantWrdInKiloAmpere'
    label = 'Kwantitatieve waarde in kilo ampère'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloAmpere'
    definition = 'Een kwantitatieve waarde die een getal in kiloampère uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInKiloAmpereWaarden

    def __str__(self):
        return OTLField.__str__(self)

