# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ZenderOntvangerToegang import ZenderOntvangerToegang
from ...Datatypes.KlOntvangerMerk import KlOntvangerMerk
from ...Datatypes.KlOntvangerModelnaam import KlOntvangerModelnaam
from ...Datatypes.KlOntvangerToepassing import KlOntvangerToepassing


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ontvanger(ZenderOntvangerToegang):
    """Toestel voor het opvangen van signalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zender', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij', direction='i')  # i = direction: incoming

        self._merk = OTLAttribuut(field=KlOntvangerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.merk',
                                  definition='Het merk van een ontvanger.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlOntvangerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.modelnaam',
                                       definition='De modelnaam/product range van een ontvanger.',
                                       owner=self)

        self._toepassing = OTLAttribuut(field=KlOntvangerToepassing,
                                        naam='toepassing',
                                        label='toepassing',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.toepassing',
                                        usagenote='Attribuut uit gebruik sinds versie 2.8.0 ',
                                        deprecated_version='2.8.0',
                                        definition='De techniek of standaard waarmee signalen over het netwerk verstuurd worden.',
                                        owner=self)

    @property
    def merk(self) -> str:
        """Het merk van een ontvanger."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van een ontvanger."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def toepassing(self) -> str:
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden."""
        return self._toepassing.get_waarde()

    @toepassing.setter
    def toepassing(self, value):
        self._toepassing.set_waarde(value, owner=self)
