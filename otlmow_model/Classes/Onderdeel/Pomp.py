# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.LinkendElement import LinkendElement
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlPompMerk import KlPompMerk
from otlmow_model.Datatypes.KlPompModelnaam import KlPompModelnaam
from otlmow_model.Datatypes.KlPompSoort import KlPompSoort
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pomp(LinkendElement, PuntGeometrie):
    """Een pomp is een werktuig dat water verplaatst door er energie aan af te geven in de vorm van een drukverhoging of snelheidsverhoging."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart')

        self._binnenDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='binnenDiameter',
                                            label='binnendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.binnenDiameter',
                                            definition='Afmeting van de binnenkant van de opening waardoor het opgepompte water loopt.',
                                            owner=self)

        self._buitenDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitenDiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.buitenDiameter',
                                            definition='Afmeting van de buitenkant van de opening waarlangs het opgepomte water loopt in functie van een aansluiting van een afvoer.',
                                            owner=self)

        self._maximaalDebiet = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                            naam='maximaalDebiet',
                                            label='maximaal debiet',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.maximaalDebiet',
                                            definition='Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant.',
                                            owner=self)

        self._merk = OTLAttribuut(field=KlPompMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.merk',
                                  definition='De naam van het merk volgens de fabrikant.',
                                  owner=self)

        self._metSoftstarter = OTLAttribuut(field=BooleanField,
                                            naam='metSoftstarter',
                                            label='met softstarter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.metSoftstarter',
                                            definition='Geeft aan of het toestel voorzien is van een eigen softstarter.',
                                            owner=self)

        self._metTempSensor = OTLAttribuut(field=BooleanField,
                                           naam='metTempSensor',
                                           label='met temperatuur sensor',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.metTempSensor',
                                           definition='Geeft aan of het toestel uitgerust is met een temperatuur sensor in functie van de bewaking van de correcte werking.',
                                           owner=self)

        self._metVochtsensor = OTLAttribuut(field=BooleanField,
                                            naam='metVochtsensor',
                                            label='met vocht sensor',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.metVochtsensor',
                                            definition='Geeft aan of het toestel uitgerust is met een vocht sensor in functie van de bewaking van de correcte werking.',
                                            owner=self)

        self._modelnaam = OTLAttribuut(field=KlPompModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.modelnaam',
                                       definition='Naam van het model van het toestel volgens de fabrikant.',
                                       owner=self)

        self._soort = OTLAttribuut(field=KlPompSoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.soort',
                                   definition='Bepaalt de aard van de pomp volgens haar werkingsprincipe.',
                                   owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.vermogen',
                                      definition='Elektrisch vermogen van het toestels volgens de specificaties van de fabrikant.',
                                      owner=self)

    @property
    def binnenDiameter(self) -> KwantWrdInMillimeterWaarden:
        """Afmeting van de binnenkant van de opening waardoor het opgepompte water loopt."""
        return self._binnenDiameter.get_waarde()

    @binnenDiameter.setter
    def binnenDiameter(self, value):
        self._binnenDiameter.set_waarde(value, owner=self)

    @property
    def buitenDiameter(self) -> KwantWrdInMillimeterWaarden:
        """Afmeting van de buitenkant van de opening waarlangs het opgepomte water loopt in functie van een aansluiting van een afvoer."""
        return self._buitenDiameter.get_waarde()

    @buitenDiameter.setter
    def buitenDiameter(self, value):
        self._buitenDiameter.set_waarde(value, owner=self)

    @property
    def maximaalDebiet(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant."""
        return self._maximaalDebiet.get_waarde()

    @maximaalDebiet.setter
    def maximaalDebiet(self, value):
        self._maximaalDebiet.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """De naam van het merk volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def metSoftstarter(self) -> bool:
        """Geeft aan of het toestel voorzien is van een eigen softstarter."""
        return self._metSoftstarter.get_waarde()

    @metSoftstarter.setter
    def metSoftstarter(self, value):
        self._metSoftstarter.set_waarde(value, owner=self)

    @property
    def metTempSensor(self) -> bool:
        """Geeft aan of het toestel uitgerust is met een temperatuur sensor in functie van de bewaking van de correcte werking."""
        return self._metTempSensor.get_waarde()

    @metTempSensor.setter
    def metTempSensor(self, value):
        self._metTempSensor.set_waarde(value, owner=self)

    @property
    def metVochtsensor(self) -> bool:
        """Geeft aan of het toestel uitgerust is met een vocht sensor in functie van de bewaking van de correcte werking."""
        return self._metVochtsensor.get_waarde()

    @metVochtsensor.setter
    def metVochtsensor(self, value):
        self._metVochtsensor.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam van het model van het toestel volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def soort(self) -> str:
        """Bepaalt de aard van de pomp volgens haar werkingsprincipe."""
        return self._soort.get_waarde()

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInWattWaarden:
        """Elektrisch vermogen van het toestels volgens de specificaties van de fabrikant."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
