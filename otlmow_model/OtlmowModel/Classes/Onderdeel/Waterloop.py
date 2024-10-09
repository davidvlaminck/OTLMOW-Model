# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.WaterloopRelatie import WaterloopRelatie
from ...Datatypes.KlWaterloopCategorie import KlWaterloopCategorie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Waterloop(WaterloopRelatie):
    """Oorspronkelijk natuurlijke watergeul in het landschap waarin water stroomt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waterloop'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._categorie = OTLAttribuut(field=KlWaterloopCategorie,
                                       naam='categorie',
                                       label='categorie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waterloop.categorie',
                                       definition='De categorie betreft een subindeling op basis van het juridisch statuut van de waterloop.',
                                       owner=self)

    @property
    def categorie(self) -> str:
        """De categorie betreft een subindeling op basis van het juridisch statuut van de waterloop."""
        return self._categorie.get_waarde()

    @categorie.setter
    def categorie(self, value):
        self._categorie.set_waarde(value, owner=self)
