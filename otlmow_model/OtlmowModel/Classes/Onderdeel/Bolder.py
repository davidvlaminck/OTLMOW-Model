# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.Abstracten.DetaiplanObject import DetaiplanObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalBolder import KlMateriaalBolder
from ...Datatypes.KlTypeBevestigingBolder import KlTypeBevestigingBolder
from ...Datatypes.KlTypeBolder import KlTypeBolder
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bolder(AanhorigheidSluisStuw, DetaiplanObject, AIMNaamObject, PuntGeometrie):
    """Een bolder is een aanmeervoorziening voor schepen geplaatst bovenop een constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bolder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief', direction='u')  # u = unidirectional

        self._materiaalBolder = OTLAttribuut(field=KlMateriaalBolder,
                                             naam='materiaalBolder',
                                             label='materiaal bolder',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bolder.materiaalBolder',
                                             definition='Het gebruikte materiaal voor de bolder.',
                                             owner=self)

        self._materiaalVerankeringBolder = OTLAttribuut(field=StringField,
                                                        naam='materiaalVerankeringBolder',
                                                        label='materiaal verankering bolder',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bolder.materiaalVerankeringBolder',
                                                        definition='Het type van materiaal van de verankering van de bolder (Bijv: 42CrMo4QT,..).',
                                                        owner=self)

        self._maximaleTroskracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                naam='maximaleTroskracht',
                                                label='maximale troskracht',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bolder.maximaleTroskracht',
                                                definition='De maximale troskracht, uitgedrukt in kN(Karakteristieke waarde).',
                                                owner=self)

        self._typeBevestiging = OTLAttribuut(field=KlTypeBevestigingBolder,
                                             naam='typeBevestiging',
                                             label='type bevestiging',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bolder.typeBevestiging',
                                             definition='De verschillende bevestigingsmiddellen van een bolder.',
                                             owner=self)

        self._typeBolder = OTLAttribuut(field=KlTypeBolder,
                                        naam='typeBolder',
                                        label='type bolder',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bolder.typeBolder',
                                        definition='De verschillende types bolder.',
                                        owner=self)

    @property
    def materiaalBolder(self) -> str:
        """Het gebruikte materiaal voor de bolder."""
        return self._materiaalBolder.get_waarde()

    @materiaalBolder.setter
    def materiaalBolder(self, value):
        self._materiaalBolder.set_waarde(value, owner=self)

    @property
    def materiaalVerankeringBolder(self) -> str:
        """Het type van materiaal van de verankering van de bolder (Bijv: 42CrMo4QT,..)."""
        return self._materiaalVerankeringBolder.get_waarde()

    @materiaalVerankeringBolder.setter
    def materiaalVerankeringBolder(self, value):
        self._materiaalVerankeringBolder.set_waarde(value, owner=self)

    @property
    def maximaleTroskracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De maximale troskracht, uitgedrukt in kN(Karakteristieke waarde)."""
        return self._maximaleTroskracht.get_waarde()

    @maximaleTroskracht.setter
    def maximaleTroskracht(self, value):
        self._maximaleTroskracht.set_waarde(value, owner=self)

    @property
    def typeBevestiging(self) -> str:
        """De verschillende bevestigingsmiddellen van een bolder."""
        return self._typeBevestiging.get_waarde()

    @typeBevestiging.setter
    def typeBevestiging(self, value):
        self._typeBevestiging.set_waarde(value, owner=self)

    @property
    def typeBolder(self) -> str:
        """De verschillende types bolder."""
        return self._typeBolder.get_waarde()

    @typeBolder.setter
    def typeBolder(self, value):
        self._typeBolder.set_waarde(value, owner=self)
