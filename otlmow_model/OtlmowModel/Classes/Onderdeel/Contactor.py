# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.MotorVermogenskring import MotorVermogenskring
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlContactorMerk import KlContactorMerk
from ...Datatypes.KlContactorModelnaam import KlContactorModelnaam
from ...Datatypes.KlContactorType import KlContactorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Contactor(ElektrischComponentennummerObject, MotorVermogenskring, SerienummerObject, AIMObject):
    """Toestel dat ter plaatse of op afstand aangestuurd wordt om (grote) vermogensstromen af te schakelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MotorVermogenskring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais', direction='i')  # i = direction: incoming

        self._merk = OTLAttribuut(field=KlContactorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.merk',
                                  definition='Het merk van de contactor volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlContactorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.modelnaam',
                                       definition='De modelnaam van de contactor volgens de fabrikant.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlContactorType,
                                  naam='type',
                                  label='type contactor',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.type',
                                  definition='Geeft aan of het een K of Q contactor betreft.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de contactor volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de contactor volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Geeft aan of het een K of Q contactor betreft."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
