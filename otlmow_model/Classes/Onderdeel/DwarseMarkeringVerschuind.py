# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.DwarseMarkeringToegang import DwarseMarkeringToegang
from otlmow_model.Datatypes.KlDwarseMarkeringVerschuindCode import KlDwarseMarkeringVerschuindCode
from otlmow_model.Datatypes.KlDwarseMarkeringVerschuindSoort import KlDwarseMarkeringVerschuindSoort
from otlmow_model.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwarseMarkeringVerschuind(DwarseMarkeringToegang):
    """Een schuine markering dwars op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._basisoppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                              naam='basisoppervlakte',
                                              label='oppervlakte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.basisoppervlakte',
                                              definition='De basisoppervlakte van de dwarse markering in vierkante meter.',
                                              owner=self)

        self._code = OTLAttribuut(field=KlDwarseMarkeringVerschuindCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.code',
                                  definition='De (COPRO/BENOR) code van dwarse markering.',
                                  owner=self)

        self._hoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                  naam='hoek',
                                  label='hoek',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.hoek',
                                  definition='De hoek van de verschuinde dwarsmarkering in decimale graden.',
                                  owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.oppervlakte',
                                         definition='De oppervlakte van een dwarsmarkering na verschuining.',
                                         owner=self)

        self._soortOmschrijving = OTLAttribuut(field=KlDwarseMarkeringVerschuindSoort,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van dwarse markering.',
                                               owner=self)

    @property
    def basisoppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De basisoppervlakte van de dwarse markering in vierkante meter."""
        return self._basisoppervlakte.get_waarde()

    @basisoppervlakte.setter
    def basisoppervlakte(self, value):
        self._basisoppervlakte.set_waarde(value, owner=self)

    @property
    def code(self) -> str:
        """De (COPRO/BENOR) code van dwarse markering."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def hoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """De hoek van de verschuinde dwarsmarkering in decimale graden."""
        return self._hoek.get_waarde()

    @hoek.setter
    def hoek(self, value):
        self._hoek.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van een dwarsmarkering na verschuining."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self) -> str:
        """De soort en tevens de omschrijving van dwarse markering."""
        return self._soortOmschrijving.get_waarde()

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)
