# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GroepMarkering(AIMObject, PuntGeometrie):
    """Groepering om alle soorten markeringen te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering')

        self._totaleGroepOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                                    naam='totaleGroepOppervlakte',
                                                    label='totale oppervlakte groepering',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering.totaleGroepOppervlakte',
                                                    definition='De totale oppervlakte van de totale markering groepering.',
                                                    owner=self)

    @property
    def totaleGroepOppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De totale oppervlakte van de totale markering groepering."""
        return self._totaleGroepOppervlakte.get_waarde()

    @totaleGroepOppervlakte.setter
    def totaleGroepOppervlakte(self, value):
        self._totaleGroepOppervlakte.set_waarde(value, owner=self)
