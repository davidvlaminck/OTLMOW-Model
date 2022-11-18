# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.BaseClasses.ComplexField import ComplexField
from otlmow_model.Datatypes.DteTekstblok import DteTekstblok, DteTekstblokWaarden
from otlmow_model.Datatypes.KlAlgMimeType import KlAlgMimeType
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.BaseClasses.URIField import URIField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDocumentWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._bestandsnaam = OTLAttribuut(field=StringField,
                                          naam='bestandsnaam',
                                          label='bestandsnaam',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.bestandsnaam',
                                          definition='De naam van het Document inclusief de bestandsextensie, van de naam gescheiden door een punt.',
                                          owner=self)

        self._mimeType = OTLAttribuut(field=KlAlgMimeType,
                                      naam='mimeType',
                                      label='mime-type',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.mimeType',
                                      definition='Het MIME type van het document.',
                                      owner=self)

        self._omschrijving = OTLAttribuut(field=DteTekstblok,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.omschrijving',
                                          definition='Een korte toelichting over waar het document juist voor dient.',
                                          owner=self)

        self._uri = OTLAttribuut(field=URIField,
                                 naam='uri',
                                 label='uri',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.uri',
                                 definition='De verwijzing naar de bestandslocatie via een link. Bij lokale bestanden kan dit eventueel ook een pad zijn.',
                                 owner=self)

    @property
    def bestandsnaam(self) -> str:
        """De naam van het Document inclusief de bestandsextensie, van de naam gescheiden door een punt."""
        return self._bestandsnaam.get_waarde()

    @bestandsnaam.setter
    def bestandsnaam(self, value):
        self._bestandsnaam.set_waarde(value, owner=self._parent)

    @property
    def mimeType(self) -> str:
        """Het MIME type van het document."""
        return self._mimeType.get_waarde()

    @mimeType.setter
    def mimeType(self, value):
        self._mimeType.set_waarde(value, owner=self._parent)

    @property
    def omschrijving(self) -> DteTekstblokWaarden:
        """Een korte toelichting over waar het document juist voor dient."""
        return self._omschrijving.get_waarde()

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self._parent)

    @property
    def uri(self) -> str:
        """De verwijzing naar de bestandslocatie via een link. Bij lokale bestanden kan dit eventueel ook een pad zijn."""
        return self._uri.get_waarde()

    @uri.setter
    def uri(self, value):
        self._uri.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDocument(ComplexField):
    """Complex datatype voor alle bestandsbijlages."""
    naam = 'DtcDocument'
    label = 'Bestandsbijlage'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument'
    definition = 'Complex datatype voor alle bestandsbijlages.'
    waardeObject = DtcDocumentWaarden

    def __str__(self):
        return ComplexField.__str__(self)

