# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GroepDwarseMarkeringEnFiguratie(AIMObject, PuntGeometrie):
    """Groepering van de dwarse- en figuratiemarkering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering')

        self._totaleOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                               naam='totaleOppervlakte',
                                               label='totale oppervlakte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie.totaleOppervlakte',
                                               definition='De oppervlakte van de groep dwarse en/of figuratie markering.',
                                               owner=self)

        self._tussenruimte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='tussenruimte',
                                          label='tussenruimte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie.tussenruimte',
                                          definition='De lengte van de tussenruimte in meter tussen de dwarse en/of figuratie markering.',
                                          owner=self)

    @property
    def totaleOppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de groep dwarse en/of figuratie markering."""
        return self._totaleOppervlakte.get_waarde()

    @totaleOppervlakte.setter
    def totaleOppervlakte(self, value):
        self._totaleOppervlakte.set_waarde(value, owner=self)

    @property
    def tussenruimte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de tussenruimte in meter tussen de dwarse en/of figuratie markering."""
        return self._tussenruimte.get_waarde()

    @tussenruimte.setter
    def tussenruimte(self, value):
        self._tussenruimte.set_waarde(value, owner=self)
