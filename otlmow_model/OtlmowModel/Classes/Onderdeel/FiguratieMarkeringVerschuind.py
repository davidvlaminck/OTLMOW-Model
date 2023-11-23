# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from ...Datatypes.KlFiguratieCodeVerschuind import KlFiguratieCodeVerschuind
from ...Datatypes.KlFiguratieSoortVerschuind import KlFiguratieSoortVerschuind
from ...Datatypes.KlFiguratieTypeVerschuind import KlFiguratieTypeVerschuind
from ...Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class FiguratieMarkeringVerschuind(FiguratieMarkeringToegang, VlakGeometrie):
    """Een schuine markering als figuratie op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._basisOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                              naam='basisOppervlakte',
                                              label='basisoppervlakte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.basisOppervlakte',
                                              definition='De (basis) oppervlakte van de markering zoals beschreven in de algemene omzendbrief.',
                                              owner=self)

        self._code = OTLAttribuut(field=KlFiguratieCodeVerschuind,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.code',
                                  definition='De code van de verschuinde figuratie markering.',
                                  owner=self)

        self._hoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                  naam='hoek',
                                  label='hoek',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.hoek',
                                  definition='De hoek van de verschuinde figuratiemarkering in decimale graden.',
                                  owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.oppervlakte',
                                         definition='De oppervlakte van de figuratie markering na verschuining.',
                                         owner=self)

        self._soortOmschrijving = OTLAttribuut(field=KlFiguratieSoortVerschuind,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van de verschuinde figuratie markering.',
                                               owner=self)

        self._type = OTLAttribuut(field=KlFiguratieTypeVerschuind,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.type',
                                  definition='Het type van de verschuinde figuratie markering.',
                                  owner=self)

    @property
    def basisOppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De (basis) oppervlakte van de markering zoals beschreven in de algemene omzendbrief."""
        return self._basisOppervlakte.get_waarde()

    @basisOppervlakte.setter
    def basisOppervlakte(self, value):
        self._basisOppervlakte.set_waarde(value, owner=self)

    @property
    def code(self) -> str:
        """De code van de verschuinde figuratie markering."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def hoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """De hoek van de verschuinde figuratiemarkering in decimale graden."""
        return self._hoek.get_waarde()

    @hoek.setter
    def hoek(self, value):
        self._hoek.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de figuratie markering na verschuining."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self) -> str:
        """De soort en tevens de omschrijving van de verschuinde figuratie markering."""
        return self._soortOmschrijving.get_waarde()

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van de verschuinde figuratie markering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
