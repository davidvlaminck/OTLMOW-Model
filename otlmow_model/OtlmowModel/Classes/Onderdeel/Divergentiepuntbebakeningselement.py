# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Signalisatie import Signalisatie
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlDivergentiepuntbebakeningselementType import KlDivergentiepuntbebakeningselementType
from ...Datatypes.KlFolieType import KlFolieType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Divergentiepuntbebakeningselement(Signalisatie, AIMObject, PuntGeometrie):
    """Een constructie met als doel de zichtbaarheid van het divergentiepunt te vergroten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie', direction='u')  # u = unidirectional

        self._folietype = OTLAttribuut(field=KlFolieType,
                                       naam='folietype',
                                       label='folietype',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.folietype',
                                       definition='Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlDivergentiepuntbebakeningselementType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.type',
                                  definition='De vormen van het divergentiepuntbebakeningselement.',
                                  owner=self)

    @property
    def folietype(self) -> str:
        """Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement."""
        return self._folietype.get_waarde()

    @folietype.setter
    def folietype(self, value):
        self._folietype.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De vormen van het divergentiepuntbebakeningselement."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
