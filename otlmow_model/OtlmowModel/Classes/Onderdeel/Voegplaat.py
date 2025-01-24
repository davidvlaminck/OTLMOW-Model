# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalVoegplaat import KlMateriaalVoegplaat
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voegplaat(AIMNaamObject, PuntGeometrie):
    """Een plaatvormig element dat in voegen van betonconstructies wordt aangebracht. Wordt veelal voorzien t.p.v. (gronddichte) uitzettingsvoegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur', direction='u')  # u = unidirectional

        self._materiaalVoegplaat = OTLAttribuut(field=KlMateriaalVoegplaat,
                                                naam='materiaalVoegplaat',
                                                label='materiaal voegplaat',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegplaat.materiaalVoegplaat',
                                                definition='De verschillende opties van materiaal voor voegplaten.',
                                                owner=self)

    @property
    def materiaalVoegplaat(self) -> str:
        """De verschillende opties van materiaal voor voegplaten."""
        return self._materiaalVoegplaat.get_waarde()

    @materiaalVoegplaat.setter
    def materiaalVoegplaat(self, value):
        self._materiaalVoegplaat.set_waarde(value, owner=self)
