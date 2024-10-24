# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlMateriaalVentilatiekanaal import KlMateriaalVentilatiekanaal
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilatiekanaal(AIMObject, LijnGeometrie):
    """Een buis die paarsgewijs zorgt voor passieve verluchting van een afgesloten ruimte door langs de ene buis lucht naar binnen en door de andere naar buiten te laten stromen op basis van de hoogte ten opzichte van elkaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ventilatiekanaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verluchtingskap', direction='u')  # u = unidirectional

        self._materiaal = OTLAttribuut(field=KlMateriaalVentilatiekanaal,
                                       naam='materiaal',
                                       label='materiaal ventilatiekanaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ventilatiekanaal.materiaal',
                                       definition='Het materiaal van een ventilatiekanaal verwijst naar de substantie waaruit het kanaal is vervaardigd.',
                                       owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte ventilatiekanaal',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ventilatiekanaal.oppervlakte',
                                         definition='De oppervlakte van het ventilatiekanaal is de totale doorsnede van het kanaal en vertegenwoordigt het gebied dat beschikbaar is voor de luchtstroom binnenin.',
                                         owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal van een ventilatiekanaal verwijst naar de substantie waaruit het kanaal is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van het ventilatiekanaal is de totale doorsnede van het kanaal en vertegenwoordigt het gebied dat beschikbaar is voor de luchtstroom binnenin."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
