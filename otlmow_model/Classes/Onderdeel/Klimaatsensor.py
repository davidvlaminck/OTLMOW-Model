# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlKlimaatsensorMerk import KlKlimaatsensorMerk
from otlmow_model.Datatypes.KlKlimaatsensorModelnaam import KlKlimaatsensorModelnaam
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Klimaatsensor(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een sensor die een of meer klimatologische variabelen van een ruimte meet zoals bv. temperatuur, luchtvochtigheid of luchtdruk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        SerienummerObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller')

        self._meetCO2 = OTLAttribuut(field=BooleanField,
                                     naam='meetCO2',
                                     label='meet CO2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor.meetCO2',
                                     definition='Geeft aan of het toestel het CO2 gehalte in de ruimte meet.',
                                     owner=self)

        self._meetFijnStof = OTLAttribuut(field=BooleanField,
                                          naam='meetFijnStof',
                                          label='meet fijn stof',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor.meetFijnStof',
                                          definition='Geeft aan of het toestel het gehalte aan fijn stof in de ruimte meet.',
                                          owner=self)

        self._meetLuchtdruk = OTLAttribuut(field=BooleanField,
                                           naam='meetLuchtdruk',
                                           label='meet luchtdruk',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor.meetLuchtdruk',
                                           definition='Geeft aan of het toestel de luchtdruk in de ruimte meet.',
                                           owner=self)

        self._meetTemperatuur = OTLAttribuut(field=BooleanField,
                                             naam='meetTemperatuur',
                                             label='meet temperatuur',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor.meetTemperatuur',
                                             definition='Geeft aan of het toestel de temperatuur in de ruimte meet.',
                                             owner=self)

        self._meetVochtigheid = OTLAttribuut(field=BooleanField,
                                             naam='meetVochtigheid',
                                             label='meet luchtvochtigheid',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor.meetVochtigheid',
                                             definition='Geeft aan of het toestel de luchtvochtigheid in de ruimte meet.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlKlimaatsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor.merk',
                                  definition='Het merk van de klimaatsensor',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlKlimaatsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimaatsensor.modelnaam',
                                       definition='Modelnaam van de klimaatsensor volgens de fabrikant.',
                                       owner=self)

    @property
    def meetCO2(self) -> bool:
        """Geeft aan of het toestel het CO2 gehalte in de ruimte meet."""
        return self._meetCO2.get_waarde()

    @meetCO2.setter
    def meetCO2(self, value):
        self._meetCO2.set_waarde(value, owner=self)

    @property
    def meetFijnStof(self) -> bool:
        """Geeft aan of het toestel het gehalte aan fijn stof in de ruimte meet."""
        return self._meetFijnStof.get_waarde()

    @meetFijnStof.setter
    def meetFijnStof(self, value):
        self._meetFijnStof.set_waarde(value, owner=self)

    @property
    def meetLuchtdruk(self) -> bool:
        """Geeft aan of het toestel de luchtdruk in de ruimte meet."""
        return self._meetLuchtdruk.get_waarde()

    @meetLuchtdruk.setter
    def meetLuchtdruk(self, value):
        self._meetLuchtdruk.set_waarde(value, owner=self)

    @property
    def meetTemperatuur(self) -> bool:
        """Geeft aan of het toestel de temperatuur in de ruimte meet."""
        return self._meetTemperatuur.get_waarde()

    @meetTemperatuur.setter
    def meetTemperatuur(self, value):
        self._meetTemperatuur.set_waarde(value, owner=self)

    @property
    def meetVochtigheid(self) -> bool:
        """Geeft aan of het toestel de luchtvochtigheid in de ruimte meet."""
        return self._meetVochtigheid.get_waarde()

    @meetVochtigheid.setter
    def meetVochtigheid(self, value):
        self._meetVochtigheid.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de klimaatsensor"""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de klimaatsensor volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
