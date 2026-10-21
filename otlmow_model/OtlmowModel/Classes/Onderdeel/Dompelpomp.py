# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlDompelpompMerk import KlDompelpompMerk
from ...Datatypes.KlDompelpompModelnaam import KlDompelpompModelnaam
from ...Datatypes.KlNominaleSpanning import KlNominaleSpanning
from ...Datatypes.KwantWrdInKubiekeMeterPerUur import KwantWrdInKubiekeMeterPerUur, KwantWrdInKubiekeMeterPerUurWaarden
from ...Datatypes.KwantWrdInLiterPerMinuut import KwantWrdInLiterPerMinuut, KwantWrdInLiterPerMinuutWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dompelpomp(LinkendElement, NaampadObject, PuntGeometrie):
    """Een pomp die geheel in de te verpompen vloeistof wordt ondergedompeld. Ook klokpomp of onderwaterpomp genoemd. Voor kleinschalige dompelpompen gebruikt men ook de naam lekwaterpomp."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderstel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pompgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MotorVermogenskring', direction='i')  # i = direction: incoming

        self._binnenDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='binnenDiameter',
                                            label='binnendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.binnenDiameter',
                                            definition='Afmeting van de binnenkant van de opening waardoor het opgepompte water loopt.',
                                            owner=self)

        self._buitenDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitenDiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.buitenDiameter',
                                            definition='Afmeting van de buitenkant van de opening waarlangs het opgepompte water loopt in functie van een aansluiting van een afvoer.',
                                            owner=self)

        self._maximaalDebiet = OTLAttribuut(field=KwantWrdInLiterPerMinuut,
                                            naam='maximaalDebiet',
                                            label='maximaal debiet',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.maximaalDebiet',
                                            usagenote='Attribuut uit gebruik sinds versie 2.21.0 ',
                                            deprecated_version='2.21.0',
                                            definition='Het maximaal debiet dat de pomp kan leveren.',
                                            owner=self)

        self._maximaleOpvoerhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='maximaleOpvoerhoogte',
                                                  label='maximale opvoerhoogte',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.maximaleOpvoerhoogte',
                                                  usagenote='Attribuut uit gebruik sinds versie 2.21.0 ',
                                                  deprecated_version='2.21.0',
                                                  definition='De maximale hoogte die de pomp een vloeistof kan doen bereiken.',
                                                  owner=self)

        self._merk = OTLAttribuut(field=KlDompelpompMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.merk',
                                  definition='Het merk van de dompelpomp.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDompelpompModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.modelnaam',
                                       definition='De modelnaam van de dompelpomp.',
                                       owner=self)

        self._nominaleSpanning = OTLAttribuut(field=KlNominaleSpanning,
                                              naam='nominaleSpanning',
                                              label='nominale spanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.nominaleSpanning',
                                              definition='De nominale spanning van de dompelpomp.',
                                              owner=self)

        self._opvoerhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opvoerhoogte',
                                          label='opvoerhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.opvoerhoogte',
                                          definition='De verticale afstand tussen het vloeistofniveau aan de zuigzijde en het hoogste punt waar de vloeistof naartoe moet worden gepompt. Dit is de druk die de pomp moet leveren om de gewenste pompcapaciteit te bereiken, uitgedrukt in meter.',
                                          owner=self)

        self._pompcapaciteit = OTLAttribuut(field=KwantWrdInKubiekeMeterPerUur,
                                            naam='pompcapaciteit',
                                            label='pompcapaciteit',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.pompcapaciteit',
                                            definition='Het volume vloeistof dat de pomp per tijdseenheid verplaatst bij het nominale werkpunt, doorgaans uitgedrukt in kubieke meter per uur.',
                                            owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp.vermogen',
                                      definition='Elektrisch vermogen van het toestel volgens de specificaties van de fabrikant.',
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
        """Afmeting van de buitenkant van de opening waarlangs het opgepompte water loopt in functie van een aansluiting van een afvoer."""
        return self._buitenDiameter.get_waarde()

    @buitenDiameter.setter
    def buitenDiameter(self, value):
        self._buitenDiameter.set_waarde(value, owner=self)

    @property
    def maximaalDebiet(self) -> KwantWrdInLiterPerMinuutWaarden:
        """Het maximaal debiet dat de pomp kan leveren."""
        return self._maximaalDebiet.get_waarde()

    @maximaalDebiet.setter
    def maximaalDebiet(self, value):
        self._maximaalDebiet.set_waarde(value, owner=self)

    @property
    def maximaleOpvoerhoogte(self) -> KwantWrdInMeterWaarden:
        """De maximale hoogte die de pomp een vloeistof kan doen bereiken."""
        return self._maximaleOpvoerhoogte.get_waarde()

    @maximaleOpvoerhoogte.setter
    def maximaleOpvoerhoogte(self, value):
        self._maximaleOpvoerhoogte.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de dompelpomp."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de dompelpomp."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def nominaleSpanning(self) -> str:
        """De nominale spanning van de dompelpomp."""
        return self._nominaleSpanning.get_waarde()

    @nominaleSpanning.setter
    def nominaleSpanning(self, value):
        self._nominaleSpanning.set_waarde(value, owner=self)

    @property
    def opvoerhoogte(self) -> KwantWrdInMeterWaarden:
        """De verticale afstand tussen het vloeistofniveau aan de zuigzijde en het hoogste punt waar de vloeistof naartoe moet worden gepompt. Dit is de druk die de pomp moet leveren om de gewenste pompcapaciteit te bereiken, uitgedrukt in meter."""
        return self._opvoerhoogte.get_waarde()

    @opvoerhoogte.setter
    def opvoerhoogte(self, value):
        self._opvoerhoogte.set_waarde(value, owner=self)

    @property
    def pompcapaciteit(self) -> KwantWrdInKubiekeMeterPerUurWaarden:
        """Het volume vloeistof dat de pomp per tijdseenheid verplaatst bij het nominale werkpunt, doorgaans uitgedrukt in kubieke meter per uur."""
        return self._pompcapaciteit.get_waarde()

    @pompcapaciteit.setter
    def pompcapaciteit(self, value):
        self._pompcapaciteit.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInWattWaarden:
        """Elektrisch vermogen van het toestel volgens de specificaties van de fabrikant."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
