# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm, DtcAfmetingBxlxhInMmWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlFietstelsysteemMerk import KlFietstelsysteemMerk
from ...Datatypes.KlFietstelsysteemModelnaam import KlFietstelsysteemModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fietstelsysteem(NaampadObject, PuntGeometrie):
    """Toestel bij de fietstelinstallatie dat gegevens van detectielussen over passerende fietsers verzamelt en verwerkt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fietstelinstallatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij', direction='i')  # i = direction: incoming

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.afmetingen',
                                        definition='De afmetingen van het fietstelsysteem.',
                                        owner=self)

        self._merk = OTLAttribuut(field=KlFietstelsysteemMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.merk',
                                  definition='Merknaam van het fietstelsysteem.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlFietstelsysteemModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.modelnaam',
                                       definition='Naam van het model van het fietstelsysteem volgens de fabrikant.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.technischeFiche',
                                             definition='Document met de technische specificaties van het fietstelsysteem.',
                                             owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlxhInMmWaarden:
        """De afmetingen van het fietstelsysteem."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van het fietstelsysteem."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam van het model van het fietstelsysteem volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Document met de technische specificaties van het fietstelsysteem."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
