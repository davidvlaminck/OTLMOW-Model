# coding=utf-8
from ..BaseClasses.OTLObject import OTLAttribuut
from ..BaseClasses.OTLField import OTLField
from ..BaseClasses.WaardenObject import WaardenObject
from ..BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ..BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMeterTAWWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterTAW.standaardEenheid',
                                              usagenote='"m"^^cdt:ucumunit',
                                              readonly=True,
                                              constraints='"m"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in meter.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterTAW.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self) -> str:
        """De standaard eenheid bij dit datatype is uitgedrukt in meter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self) -> float:
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMeterTAW(OTLField):
    """Een kwantitatieve waarde die de hoogte weergeeft in meter van een locatie tov het TAW-referentiepeil."""
    naam = 'KwantWrdInMeterTAW'
    label = 'Kwantitatieve waarde in meter TAW'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterTAW'
    definition = 'Een kwantitatieve waarde die de hoogte weergeeft in meter van een locatie tov het TAW-referentiepeil.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInMeterTAWWaarden

    def __str__(self):
        return OTLField.__str__(self)
