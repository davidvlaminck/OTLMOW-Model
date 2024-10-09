# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.KlLEACKerendVermogen import KlLEACKerendVermogen
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefKerendVermogen(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om het vermogen van een voertuigkering te bepalen om een doorbraak bij een bepaald type crash te voorkomen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKerendVermogen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', direction='o', deprecated='2.0.0')  # o = direction: outgoing

        self._kerendVermogen = OTLAttribuut(field=KlLEACKerendVermogen,
                                            naam='kerendVermogen',
                                            label='kerend vermogen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKerendVermogen.kerendVermogen',
                                            usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                            deprecated_version='2.0.0',
                                            definition='Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen.',
                                            owner=self)

    @property
    def kerendVermogen(self) -> str:
        """Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen."""
        return self._kerendVermogen.get_waarde()

    @kerendVermogen.setter
    def kerendVermogen(self, value):
        self._kerendVermogen.set_waarde(value, owner=self)
