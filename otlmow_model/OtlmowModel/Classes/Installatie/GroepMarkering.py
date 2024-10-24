# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GroepMarkering(AIMObject, PuntGeometrie):
    """Groepering om alle soorten markeringen te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DwarseMarkeringToegang', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FiguratieMarkeringToegang', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering', direction='i')  # i = direction: incoming

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
