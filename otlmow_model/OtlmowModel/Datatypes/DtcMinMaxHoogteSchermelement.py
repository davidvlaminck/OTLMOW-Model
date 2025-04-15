# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMinMaxHoogteSchermelementWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._maxSchermhoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                             naam='maxSchermhoogte',
                                             label='maximale schermhoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMinMaxHoogteSchermelement.maxSchermhoogte',
                                             definition='De waarde die de hoogte in centimeter weergeeft van het hoogste element in de constructie.',
                                             owner=self)

        self._minSchermhoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                             naam='minSchermhoogte',
                                             label='minimale schermhoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMinMaxHoogteSchermelement.minSchermhoogte',
                                             definition='De waarde die de hoogte in centimeter weergeeft van het laagste element in de constructie.',
                                             owner=self)

    @property
    def maxSchermhoogte(self) -> KwantWrdInCentimeterWaarden:
        """De waarde die de hoogte in centimeter weergeeft van het hoogste element in de constructie."""
        return self._maxSchermhoogte.get_waarde()

    @maxSchermhoogte.setter
    def maxSchermhoogte(self, value):
        self._maxSchermhoogte.set_waarde(value, owner=self._parent)

    @property
    def minSchermhoogte(self) -> KwantWrdInCentimeterWaarden:
        """De waarde die de hoogte in centimeter weergeeft van het laagste element in de constructie."""
        return self._minSchermhoogte.get_waarde()

    @minSchermhoogte.setter
    def minSchermhoogte(self, value):
        self._minSchermhoogte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMinMaxHoogteSchermelement(ComplexField):
    """Complex datatype voor de hoogte in centimeter van het laagste element en van het hoogste element."""
    naam = 'DtcMinMaxHoogteSchermelement'
    label = 'min max hoogte schermelement'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMinMaxHoogteSchermelement'
    definition = 'Complex datatype voor de hoogte in centimeter van het laagste element en van het hoogste element.'
    waardeObject = DtcMinMaxHoogteSchermelementWaarden

    def __str__(self):
        return ComplexField.__str__(self)

