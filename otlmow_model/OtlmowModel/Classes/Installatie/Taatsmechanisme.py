# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlTypeMechanisme import KlTypeMechanisme


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taatsmechanisme(Geleidingsmechanisme, AIMObject):
    """Wordt gebruikt om bouwkundige constructies, zoals een puntdeur, draaideur of draaibrug, te geleiden. De geleiding omvat voornamelijk rotatie en soms ook translatie. Daarnaast vervult het een dragende functie met betrekking tot de sluisdeur."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspot', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatsschoen', direction='i')  # i = direction: incoming

        self._isRegelbaar = OTLAttribuut(field=BooleanField,
                                         naam='isRegelbaar',
                                         label='is regelbaar',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme.isRegelbaar',
                                         definition='Geeft aan of het taatsmechanisme regelbaar is of niet.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlTypeMechanisme,
                                  naam='type',
                                  label='type mechanisme',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme.type',
                                  definition='Geeft de verschillende types taatsmechanismen aan.',
                                  owner=self)

    @property
    def isRegelbaar(self) -> bool:
        """Geeft aan of het taatsmechanisme regelbaar is of niet."""
        return self._isRegelbaar.get_waarde()

    @isRegelbaar.setter
    def isRegelbaar(self, value):
        self._isRegelbaar.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Geeft de verschillende types taatsmechanismen aan."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
