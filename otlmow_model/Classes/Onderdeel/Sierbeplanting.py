# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.BegroeidVoorkomen import BegroeidVoorkomen
from otlmow_model.Datatypes.DtcSierbeplAanleg import DtcSierbeplAanleg, DtcSierbeplAanlegWaarden
from otlmow_model.Datatypes.KlSierbeplantingType import KlSierbeplantingType
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sierbeplanting(BegroeidVoorkomen, VlakGeometrie):
    """Planten die geen blijvende houtige stengel vormen. Eenjarige,tweejarige of vaste planten,die in de winter tot de grond toe afsterven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerSierbeplanting')

        self._aanleg = OTLAttribuut(field=DtcSierbeplAanleg,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting.aanleg',
                                    definition='De manier van aanplanten van de sierbeplanting.',
                                    owner=self)

        self._type = OTLAttribuut(field=KlSierbeplantingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting.type',
                                  kardinaliteit_max='*',
                                  definition='Type van sierbeplanting.',
                                  owner=self)

    @property
    def aanleg(self) -> DtcSierbeplAanlegWaarden:
        """De manier van aanplanten van de sierbeplanting."""
        return self._aanleg.get_waarde()

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def type(self) -> List[str]:
        """Type van sierbeplanting."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
