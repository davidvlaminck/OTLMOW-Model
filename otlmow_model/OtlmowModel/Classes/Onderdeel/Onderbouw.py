# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Laag import Laag
from ...Classes.Abstracten.LaagDikte import LaagDikte
from ...Classes.Abstracten.LaagProductidentificatiecode import LaagProductidentificatiecode
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcKrimpvoeg import DtcKrimpvoeg, DtcKrimpvoegWaarden
from ...Datatypes.KlGewaarborgdeWrijvingshoek import KlGewaarborgdeWrijvingshoek
from ...Datatypes.KlOnderbouwType import KlOnderbouwType
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderbouw(Laag, LaagDikte, LaagProductidentificatiecode):
    """Gedeelte dat onder de verhardingslagen ligt. Deze omvat de aanvulling,omhulling,onderfundering,fundering en de straatlaag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraagvermogen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDruksterkte', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', direction='i')  # i = direction: incoming

        self._isHerstel = OTLAttribuut(field=BooleanField,
                                       naam='isHerstel',
                                       label='is herstel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.isHerstel',
                                       definition='Aanduiding of de onderbouw laag is of wordt hersteld.',
                                       owner=self)

        self._krimpvoegen = OTLAttribuut(field=DtcKrimpvoeg,
                                         naam='krimpvoegen',
                                         label='krimpvoegen',
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
