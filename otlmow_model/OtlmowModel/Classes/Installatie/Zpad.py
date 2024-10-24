# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ...Datatypes.KlZpadType import KlZpadType
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zpad(NaampadObject, GeenGeometrie):
    """End-to-end gebruikersverbinding over het transport netwerk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerkProtectie', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='i')  # i = direction: incoming

        self._WANCapaciteit = OTLAttribuut(field=IntegerField,
                                           naam='WANCapaciteit',
                                           label='wan capaciteit',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.WANCapaciteit',
                                           definition='Capaciteit van de verbinding vanuit het standpunt van de gebruiker.',
                                           owner=self)

        self._netwerkklant = OTLAttribuut(field=StringField,
                                          naam='netwerkklant',
                                          label='netwerkklant',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.netwerkklant',
                                          definition='Naam van de organisatie van de gebruiker.',
                                          owner=self)

        self._omschrijving = OTLAttribuut(field=StringField,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.omschrijving',
                                          definition='Beschrijving van de aard en/of doel van de verbinding.',
                                          owner=self)

        self._type = OTLAttribuut(field=KlZpadType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.type',
                                  definition='De soort verbinding, gebaseerd op het gebruikte protocol.',
                                  owner=self)

    @property
    def WANCapaciteit(self) -> int:
        """Capaciteit van de verbinding vanuit het standpunt van de gebruiker."""
        return self._WANCapaciteit.get_waarde()

    @WANCapaciteit.setter
    def WANCapaciteit(self, value):
        self._WANCapaciteit.set_waarde(value, owner=self)

    @property
    def netwerkklant(self) -> str:
        """Naam van de organisatie van de gebruiker."""
        return self._netwerkklant.get_waarde()

    @netwerkklant.setter
    def netwerkklant(self, value):
        self._netwerkklant.set_waarde(value, owner=self)

    @property
    def omschrijving(self) -> str:
        """Beschrijving van de aard en/of doel van de verbinding."""
        return self._omschrijving.get_waarde()

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De soort verbinding, gebaseerd op het gebruikte protocol."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
