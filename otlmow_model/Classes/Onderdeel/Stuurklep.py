# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlStuurklepMerk import KlStuurklepMerk
from otlmow_model.Datatypes.KlStuurklepModelnaam import KlStuurklepModelnaam
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stuurklep(AIMNaamObject, PuntGeometrie):
    """Een afsluiter die vanop afstand bediend wordt om te bepalen of er al of niet vloeistof of gas door de leiding stroomt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuurklep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC')

        self._merk = OTLAttribuut(field=KlStuurklepMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuurklep.merk',
                                  definition='De merknaam van de stuurklep.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlStuurklepModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuurklep.modelnaam',
                                       definition='De modelnaam van de stuurklep.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuurklep.technischeFiche',
                                             definition='Technische fiche van de stuurklep.',
                                             owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de stuurklep."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de stuurklep."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Technische fiche van de stuurklep."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
