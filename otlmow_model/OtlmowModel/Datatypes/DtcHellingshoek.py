# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from ..Datatypes.KlRichtingHellingshoek import KlRichtingHellingshoek
from ..Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHellingshoekWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._hoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                  naam='hoek',
                                  label='hoek',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHellingshoek.hoek',
                                  usagenote='Attribuut uit gebruik sinds versie 2.16.0 ',
                                  deprecated_version='2.16.0',
                                  definition='Hoek van het ingebrachte anker in decimale graden.',
                                  owner=self)

        self._hoekHorizontaleAs = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                               naam='hoekHorizontaleAs',
                                               label='hoek t.o.v. horizontale as',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHellingshoek.hoekHorizontaleAs',
                                               definition='De hellingshoek die wordt gemeten ten opzichte van een horizontale as.',
                                               owner=self)

        self._hoekVerticaleAs = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                             naam='hoekVerticaleAs',
                                             label='hoek t.o.v. verticale as',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHellingshoek.hoekVerticaleAs',
                                             definition='De hellingshoek die wordt gemeten ten opzichte van een verticale as.',
                                             owner=self)

        self._richtingHellingshoek = OTLAttribuut(field=KlRichtingHellingshoek,
                                                  naam='richtingHellingshoek',
                                                  label='richting hellingshoek',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHellingshoek.richtingHellingshoek',
                                                  usagenote='Attribuut uit gebruik sinds versie 2.16.0 ',
                                                  deprecated_version='2.16.0',
                                                  definition='Geeft de richting van de hoek t.o.v. de as aan.',
                                                  owner=self)

    @property
    def hoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """Hoek van het ingebrachte anker in decimale graden."""
        return self._hoek.get_waarde()

    @hoek.setter
    def hoek(self, value):
        self._hoek.set_waarde(value, owner=self._parent)

    @property
    def hoekHorizontaleAs(self) -> KwantWrdInDecimaleGradenWaarden:
        """De hellingshoek die wordt gemeten ten opzichte van een horizontale as."""
        return self._hoekHorizontaleAs.get_waarde()

    @hoekHorizontaleAs.setter
    def hoekHorizontaleAs(self, value):
        self._hoekHorizontaleAs.set_waarde(value, owner=self._parent)

    @property
    def hoekVerticaleAs(self) -> KwantWrdInDecimaleGradenWaarden:
        """De hellingshoek die wordt gemeten ten opzichte van een verticale as."""
        return self._hoekVerticaleAs.get_waarde()

    @hoekVerticaleAs.setter
    def hoekVerticaleAs(self, value):
        self._hoekVerticaleAs.set_waarde(value, owner=self._parent)

    @property
    def richtingHellingshoek(self) -> str:
        """Geeft de richting van de hoek t.o.v. de as aan."""
        return self._richtingHellingshoek.get_waarde()

    @richtingHellingshoek.setter
    def richtingHellingshoek(self, value):
        self._richtingHellingshoek.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHellingshoek(ComplexField):
    """Complex datatype dat informatie bevat over de helling van de hoek alsook de richitng t.o.v. de as."""
    naam = 'DtcHellingshoek'
    label = 'Complex datatype hellingshoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHellingshoek'
    definition = 'Complex datatype dat informatie bevat over de helling van de hoek alsook de richitng t.o.v. de as.'
    waardeObject = DtcHellingshoekWaarden

    def __str__(self):
        return ComplexField.__str__(self)

