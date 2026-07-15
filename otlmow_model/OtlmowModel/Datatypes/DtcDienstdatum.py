# coding=utf-8
from datetime import datetime, datetime
from ..BaseClasses.OTLObject import OTLAttribuut
from ..BaseClasses.WaardenObject import WaardenObject
from ..BaseClasses.ComplexField import ComplexField
from ..BaseClasses.DateTimeField import DateTimeField
from ..BaseClasses.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDienstdatumWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._commentaar = OTLAttribuut(field=StringField,
                                        naam='commentaar',
                                        label='commentaar',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcDienstdatum.commentaar',
                                        definition='Bijkomende informatie van de regeling.',
                                        owner=self)

        self._indienstname = OTLAttribuut(field=DateTimeField,
                                          naam='indienstname',
                                          label='indienstname',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcDienstdatum.indienstname',
                                          definition='De datum waarop het VPlan effectief van toepassing wordt op de verkeersregelinstallatie.',
                                          owner=self)

        self._uitdienstname = OTLAttribuut(field=DateTimeField,
                                           naam='uitdienstname',
                                           label='uitdienstname',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcDienstdatum.uitdienstname',
                                           definition='De uitdienstname is de datum waarop het VPlan niet langer van toepassing is op de verkeersregelinstallatie.',
                                           owner=self)

    @property
    def commentaar(self) -> str:
        """Bijkomende informatie van de regeling."""
        return self._commentaar.get_waarde()

    @commentaar.setter
    def commentaar(self, value):
        self._commentaar.set_waarde(value, owner=self._parent)

    @property
    def indienstname(self) -> datetime:
        """De datum waarop het VPlan effectief van toepassing wordt op de verkeersregelinstallatie."""
        return self._indienstname.get_waarde()

    @indienstname.setter
    def indienstname(self, value):
        self._indienstname.set_waarde(value, owner=self._parent)

    @property
    def uitdienstname(self) -> datetime:
        """De uitdienstname is de datum waarop het VPlan niet langer van toepassing is op de verkeersregelinstallatie."""
        return self._uitdienstname.get_waarde()

    @uitdienstname.setter
    def uitdienstname(self, value):
        self._uitdienstname.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDienstdatum(ComplexField):
    """Complex datatype ter inventarisatie van de indienst- en uitdienstname van een V-plan."""
    naam = 'DtcDienstdatum'
    label = 'Dienstdatum V-plan'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcDienstdatum'
    definition = 'Complex datatype ter inventarisatie van de indienst- en uitdienstname van een V-plan.'
    waardeObject = DtcDienstdatumWaarden

    def __str__(self):
        return ComplexField.__str__(self)

