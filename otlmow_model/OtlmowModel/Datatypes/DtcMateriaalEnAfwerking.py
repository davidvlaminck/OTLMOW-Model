# coding=utf-8
from ..BaseClasses.OTLObject import OTLAttribuut
from ..BaseClasses.WaardenObject import WaardenObject
from ..BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlAfwerkingstypeLeuning import KlAfwerkingstypeLeuning
from ..Datatypes.KlMateriaalLeuning import KlMateriaalLeuning


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMateriaalEnAfwerkingWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._afwerkingstypeLeuning = OTLAttribuut(field=KlAfwerkingstypeLeuning,
                                                   naam='afwerkingstypeLeuning',
                                                   label='afwerkingstype leuning',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMateriaalEnAfwerking.afwerkingstypeLeuning',
                                                   definition='Type afwerking van de leuning.',
                                                   owner=self)

        self._materiaalLeuning = OTLAttribuut(field=KlMateriaalLeuning,
                                              naam='materiaalLeuning',
                                              label='materiaal leuning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMateriaalEnAfwerking.materiaalLeuning',
                                              definition='Het materiaal waaruit de leuning is vervaardigd.',
                                              owner=self)

    @property
    def afwerkingstypeLeuning(self) -> str:
        """Type afwerking van de leuning."""
        return self._afwerkingstypeLeuning.get_waarde()

    @afwerkingstypeLeuning.setter
    def afwerkingstypeLeuning(self, value):
        self._afwerkingstypeLeuning.set_waarde(value, owner=self._parent)

    @property
    def materiaalLeuning(self) -> str:
        """Het materiaal waaruit de leuning is vervaardigd."""
        return self._materiaalLeuning.get_waarde()

    @materiaalLeuning.setter
    def materiaalLeuning(self, value):
        self._materiaalLeuning.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMateriaalEnAfwerking(ComplexField):
    """Complex datatype voor materiaal en afwerking van de leuning."""
    naam = 'DtcMateriaalEnAfwerking'
    label = 'materiaal en afwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcMateriaalEnAfwerking'
    definition = 'Complex datatype voor materiaal en afwerking van de leuning.'
    waardeObject = DtcMateriaalEnAfwerkingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

