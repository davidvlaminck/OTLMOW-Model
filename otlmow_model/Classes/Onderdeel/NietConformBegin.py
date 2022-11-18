# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlLEACMateriaal import KlLEACMateriaal
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietConformBegin(AIMObject, LijnGeometrie):
    """Een begin aan een geleideconstructie dat niet voldoet aan de voorwaarden van een GetesteBeginconstructie of een NietGetestBeginstuk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietConformBegin'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement')

        self._materiaal = OTLAttribuut(field=KlLEACMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietConformBegin.materiaal',
                                       definition='Het gebruikte materiaal voor het niet conform begins.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Het gebruikte materiaal voor het niet conform begins."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
