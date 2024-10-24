# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LEDBord import LEDBord
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlDynBordZ30Merk import KlDynBordZ30Merk
from ...Datatypes.KlDynBordZ30Modelnaam import KlDynBordZ30Modelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordZ30(LEDBord):
    """Dynamisch verkeersbord dat verkeerstekens voor een zone 30 kan weergeven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NetwerkModem', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting', direction='i')  # i = direction: incoming

        self._merk = OTLAttribuut(field=KlDynBordZ30Merk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30.merk',
                                  definition='Merk van het dynamisch zone-30 bord.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordZ30Modelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30.modelnaam',
                                       definition='De modelnaam van het Z30-bord.',
                                       owner=self)

        self._naastGenummerdeWeg = OTLAttribuut(field=BooleanField,
                                                naam='naastGenummerdeWeg',
                                                label='langs genummerde weg',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30.naastGenummerdeWeg',
                                                definition='Aanduiding of het bord naast een genummerde weg of een niet-genummerde weg staat, gericht naar het aankomende verkeer.',
                                                owner=self)

    @property
    def merk(self) -> str:
        """Merk van het dynamisch zone-30 bord."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het Z30-bord."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def naastGenummerdeWeg(self) -> bool:
        """Aanduiding of het bord naast een genummerde weg of een niet-genummerde weg staat, gericht naar het aankomende verkeer."""
        return self._naastGenummerdeWeg.get_waarde()

    @naastGenummerdeWeg.setter
    def naastGenummerdeWeg(self, value):
        self._naastGenummerdeWeg.set_waarde(value, owner=self)
