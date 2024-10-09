# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.DamplankAbstracte import DamplankAbstracte
from ...Classes.Abstracten.StalenConstructieElement import StalenConstructieElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlInbrengmethode import KlInbrengmethode
from ...Datatypes.KlLeveringsvorm import KlLeveringsvorm
from ...Datatypes.KlStalenDamplankvorm import KlStalenDamplankvorm
from ...Datatypes.KwantWrdInKubiekeCentimeterPerMeter import KwantWrdInKubiekeCentimeterPerMeter, KwantWrdInKubiekeCentimeterPerMeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenDamplank(DamplankAbstracte, StalenConstructieElement):
    """Slank geprofileerd stalen profiel, op de uiteindes voorzien van "sloten" om de planken met elkaar te verbinden en zodoende een continu gronddicht scherm te vormen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenCaisson', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._elastischWeerstandsmoment = OTLAttribuut(field=KwantWrdInKubiekeCentimeterPerMeter,
                                                       naam='elastischWeerstandsmoment',
                                                       label='elastisch weerstandsmoment',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank.elastischWeerstandsmoment',
                                                       definition='Maximale elastische spanning. Als de damplank Z- of U-vormig is, dan gaat het elastisch weerstandsmoment over de dubbele plank.',
                                                       owner=self)

        self._inbrengmethode = OTLAttribuut(field=KlInbrengmethode,
                                            naam='inbrengmethode',
                                            label='inbrengmethode',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank.inbrengmethode',
                                            definition='Manier waarop de damplank wordt ingebracht.',
                                            owner=self)

        self._isWarmgewalsd = OTLAttribuut(field=BooleanField,
                                           naam='isWarmgewalsd',
                                           label='is warmgewalsd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank.isWarmgewalsd',
                                           definition='Geeft aan of de stalen damplank, warmgewalsd is. Indien niet is het koudgewalsd.',
                                           owner=self)

        self._leveringsvorm = OTLAttribuut(field=KlLeveringsvorm,
                                           naam='leveringsvorm',
                                           label='leveringsvorm',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank.leveringsvorm',
                                           definition='Keuzelijst om aan te geven op welke manier de planken geleverd worden.',
                                           owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank.oppervlakte',
                                         definition='De oppervlakte van de plank in vierkante meter.',
                                         owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank.serienummer',
                                         definition='Het serienummer van de stalen damplank. Deze omvat uitgebreide info over o.a. het weerstandsmoment, de vorm,...',
                                         owner=self)

        self._vorm = OTLAttribuut(field=KlStalenDamplankvorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank.vorm',
                                  definition='Keuzelijst om aan te geven welke geometrie de plank hebben.',
                                  owner=self)

    @property
    def elastischWeerstandsmoment(self) -> KwantWrdInKubiekeCentimeterPerMeterWaarden:
        """Maximale elastische spanning. Als de damplank Z- of U-vormig is, dan gaat het elastisch weerstandsmoment over de dubbele plank."""
        return self._elastischWeerstandsmoment.get_waarde()

    @elastischWeerstandsmoment.setter
    def elastischWeerstandsmoment(self, value):
        self._elastischWeerstandsmoment.set_waarde(value, owner=self)

    @property
    def inbrengmethode(self) -> str:
        """Manier waarop de damplank wordt ingebracht."""
        return self._inbrengmethode.get_waarde()

    @inbrengmethode.setter
    def inbrengmethode(self, value):
        self._inbrengmethode.set_waarde(value, owner=self)

    @property
    def isWarmgewalsd(self) -> bool:
        """Geeft aan of de stalen damplank, warmgewalsd is. Indien niet is het koudgewalsd."""
        return self._isWarmgewalsd.get_waarde()

    @isWarmgewalsd.setter
    def isWarmgewalsd(self, value):
        self._isWarmgewalsd.set_waarde(value, owner=self)

    @property
    def leveringsvorm(self) -> str:
        """Keuzelijst om aan te geven op welke manier de planken geleverd worden."""
        return self._leveringsvorm.get_waarde()

    @leveringsvorm.setter
    def leveringsvorm(self, value):
        self._leveringsvorm.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de plank in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Het serienummer van de stalen damplank. Deze omvat uitgebreide info over o.a. het weerstandsmoment, de vorm,..."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """Keuzelijst om aan te geven welke geometrie de plank hebben."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
