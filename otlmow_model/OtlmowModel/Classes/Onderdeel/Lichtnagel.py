# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.EMAfbakening import EMAfbakening
from ...BaseClasses.BooleanField import BooleanField
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtnagel(EMAfbakening, PuntGeometrie):
    """Een lage, gele, plastic koepel die geplaatst wordt op een ondergronds geïnstalleerde, lichtgevende module waardoor de weggebruiker de indruk heeft dat de koepel zelf verlicht is. De koepel kan ook geïntegreerde LEDjes bevatten om op te lichten in plaats van boven een lichtgevende module gezet te worden. Deze voorwerpen hebben als doel de weggebruiker attent te maken van een gewijzigde wegprofiel (bv. betonnen middeneiland op de weg,...)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtnagel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VRIBuiteninstallatie', direction='o')  # o = direction: outgoing

        self._isLED = OTLAttribuut(field=BooleanField,
                                   naam='isLED',
                                   label='is LED',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtnagel.isLED',
                                   definition='Geeft aan of de lichtnagel opgelicht wordt door middel van geïntegreerde LEDs.',
                                   owner=self)

    @property
    def isLED(self) -> bool:
        """Geeft aan of de lichtnagel opgelicht wordt door middel van geïntegreerde LEDs."""
        return self._isLED.get_waarde()

    @isLED.setter
    def isLED(self, value):
        self._isLED.set_waarde(value, owner=self)
