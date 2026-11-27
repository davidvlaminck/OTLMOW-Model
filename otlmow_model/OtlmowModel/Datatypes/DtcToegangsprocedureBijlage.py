# coding=utf-8
from ..BaseClasses.ComplexField import ComplexField
from ..BaseClasses.OTLObject import OTLAttribuut
from ..BaseClasses.URIField import URIField
from ..BaseClasses.WaardenObject import WaardenObject
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.DteTekstblok import DteTekstblok, DteTekstblokWaarden
from ..Datatypes.KlToegangsprocedureBijlageType import KlToegangsprocedureBijlageType


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcToegangsprocedureBijlageWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._document = OTLAttribuut(field=DtcDocument,
                                      naam='document',
                                      label='document',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureBijlage.document',
                                      kardinaliteit_max='*',
                                      definition='Document dat bij de toegangsprocedure als bijlage toegevoed kan worden.',
                                      owner=self)

        self._nota = OTLAttribuut(field=DteTekstblok,
                                  naam='nota',
                                  label='nota',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureBijlage.nota',
                                  definition='Vrije nota die als bijlage bij de toegangsprocedure gevoegd kan worden.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlToegangsprocedureBijlageType,
                                  naam='type',
                                  label='bijlage type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureBijlage.type',
                                  definition='Het type bijlage gevoegd bij de toegangsprocedure.',
                                  owner=self)

        self._website = OTLAttribuut(field=URIField,
                                     naam='website',
                                     label='website URL',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureBijlage.website',
                                     definition='Website URL die als bijlage bij de toegangsprocedure gevoegd kan worden',
                                     owner=self)

    @property
    def document(self) -> list[DtcDocumentWaarden]:
        """Document dat bij de toegangsprocedure als bijlage toegevoed kan worden."""
        return self._document.get_waarde()

    @document.setter
    def document(self, value):
        self._document.set_waarde(value, owner=self._parent)

    @property
    def nota(self) -> DteTekstblokWaarden:
        """Vrije nota die als bijlage bij de toegangsprocedure gevoegd kan worden."""
        return self._nota.get_waarde()

    @nota.setter
    def nota(self, value):
        self._nota.set_waarde(value, owner=self._parent)

    def _get_type(self) -> str:
        """Het type bijlage gevoegd bij de toegangsprocedure."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self._parent)
    type = property(_get_type, _set_type)

    @property
    def website(self) -> str:
        """Website URL die als bijlage bij de toegangsprocedure gevoegd kan worden"""
        return self._website.get_waarde()

    @website.setter
    def website(self, value):
        self._website.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcToegangsprocedureBijlage(ComplexField):
    """Complex datatype dat informatie omtrent een bijlage voor een toegangsprocedure specifieert."""
    naam = 'DtcToegangsprocedureBijlage'
    label = 'Bijlage toegangsprocedure'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcToegangsprocedureBijlage'
    definition = 'Complex datatype dat informatie omtrent een bijlage voor een toegangsprocedure specifieert.'
    waardeObject = DtcToegangsprocedureBijlageWaarden

    def __str__(self):
        return ComplexField.__str__(self)

