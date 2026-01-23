# coding=utf-8
from ..BaseClasses.OTLObject import OTLAttribuut
from ..BaseClasses.WaardenObject import WaardenObject
from ..BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlAfdichtingsmateriaal import KlAfdichtingsmateriaal
from ..Datatypes.KlFunctionaliteitsvereisteKabelleidingdoorvoer import KlFunctionaliteitsvereisteKabelleidingdoorvoer


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfdichtingKabelleidingdoorvoerWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._afdichtingsmateriaal = OTLAttribuut(field=KlAfdichtingsmateriaal,
                                                  naam='afdichtingsmateriaal',
                                                  label='afdichtingsmateriaal',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAfdichtingKabelleidingdoorvoer.afdichtingsmateriaal',
                                                  definition='Het afdichtingsmateriaal van de kabellleidingdoorvoer.',
                                                  owner=self)

        self._functionaliteitsvereiste = OTLAttribuut(field=KlFunctionaliteitsvereisteKabelleidingdoorvoer,
                                                      naam='functionaliteitsvereiste',
                                                      label='functionaliteitsvereiste',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAfdichtingKabelleidingdoorvoer.functionaliteitsvereiste',
                                                      definition='De functionaliteitsvereiste van de afdichting van de kabelleidingdoorvoer.',
                                                      owner=self)

    @property
    def afdichtingsmateriaal(self) -> str:
        """Het afdichtingsmateriaal van de kabellleidingdoorvoer."""
        return self._afdichtingsmateriaal.get_waarde()

    @afdichtingsmateriaal.setter
    def afdichtingsmateriaal(self, value):
        self._afdichtingsmateriaal.set_waarde(value, owner=self._parent)

    @property
    def functionaliteitsvereiste(self) -> str:
        """De functionaliteitsvereiste van de afdichting van de kabelleidingdoorvoer."""
        return self._functionaliteitsvereiste.get_waarde()

    @functionaliteitsvereiste.setter
    def functionaliteitsvereiste(self, value):
        self._functionaliteitsvereiste.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfdichtingKabelleidingdoorvoer(ComplexField):
    """Complex datatype voor materiaal en functionaliteitsvereisten van de kabelleidingdoorvoer."""
    naam = 'DtcAfdichtingKabelleidingdoorvoer'
    label = 'afdichting kabelleidingdoorvoer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAfdichtingKabelleidingdoorvoer'
    definition = 'Complex datatype voor materiaal en functionaliteitsvereisten van de kabelleidingdoorvoer.'
    waardeObject = DtcAfdichtingKabelleidingdoorvoerWaarden

    def __str__(self):
        return ComplexField.__str__(self)

