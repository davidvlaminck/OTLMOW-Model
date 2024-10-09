# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlNoodstopknopMerk import KlNoodstopknopMerk
from ...Datatypes.KlNoodstopknopModelnaam import KlNoodstopknopModelnaam
from ...Datatypes.KlNoodstopknopUitvoering import KlNoodstopknopUitvoering
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Noodstopknop(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een knop waarmee de werking van een machine of installatie koste wat het koste onmiddellijk stilgelegd wordt. Ook noodstopschakelaar genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodstopknop'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais', direction='u')  # u = unidirectional

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
                                        label='uitvoering',
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
