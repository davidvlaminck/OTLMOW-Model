# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeDrempel import KlTypeDrempel
from ...Datatypes.KlVastAanslagmateriaal import KlVastAanslagmateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Drempel(AIMNaamObject, LijnGeometrie):
    """Vaste opstand op de bodem van het constructiehoofd over de breedte van de constructie voor de waterdichting en/of krachtoverdracht van de beweegbare waterkerende constructie (m.u.v. roldeuren)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Drempel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd', direction='o')  # o = direction: outgoing

        self._typeDrempel = OTLAttribuut(field=KlTypeDrempel,
                                         naam='typeDrempel',
                                         label='type drempel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Drempel.typeDrempel',
                                         definition='Vaste opstand op de bodem van het constructiehoofd over de breedte van de constructie voor de waterdichting en/of krachtoverdracht van de beweegbare waterkerende constructie (m.u.v. roldeuren).',
                                         owner=self)

        self._vastAanslagmateriaal = OTLAttribuut(field=KlVastAanslagmateriaal,
                                                  naam='vastAanslagmateriaal',
                                                  label='vast aanslagmateriaal',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Drempel.vastAanslagmateriaal',
                                                  definition='De verschillende mogelijkheden m.b.t. het materiaal van de aanslag',
                                                  owner=self)

    @property
    def typeDrempel(self) -> str:
        """Vaste opstand op de bodem van het constructiehoofd over de breedte van de constructie voor de waterdichting en/of krachtoverdracht van de beweegbare waterkerende constructie (m.u.v. roldeuren)."""
        return self._typeDrempel.get_waarde()

    @typeDrempel.setter
    def typeDrempel(self, value):
        self._typeDrempel.set_waarde(value, owner=self)

    @property
    def vastAanslagmateriaal(self) -> str:
        """De verschillende mogelijkheden m.b.t. het materiaal van de aanslag"""
        return self._vastAanslagmateriaal.get_waarde()

    @vastAanslagmateriaal.setter
    def vastAanslagmateriaal(self, value):
        self._vastAanslagmateriaal.set_waarde(value, owner=self)
