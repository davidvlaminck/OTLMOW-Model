# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ..Datatypes.KlTechnischDocument import KlTechnischDocument


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTechnischDocumentWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._bijlage = OTLAttribuut(field=DtcDocument,
                                     naam='bijlage',
                                     label='bijlage',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTechnischDocument.bijlage',
                                     definition='Een bestandsbijlage.',
                                     owner=self)

        self._typeDocument = OTLAttribuut(field=KlTechnischDocument,
                                          naam='typeDocument',
                                          label='type document',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTechnischDocument.typeDocument',
                                          definition='Het type bestandsbijlage.',
                                          owner=self)

    @property
    def bijlage(self) -> DtcDocumentWaarden:
        """Een bestandsbijlage."""
        return self._bijlage.get_waarde()

    @bijlage.setter
    def bijlage(self, value):
        self._bijlage.set_waarde(value, owner=self._parent)

    @property
    def typeDocument(self) -> str:
        """Het type bestandsbijlage."""
        return self._typeDocument.get_waarde()

    @typeDocument.setter
    def typeDocument(self, value):
        self._typeDocument.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTechnischDocument(ComplexField):
    """Complex datatype om een of meerdere technische documenten aan te koppelen aan de assets"""
    naam = 'DtcTechnischDocument'
    label = 'complex datatype technisch document'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTechnischDocument'
    definition = 'Complex datatype om een of meerdere technische documenten aan te koppelen aan de assets'
    waardeObject = DtcTechnischDocumentWaarden

    def __str__(self):
        return ComplexField.__str__(self)

