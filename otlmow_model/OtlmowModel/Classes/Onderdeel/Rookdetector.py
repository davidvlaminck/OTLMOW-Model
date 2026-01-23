# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMerkRookdetector import KlMerkRookdetector
from ...Datatypes.KlModelnaamRookdetector import KlModelnaamRookdetector
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rookdetector(AIMNaamObject, PuntGeometrie):
    """Een sensor die via een optisch of ionisatieprincipe de aanwezigheid van rookdeeltjes signaleert om vroegtijdig brand te detecteren en een alarm te activeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rookdetector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlMerkRookdetector,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rookdetector.merk',
                                  definition='Het merk van de rookdetector.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlModelnaamRookdetector,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rookdetector.modelnaam',
                                       definition='De modelnaam van de rookdetector.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rookdetector.technischeFiche',
                                             definition='De technische fiche van de rookdetector.',
                                             owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de rookdetector."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de rookdetector."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de rookdetector."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
