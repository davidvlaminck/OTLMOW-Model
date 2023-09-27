# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.TerreinDeel import TerreinDeel
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlWegbermBIO import KlWegbermBIO
from otlmow_model.Datatypes.KlWegbermType import KlWegbermType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegberm(TerreinDeel, AIMObject):
    """Gedeelte van het wegplatform dat buiten de rijbanen ligt. Een wegberm kan sloten en bijzonder ingerichte onderdelen bevatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement')

        self._bijzonderIngerichteOnderdelen = OTLAttribuut(field=KlWegbermBIO,
                                                           naam='bijzonderIngerichteOnderdelen',
                                                           label='bijzonder ingerichte onderdelen van de wegberm',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm.bijzonderIngerichteOnderdelen',
                                                           definition='De bijzonder ingerichte onderdelen van de wegberm.',
                                                           owner=self)

        self._type = OTLAttribuut(field=KlWegbermType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm.type',
                                  definition='Het type van wegberm.',
                                  owner=self)

    @property
    def bijzonderIngerichteOnderdelen(self) -> str:
        """De bijzonder ingerichte onderdelen van de wegberm."""
        return self._bijzonderIngerichteOnderdelen.get_waarde()

    @bijzonderIngerichteOnderdelen.setter
    def bijzonderIngerichteOnderdelen(self, value):
        self._bijzonderIngerichteOnderdelen.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van wegberm."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
