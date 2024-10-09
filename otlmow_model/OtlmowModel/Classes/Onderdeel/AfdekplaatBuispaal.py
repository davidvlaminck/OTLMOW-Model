# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StalenConstructieElement import StalenConstructieElement
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KwantWrdInProcent import KwantWrdInProcent, KwantWrdInProcentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfdekplaatBuispaal(StalenConstructieElement, AIMObject, PuntGeometrie):
    """Stalen plaat bevestigd op/in de buispaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AfdekplaatBuispaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal', direction='u')  # u = unidirectional

        self._afschot = OTLAttribuut(field=KwantWrdInProcent,
                                     naam='afschot',
                                     label='afschot',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AfdekplaatBuispaal.afschot',
                                     definition='Helling van de afdekplaat in procenten om stagenerend water tegen te gaan.',
                                     owner=self)

    @property
    def afschot(self) -> KwantWrdInProcentWaarden:
        """Helling van de afdekplaat in procenten om stagenerend water tegen te gaan."""
        return self._afschot.get_waarde()

    @afschot.setter
    def afschot(self, value):
        self._afschot.set_waarde(value, owner=self)
