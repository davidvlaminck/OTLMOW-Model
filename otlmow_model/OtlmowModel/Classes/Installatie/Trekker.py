# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlTypeTrekker import KlTypeTrekker
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trekker(TechnischDocument, AIMNaamObject, LijnGeometrie):
    """Een lineair mechanisch element, dubbelzijdig scharnierend, dat beoogd is om hoofdzakelijk op trek te belasten. Het verbindt, bijvoorbeeld, enerzijds het (bewegend) brugdeel/ beweegbare waterkerende constructie met anderzijds de lastzijde van de balansarm/bovenrolwagen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balans', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hefportiek', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Heftoren', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='o')  # o = direction: outgoing

        self._heeftVerendElement = OTLAttribuut(field=BooleanField,
                                                naam='heeftVerendElement',
                                                label='heeft verend element',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker.heeftVerendElement',
                                                definition='Geeft aan de trekker een verend element heeft of niet.',
                                                owner=self)

        self._type = OTLAttribuut(field=KlTypeTrekker,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker.type',
                                  definition='Het type van de trekker.',
                                  owner=self)

    @property
    def heeftVerendElement(self) -> bool:
        """Geeft aan de trekker een verend element heeft of niet."""
        return self._heeftVerendElement.get_waarde()

    @heeftVerendElement.setter
    def heeftVerendElement(self, value):
        self._heeftVerendElement.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van de trekker."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
