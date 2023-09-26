# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.Datatypes.KlLetterVerschaald import KlLetterVerschaald
from otlmow_model.Datatypes.KlLetterVerschaaldType import KlLetterVerschaaldType
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LetterMarkeringVerschaald(FiguratieMarkeringToegang, PuntGeometrie):
    """Een markering bestaande uit letters die een verschaling ondergaat zoals een vergroting en/of een verkleining."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._basisOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                              naam='basisOppervlakte',
                                              label='basisoppervlakte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.basisOppervlakte',
                                              definition='De basisoppervlakte van de individuele lettermarkering voor verschaling zoals beschreven in de algemene omzendbrief.',
                                              owner=self)

        self._letter = OTLAttribuut(field=KlLetterVerschaald,
                                    naam='letter',
                                    label='letter',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.letter',
                                    definition='De individuele letter gebruikt bij de verschaalde wegmarkering.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.oppervlakte',
                                         definition='De oppervlakte van een figuratiemarkering na de verschaling.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlLetterVerschaaldType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.type',
                                  definition='Het type van de individuele verschaalde lettermarkering.',
                                  owner=self)

        self._vergrotingsfactor = OTLAttribuut(field=FloatOrDecimalField,
                                               naam='vergrotingsfactor',
                                               label='vergrotingsfactor',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.vergrotingsfactor',
                                               definition='Een decimaal getal dat weergeeft in welke mate de figuratiemarkering vergroot of verkleind wordt.',
                                               owner=self)

        self._verlengingsfactor = OTLAttribuut(field=FloatOrDecimalField,
                                               naam='verlengingsfactor',
                                               label='verlengingsfactor',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterMarkeringVerschaald.verlengingsfactor',
                                               definition='Een decimaal getal dat de verlenging van een figuratiemarkering weergeeft.',
                                               owner=self)

    @property
    def basisOppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De basisoppervlakte van de individuele lettermarkering voor verschaling zoals beschreven in de algemene omzendbrief."""
        return self._basisOppervlakte.get_waarde()

    @basisOppervlakte.setter
    def basisOppervlakte(self, value):
        self._basisOppervlakte.set_waarde(value, owner=self)

    @property
    def letter(self) -> str:
        """De individuele letter gebruikt bij de verschaalde wegmarkering."""
        return self._letter.get_waarde()

    @letter.setter
    def letter(self, value):
        self._letter.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van een figuratiemarkering na de verschaling."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van de individuele verschaalde lettermarkering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vergrotingsfactor(self) -> float:
        """Een decimaal getal dat weergeeft in welke mate de figuratiemarkering vergroot of verkleind wordt."""
        return self._vergrotingsfactor.get_waarde()

    @vergrotingsfactor.setter
    def vergrotingsfactor(self, value):
        self._vergrotingsfactor.set_waarde(value, owner=self)

    @property
    def verlengingsfactor(self) -> float:
        """Een decimaal getal dat de verlenging van een figuratiemarkering weergeeft."""
        return self._verlengingsfactor.get_waarde()

    @verlengingsfactor.setter
    def verlengingsfactor(self, value):
        self._verlengingsfactor.set_waarde(value, owner=self)
