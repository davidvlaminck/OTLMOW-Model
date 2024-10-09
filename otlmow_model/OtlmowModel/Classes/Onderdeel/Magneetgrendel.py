# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlAansluitingskabel import KlAansluitingskabel
from ...Datatypes.KlMagneetgrendelMerk import KlMagneetgrendelMerk
from ...Datatypes.KlMagneetgrendelModelnaam import KlMagneetgrendelModelnaam
from ...Datatypes.KwantWrdInKiloNewtonPerMeter import KwantWrdInKiloNewtonPerMeter, KwantWrdInKiloNewtonPerMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Magneetgrendel(AIMNaamObject, PuntGeometrie):
    """Een magnetisch slot dat instaat voor het gesloten houden van deuren, poorten, luiken met een elektromagneet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Magneetgrendel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TGCUitbreidingsModule', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller', direction='u')  # u = unidirectional

        self._aansluitingskabel = OTLAttribuut(field=KlAansluitingskabel,
                                               naam='aansluitingskabel',
                                               label='aansluitingskabel',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Magneetgrendel.aansluitingskabel',
                                               definition='Geeft aan of er een kabel / welk type kabel er gebruikt wordt om communicatie van en naar dit element mogelijk te maken.',
                                               owner=self)

        self._isBuiten = OTLAttribuut(field=BooleanField,
                                      naam='isBuiten',
                                      label='is buiten',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Magneetgrendel.isBuiten',
                                      definition='Geeft aan of de magneetgrendel zich binnen of buiten bevindt.',
                                      owner=self)

        self._merk = OTLAttribuut(field=KlMagneetgrendelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Magneetgrendel.merk',
                                  definition='Het merk van de magneetgrendel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlMagneetgrendelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Magneetgrendel.modelnaam',
                                       definition='De modelnaam van de magneetgrendel.',
                                       owner=self)

        self._sluitkracht = OTLAttribuut(field=KwantWrdInKiloNewtonPerMeter,
                                         naam='sluitkracht',
                                         label='sluitkracht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Magneetgrendel.sluitkracht',
                                         definition='Geeft de ingestelde kracht die moet uitgeoefend worden om de magneet te ontgrendelen.',
                                         owner=self)

    @property
    def aansluitingskabel(self) -> str:
        """Geeft aan of er een kabel / welk type kabel er gebruikt wordt om communicatie van en naar dit element mogelijk te maken."""
        return self._aansluitingskabel.get_waarde()

    @aansluitingskabel.setter
    def aansluitingskabel(self, value):
        self._aansluitingskabel.set_waarde(value, owner=self)

    @property
    def isBuiten(self) -> bool:
        """Geeft aan of de magneetgrendel zich binnen of buiten bevindt."""
        return self._isBuiten.get_waarde()

    @isBuiten.setter
    def isBuiten(self, value):
        self._isBuiten.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de magneetgrendel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de magneetgrendel."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def sluitkracht(self) -> KwantWrdInKiloNewtonPerMeterWaarden:
        """Geeft de ingestelde kracht die moet uitgeoefend worden om de magneet te ontgrendelen."""
        return self._sluitkracht.get_waarde()

    @sluitkracht.setter
    def sluitkracht(self, value):
        self._sluitkracht.set_waarde(value, owner=self)
