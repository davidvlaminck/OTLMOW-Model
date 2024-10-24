# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Controller import Controller
from ...Datatypes.KlControllerBeveiligingssleutel import KlControllerBeveiligingssleutel
from ...Datatypes.KlSegmentcontrollerMerk import KlSegmentcontrollerMerk
from ...Datatypes.KlSegmentcontrollerModelnaam import KlSegmentcontrollerModelnaam
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Segmentcontroller(Controller):
    """Controller die zorgt voor de bewaking en bediening van verlichtingssegmenten per paal en aldus zorgt voor de communicatie tussen de cabine en de armatuurcontrollers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

        self._beveil_igingssleutel = OTLAttribuut(field=KlControllerBeveiligingssleutel,
                                                  naam='beveil_igingssleutel',
                                                  label='beveiligingssleutel',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveil_igingssleutel',
                                                  usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                                  deprecated_version='2.0.0',
                                                  definition='De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.',
                                                  owner=self)

        self._beveiligingssleutel = OTLAttribuut(field=KlControllerBeveiligingssleutel,
                                                 naam='beveiligingssleutel',
                                                 label='beveiligingssleutel',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveiligingssleutel',
                                                 definition='De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.',
                                                 owner=self)

        self._merk = OTLAttribuut(field=StringField,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.merk',
                                  usagenote='Attribuut uit gebruik sinds versie 2.8.0 ',
                                  deprecated_version='2.8.0',
                                  definition='Merk van de segmentcontroller.',
                                  owner=self)

        self._merknaam = OTLAttribuut(field=KlSegmentcontrollerMerk,
                                      naam='merknaam',
                                      label='merk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.merknaam',
                                      definition='Merk van de segmentcontroller.',
                                      owner=self)

        self._model = OTLAttribuut(field=KlSegmentcontrollerModelnaam,
                                   naam='model',
                                   label='modelnaam',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.model',
                                   definition='Modelnaam van de segmentcontroller.',
                                   owner=self)

        self._modelnaam = OTLAttribuut(field=StringField,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.modelnaam',
                                       usagenote='Attribuut uit gebruik sinds versie 2.8.0 ',
                                       deprecated_version='2.8.0',
                                       definition='Modelnaam van de segmentcontroller.',
                                       owner=self)

    @property
    def beveil_igingssleutel(self) -> str:
        """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""
        return self._beveil_igingssleutel.get_waarde()

    @beveil_igingssleutel.setter
    def beveil_igingssleutel(self, value):
        self._beveil_igingssleutel.set_waarde(value, owner=self)

    @property
    def beveiligingssleutel(self) -> str:
        """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""
        return self._beveiligingssleutel.get_waarde()

    @beveiligingssleutel.setter
    def beveiligingssleutel(self, value):
        self._beveiligingssleutel.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk van de segmentcontroller."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def merknaam(self) -> str:
        """Merk van de segmentcontroller."""
        return self._merknaam.get_waarde()

    @merknaam.setter
    def merknaam(self, value):
        self._merknaam.set_waarde(value, owner=self)

    @property
    def model(self) -> str:
        """Modelnaam van de segmentcontroller."""
        return self._model.get_waarde()

    @model.setter
    def model(self, value):
        self._model.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de segmentcontroller."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
