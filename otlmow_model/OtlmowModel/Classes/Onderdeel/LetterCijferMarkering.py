# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from ...Datatypes.KlLetterCijfer import KlLetterCijfer
from ...Datatypes.KlLetterCijferType import KlLetterCijferType
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LetterCijferMarkering(FiguratieMarkeringToegang, PuntGeometrie):
    """Een markering bestaande uit individuele letters en/of cijfers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._letterCijfer = OTLAttribuut(field=KlLetterCijfer,
                                          naam='letterCijfer',
                                          label='letter-cijfer',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.letterCijfer',
                                          definition='De individuele letter of cijfer gebruikt bij de wegmarkering.',
                                          owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='basisoppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.oppervlakte',
                                         definition='De oppervlakte van de individuele letter- of cijfermarkering zoals beschreven in de algemene omzendbrief.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlLetterCijferType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.type',
                                  definition='Het type van de individuele letter- of cijfermarkering.',
                                  owner=self)

    @property
    def letterCijfer(self) -> str:
        """De individuele letter of cijfer gebruikt bij de wegmarkering."""
        return self._letterCijfer.get_waarde()

    @letterCijfer.setter
    def letterCijfer(self, value):
        self._letterCijfer.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de individuele letter- of cijfermarkering zoals beschreven in de algemene omzendbrief."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van de individuele letter- of cijfermarkering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
