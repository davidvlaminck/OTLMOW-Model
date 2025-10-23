# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.KlLEACVoertuigOverhelling import KlLEACVoertuigOverhelling
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVoertuigOverhelling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om de overhelling over de bebakening van het voertuig te bepalen bij impact."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVoertuigOverhelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', direction='o', deprecated='2.0.0')  # o = direction: outgoing

        self._voertuigOverhelling = OTLAttribuut(field=KlLEACVoertuigOverhelling,
                                                 naam='voertuigOverhelling',
                                                 label='voertuig overhelling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVoertuigOverhelling.voertuigOverhelling',
                                                 usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                 deprecated_version='2.0.0',
                                                 definition="Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald.",
                                                 owner=self)

    @property
    def voertuigOverhelling(self) -> str:
        """Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald."""
        return self._voertuigOverhelling.get_waarde()

    @voertuigOverhelling.setter
    def voertuigOverhelling(self, value):
        self._voertuigOverhelling.set_waarde(value, owner=self)
