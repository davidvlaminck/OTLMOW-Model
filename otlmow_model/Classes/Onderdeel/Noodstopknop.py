# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlNoodstopknopMerk import KlNoodstopknopMerk
from otlmow_model.Datatypes.KlNoodstopknopModelnaam import KlNoodstopknopModelnaam
from otlmow_model.Datatypes.KlNoodstopknopUitvoering import KlNoodstopknopUitvoering


# Generated with OTLClassCreator. To modify: extend, do not edit
class Noodstopknop(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject):
    """Een knop waarmee de werking van een machine of installatie koste wat het koste onmiddellijk stilgelegd wordt. Ook noodstopschakelaar genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodstopknop'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        ElektrischComponentennummerObject.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais')

        self._merk = OTLAttribuut(field=KlNoodstopknopMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodstopknop.merk',
                                  definition='Het merk van de noodstopknop.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlNoodstopknopModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodstopknop.modelnaam',
                                       definition='De modelnaam van de noodstopknop.',
                                       owner=self)

        self._uitvoering = OTLAttribuut(field=KlNoodstopknopUitvoering,
                                        naam='uitvoering',
                                        label='Noodstop uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodstopknop.uitvoering',
                                        definition='Type volgens het werkingsprincipe van de knop of schakelaar.',
                                        owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de noodstopknop."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de noodstopknop."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def uitvoering(self) -> str:
        """Type volgens het werkingsprincipe van de knop of schakelaar."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
