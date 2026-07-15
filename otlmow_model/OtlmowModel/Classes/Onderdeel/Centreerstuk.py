# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalCentreerstuk import KlMateriaalCentreerstuk


# Generated with OTLClassCreator. To modify: extend, do not edit
class Centreerstuk(AIMNaamObject):
    """Het invallende onderdeel van een centreermechanisme dat in een centreervork geleid wordt om een beweegbare constructie nauwkeurig te positioneren ten opzichte van een vast of ander beweegbaar deel. Dit onderdeel kan voorzien zijn van een rol."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Centreerstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AsLagerCombinatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DraagstructuurBWCTWC', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Centreermechanisme', direction='o')  # o = direction: outgoing

        self._materiaal = OTLAttribuut(field=KlMateriaalCentreerstuk,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Centreerstuk.materiaal',
                                       definition='Het materiaal van het centreerstuk.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal van het centreerstuk."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
