# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlAansluitingskabel import KlAansluitingskabel
from ...Datatypes.KlAlgFaalmodusType import KlAlgFaalmodusType
from ...Datatypes.KlSlotGebruik import KlSlotGebruik
from ...Datatypes.KlSlotMerk import KlSlotMerk
from ...Datatypes.KlSlotModelnaam import KlSlotModelnaam
from ...Datatypes.KlSlotType import KlSlotType
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slot(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Onderdeel van het slotmechanisme dat instaat voor het gesloten houden van deuren, poorten, luiken. Dit is zonder de cilinder."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slotcilinder', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockermanagementmodule', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TGCUitbreidingsModule', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller', direction='u')  # u = unidirectional

        self._aansluitingskabel = OTLAttribuut(field=KlAansluitingskabel,
                                               naam='aansluitingskabel',
                                               label='aansluitingskabel',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.aansluitingskabel',
                                               definition='Geeft aan of er een kabel / welk type kabel er gebruikt wordt om communicatie van en naar dit element mogelijk te maken.',
                                               owner=self)

        self._asafstand = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='asafstand',
                                       label='asafstand',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.asafstand',
                                       definition='De afstand tussen het midden van de as van het sleutel- of cilindergat en het midden van de as van het krukgat. Wordt ook wel entre-axe genoemd.',
                                       owner=self)

        self._doornmaat = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='doornmaat',
                                       label='doornmaat',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.doornmaat',
                                       definition='De afstand tussen de voorplaat en het midden van de as van het krukgat. Wordt ook wel entree genoemd.',
                                       owner=self)

        self._faalmodus = OTLAttribuut(field=KlAlgFaalmodusType,
                                       naam='faalmodus',
                                       label='faalmodus',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.faalmodus',
                                       definition='Geeft de faalmodus van het slot aan. Is het slot fail-safe, dan kan je bij een stroompanne steeds binnen en buiten. Is het slot fail-secure, dan gaat die bij een stroompanne op slot.',
                                       owner=self)

        self._heeftMeerpuntsvergrendeling = OTLAttribuut(field=BooleanField,
                                                         naam='heeftMeerpuntsvergrendeling',
                                                         label='heeft meerpuntsvergrendeling',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.heeftMeerpuntsvergrendeling',
                                                         definition='Geeft aan of het slot meerpuntsvergrendeld is.',
                                                         owner=self)

        self._merk = OTLAttribuut(field=KlSlotMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.merk',
                                  definition='Het merk van het slot.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSlotModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.modelnaam',
                                       definition='De modelnaam van het slot.',
                                       owner=self)

        self._slotGebruik = OTLAttribuut(field=KlSlotGebruik,
                                         naam='slotGebruik',
                                         label='slot gebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.slotGebruik',
                                         definition='Geeft aan langs welke kan het slot bruikbaar is. Hierbij kijk je naar de deur vanuit de kant dat je hem open kan duwen. Een slot kan gemaakt zijn om ofwel links, ofwel rechts geïnstalleerd te worden, of kan voor beide kanten bruikbaar zijn.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlSlotType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.type',
                                  definition='Het type slot.',
                                  owner=self)

        self._uitvoering = OTLAttribuut(field=StringField,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot.uitvoering',
                                        definition='Vrij invulveld voor verdere specificatie van hoe het slot is uitgevoerd.',
                                        owner=self)

    @property
    def aansluitingskabel(self) -> str:
        """Geeft aan of er een kabel / welk type kabel er gebruikt wordt om communicatie van en naar dit element mogelijk te maken."""
        return self._aansluitingskabel.get_waarde()

    @aansluitingskabel.setter
    def aansluitingskabel(self, value):
        self._aansluitingskabel.set_waarde(value, owner=self)

    @property
    def asafstand(self) -> KwantWrdInMillimeterWaarden:
        """De afstand tussen het midden van de as van het sleutel- of cilindergat en het midden van de as van het krukgat. Wordt ook wel entre-axe genoemd."""
        return self._asafstand.get_waarde()

    @asafstand.setter
    def asafstand(self, value):
        self._asafstand.set_waarde(value, owner=self)

    @property
    def doornmaat(self) -> KwantWrdInMillimeterWaarden:
        """De afstand tussen de voorplaat en het midden van de as van het krukgat. Wordt ook wel entree genoemd."""
        return self._doornmaat.get_waarde()

    @doornmaat.setter
    def doornmaat(self, value):
        self._doornmaat.set_waarde(value, owner=self)

    @property
    def faalmodus(self) -> str:
        """Geeft de faalmodus van het slot aan. Is het slot fail-safe, dan kan je bij een stroompanne steeds binnen en buiten. Is het slot fail-secure, dan gaat die bij een stroompanne op slot."""
        return self._faalmodus.get_waarde()

    @faalmodus.setter
    def faalmodus(self, value):
        self._faalmodus.set_waarde(value, owner=self)

    @property
    def heeftMeerpuntsvergrendeling(self) -> bool:
        """Geeft aan of het slot meerpuntsvergrendeld is."""
        return self._heeftMeerpuntsvergrendeling.get_waarde()

    @heeftMeerpuntsvergrendeling.setter
    def heeftMeerpuntsvergrendeling(self, value):
        self._heeftMeerpuntsvergrendeling.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het slot."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het slot."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def slotGebruik(self) -> str:
        """Geeft aan langs welke kan het slot bruikbaar is. Hierbij kijk je naar de deur vanuit de kant dat je hem open kan duwen. Een slot kan gemaakt zijn om ofwel links, ofwel rechts geïnstalleerd te worden, of kan voor beide kanten bruikbaar zijn."""
        return self._slotGebruik.get_waarde()

    @slotGebruik.setter
    def slotGebruik(self, value):
        self._slotGebruik.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type slot."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def uitvoering(self) -> str:
        """Vrij invulveld voor verdere specificatie van hoe het slot is uitgevoerd."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
