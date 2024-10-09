# coding=utf-8
from ...Classes.Abstracten.Brandvoorziening import Brandvoorziening


# Generated with OTLClassCreator. To modify: extend, do not edit
class OntluchterBrandleiding(Brandvoorziening):
    """Klep in de brandleiding die toelaat de leiding te ontluchten bij een droge blusleiding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OntluchterBrandleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
