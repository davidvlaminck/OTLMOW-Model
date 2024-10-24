# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlLEACUitzettingswaardeDilatatie import KlLEACUitzettingswaardeDilatatie
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dilatatie(AIMObject, PuntGeometrie):
    """Dilataties zijn bedoeld om ervoor te zorgen dat bouwconstructies vrij kunnen krimpen en uitzetten bij onder andere temperatuurwisselingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', direction='i')  # i = direction: incoming

        self._uitzettingswaarde = OTLAttribuut(field=KlLEACUitzettingswaardeDilatatie,
                                               naam='uitzettingswaarde',
                                               label='uitzettingswaarde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie.uitzettingswaarde',
                                               definition='De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing.',
                                               owner=self)

    @property
    def uitzettingswaarde(self) -> str:
        """De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing."""
        return self._uitzettingswaarde.get_waarde()

    @uitzettingswaarde.setter
    def uitzettingswaarde(self, value):
        self._uitzettingswaarde.set_waarde(value, owner=self)
