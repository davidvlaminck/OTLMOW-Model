# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.Abstracten.DetaiplanObject import DetaiplanObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Haalkom(AanhorigheidSluisStuw, DetaiplanObject, AIMNaamObject, PuntGeometrie):
    """Een haalkom is een voorziening in een sluis- of kademuur waaraan men een schip kan vastmaken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Haalkom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional

        self._materiaalKom = OTLAttribuut(field=StringField,
                                          naam='materiaalKom',
                                          label='materiaal kom',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Haalkom.materiaalKom',
                                          definition='Het gebruikte materiaal voor de kom (Bijv: GE300, GS24Mn6,..).',
                                          owner=self)

        self._materiaalPen = OTLAttribuut(field=StringField,
                                          naam='materiaalPen',
                                          label='materiaal pen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Haalkom.materiaalPen',
                                          definition='Het gebruikte materiaal voor de pen (Bijv: 42CrMo4,..).',
                                          owner=self)

        self._maximaleTroskracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                naam='maximaleTroskracht',
                                                label='maximale troskracht',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Haalkom.maximaleTroskracht',
                                                definition='De maximale troskracht, uitgedrukt in kN (Karakteristieke waarde).',
                                                owner=self)

    @property
    def materiaalKom(self) -> str:
        """Het gebruikte materiaal voor de kom (Bijv: GE300, GS24Mn6,..)."""
        return self._materiaalKom.get_waarde()

    @materiaalKom.setter
    def materiaalKom(self, value):
        self._materiaalKom.set_waarde(value, owner=self)

    @property
    def materiaalPen(self) -> str:
        """Het gebruikte materiaal voor de pen (Bijv: 42CrMo4,..)."""
        return self._materiaalPen.get_waarde()

    @materiaalPen.setter
    def materiaalPen(self, value):
        self._materiaalPen.set_waarde(value, owner=self)

    @property
    def maximaleTroskracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De maximale troskracht, uitgedrukt in kN (Karakteristieke waarde)."""
        return self._maximaleTroskracht.get_waarde()

    @maximaleTroskracht.setter
    def maximaleTroskracht(self, value):
        self._maximaleTroskracht.set_waarde(value, owner=self)
