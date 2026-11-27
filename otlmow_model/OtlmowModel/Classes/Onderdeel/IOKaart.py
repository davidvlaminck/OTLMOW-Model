# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.Abstracten.ElektrischComponentennummerObject import (
    ElektrischComponentennummerObject,
)
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlIOBitSnelheid import KlIOBitSnelheid
from ...Datatypes.KlIOKaartMerk import KlIOKaartMerk
from ...Datatypes.KlIOKaartModelnaam import KlIOKaartModelnaam
from ...Datatypes.KlIORichting import KlIORichting
from ...Datatypes.KlIOSignaaltype import KlIOSignaaltype
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IOKaart(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een kaart of module die gebruikt wordt voor de ingang of uitgang van een verwerkingseenheid (bv. een PLC). Op de IO-kaart worden perifere toestellen en sensoren aangesloten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Controlepaneel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynamischeVluchtwegindicatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gassensor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitControleUnit', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorsturing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Relais', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StroomMeetmodule', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Temperatuursensor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VentilatieAfsluitklep', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilatierooster', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VulpuntBrandweer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._bitsnelheid = OTLAttribuut(field=KlIOBitSnelheid,
                                         naam='bitsnelheid',
                                         label='bitsnelheid',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.bitsnelheid',
                                         definition='De snelheid (hoeveel bits per seconde) waarmee data doorgestuurd kan worden.',
                                         owner=self)

        self._firmwareversie = OTLAttribuut(field=StringField,
                                            naam='firmwareversie',
                                            label='firmwareversie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.firmwareversie',
                                            definition='Versie van de firmware.',
                                            owner=self)

        self._merk = OTLAttribuut(field=KlIOKaartMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.merk',
                                  definition='Het merk van de IO-kaart.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIOKaartModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.modelnaam',
                                       definition='De modelnaam van de IO-kaart.',
                                       owner=self)

        self._poortadres = OTLAttribuut(field=StringField,
                                        naam='poortadres',
                                        label='poortadres',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.poortadres',
                                        definition='Het IO-kaart poortadres wordt gebruikt om data uit te wisselen met een perifere component. Elke component krijgt een uniek poortadres toegekend, dit adres is een hexadecimaal getal.',
                                        owner=self)

        self._richting = OTLAttribuut(field=KlIORichting,
                                      naam='richting',
                                      label='richting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.richting',
                                      definition='Geeft aan of de IO-kaart dient voor input of output.',
                                      owner=self)

        self._signaalType = OTLAttribuut(field=KlIOSignaaltype,
                                         naam='signaalType',
                                         label='signaalType',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.signaalType',
                                         definition='Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiches als bijlage.',
                                             owner=self)

    @property
    def bitsnelheid(self) -> str:
        """De snelheid (hoeveel bits per seconde) waarmee data doorgestuurd kan worden."""
        return self._bitsnelheid.get_waarde()

    @bitsnelheid.setter
    def bitsnelheid(self, value):
        self._bitsnelheid.set_waarde(value, owner=self)

    @property
    def firmwareversie(self) -> str:
        """Versie van de firmware."""
        return self._firmwareversie.get_waarde()

    @firmwareversie.setter
    def firmwareversie(self, value):
        self._firmwareversie.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de IO-kaart."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de IO-kaart."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def poortadres(self) -> str:
        """Het IO-kaart poortadres wordt gebruikt om data uit te wisselen met een perifere component. Elke component krijgt een uniek poortadres toegekend, dit adres is een hexadecimaal getal."""
        return self._poortadres.get_waarde()

    @poortadres.setter
    def poortadres(self, value):
        self._poortadres.set_waarde(value, owner=self)

    @property
    def richting(self) -> str:
        """Geeft aan of de IO-kaart dient voor input of output."""
        return self._richting.get_waarde()

    @richting.setter
    def richting(self, value):
        self._richting.set_waarde(value, owner=self)

    @property
    def signaalType(self) -> str:
        """Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal."""
        return self._signaalType.get_waarde()

    @signaalType.setter
    def signaalType(self, value):
        self._signaalType.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> list[DtcDocumentWaarden]:
        """De technische fiches als bijlage."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
