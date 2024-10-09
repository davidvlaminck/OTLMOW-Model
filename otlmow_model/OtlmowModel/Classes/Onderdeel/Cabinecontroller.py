# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Controller import Controller
from ...Datatypes.KlControllerBeveiligingssleutel import KlControllerBeveiligingssleutel
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cabinecontroller(Controller):
    """Controller die zorgt voor de bewaking en bediening van de geschakelde verlichtingsaftakkingen en voor bewaking van de voedingsinstallatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', direction='i')  # i = direction: incoming

        self._beveiligingssleutel = OTLAttribuut(field=KlControllerBeveiligingssleutel,
                                                 naam='beveiligingssleutel',
                                                 label='beveiligingssleutel',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller.beveiligingssleutel',
                                                 definition='De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.',
                                                 owner=self)

        self._merk = OTLAttribuut(field=StringField,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller.merk',
                                  definition='Merk van de cabinecontroller.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=StringField,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller.modelnaam',
                                       definition='Modelnaam van de cabinecontroller.',
                                       owner=self)

    @property
    def beveiligingssleutel(self) -> str:
        """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""
        return self._beveiligingssleutel.get_waarde()

    @beveiligingssleutel.setter
    def beveiligingssleutel(self, value):
        self._beveiligingssleutel.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk van de cabinecontroller."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de cabinecontroller."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
