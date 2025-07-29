# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAdres import DtcAdres, DtcAdresWaarden
from ...Datatypes.KlNominaleSpanning import KlNominaleSpanning
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ForfaitaireAansluiting(AIMNaamObject, PuntGeometrie):
    """Een elektrische aansluiting waarbij met een forfaitair tarief gewerkt wordt,hierbij is er geen teller voorzien door de DNB."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='o')  # o = direction: outgoing

        self._adresVolgensDNB = OTLAttribuut(field=DtcAdres,
                                             naam='adresVolgensDNB',
                                             label='adres volgens DNB',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting.adresVolgensDNB',
                                             definition='Het adres van de aansluiting volgens de distributienetbeheerder.',
                                             owner=self)

        self._eanNummer = OTLAttribuut(field=StringField,
                                       naam='eanNummer',
                                       label='ean nummer',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting.eanNummer',
                                       definition='Uniek identificatienummer van de elektrische aansluiting, bestaande uit 18 cijfers.',
                                       owner=self)

        self._nominaleSpanning = OTLAttribuut(field=KlNominaleSpanning,
                                              naam='nominaleSpanning',
                                              label='nominale spanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting.nominaleSpanning',
                                              definition='De nominale spanning van de forfaitaire aansluiting.',
                                              owner=self)

        self._referentieDNB = OTLAttribuut(field=StringField,
                                           naam='referentieDNB',
                                           label='referentie distributienetbeheerder',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting.referentieDNB',
                                           definition='De wijze waarop, de referentie waarmee de aansluiting gekend is bij de distributienetbeheerder.',
                                           owner=self)

    @property
    def adresVolgensDNB(self) -> DtcAdresWaarden:
        """Het adres van de aansluiting volgens de distributienetbeheerder."""
        return self._adresVolgensDNB.get_waarde()

    @adresVolgensDNB.setter
    def adresVolgensDNB(self, value):
        self._adresVolgensDNB.set_waarde(value, owner=self)

    @property
    def eanNummer(self) -> str:
        """Uniek identificatienummer van de elektrische aansluiting, bestaande uit 18 cijfers."""
        return self._eanNummer.get_waarde()

    @eanNummer.setter
    def eanNummer(self, value):
        self._eanNummer.set_waarde(value, owner=self)

    @property
    def nominaleSpanning(self) -> str:
        """De nominale spanning van de forfaitaire aansluiting."""
        return self._nominaleSpanning.get_waarde()

    @nominaleSpanning.setter
    def nominaleSpanning(self, value):
        self._nominaleSpanning.set_waarde(value, owner=self)

    @property
    def referentieDNB(self) -> str:
        """De wijze waarop, de referentie waarmee de aansluiting gekend is bij de distributienetbeheerder."""
        return self._referentieDNB.get_waarde()

    @referentieDNB.setter
    def referentieDNB(self, value):
        self._referentieDNB.set_waarde(value, owner=self)
