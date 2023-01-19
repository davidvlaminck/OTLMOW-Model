# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Laag import Laag
from otlmow_model.Classes.Abstracten.LaagDikte import LaagDikte
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcKrimpvoeg import DtcKrimpvoeg, DtcKrimpvoegWaarden
from otlmow_model.Datatypes.KlGewaarborgdeWrijvingshoek import KlGewaarborgdeWrijvingshoek
from otlmow_model.Datatypes.KlOnderbouwType import KlOnderbouwType
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderbouw(Laag, LaagDikte):
    """Gedeelte van het baanlichaam dat tussen het baanbed en de verharding ligt. Deze omvat onderfundering,fundering en de straatlaag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Laag.__init__(self)
        LaagDikte.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._isHerstel = OTLAttribuut(field=BooleanField,
                                       naam='isHerstel',
                                       label='is herstel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.isHerstel',
                                       definition='Aanduiding of de onderbouw laag is of wordt hersteld.',
                                       owner=self)

        self._krimpvoegen = OTLAttribuut(field=DtcKrimpvoeg,
                                         naam='krimpvoegen',
                                         label='Krimpvoegen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.krimpvoegen',
                                         definition='Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlOnderbouwType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.type',
                                  definition='Het type van onderbouw.',
                                  owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.volume',
                                    definition='Het volume van onderbouw in kubieke meter.',
                                    owner=self)

        self._wrijvingshoek = OTLAttribuut(field=KlGewaarborgdeWrijvingshoek,
                                           naam='wrijvingshoek',
                                           label='wrijvingshoek',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.wrijvingshoek',
                                           definition='De hoek van inwendige wrijving geeft een aanwijzing omtrent de afschuifkarakteristieken en wordt dan ook gebruikt bij berekening van afschuiving, gronddruk en draagvermogen van paalfunderingen.',
                                           owner=self)

    @property
    def isHerstel(self) -> bool:
        """Aanduiding of de onderbouw laag is of wordt hersteld."""
        return self._isHerstel.get_waarde()

    @isHerstel.setter
    def isHerstel(self, value):
        self._isHerstel.set_waarde(value, owner=self)

    @property
    def krimpvoegen(self) -> DtcKrimpvoegWaarden:
        """Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat."""
        return self._krimpvoegen.get_waarde()

    @krimpvoegen.setter
    def krimpvoegen(self, value):
        self._krimpvoegen.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van onderbouw."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van onderbouw in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)

    @property
    def wrijvingshoek(self) -> str:
        """De hoek van inwendige wrijving geeft een aanwijzing omtrent de afschuifkarakteristieken en wordt dan ook gebruikt bij berekening van afschuiving, gronddruk en draagvermogen van paalfunderingen."""
        return self._wrijvingshoek.get_waarde()

    @wrijvingshoek.setter
    def wrijvingshoek(self, value):
        self._wrijvingshoek.set_waarde(value, owner=self)
