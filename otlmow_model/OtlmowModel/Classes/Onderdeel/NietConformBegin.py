# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlLEACMateriaal import KlLEACMateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietConformBegin(AIMObject, LijnGeometrie):
    """Een begin aan een geleideconstructie dat niet voldoet aan de voorwaarden van een GetesteBeginconstructie of een NietGetestBeginstuk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietConformBegin'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement', direction='o')  # o = direction: outgoing

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
