# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Voedingspunt import Voedingspunt
from ...Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm, DtcAfmetingBxlxhInMmWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dieselgenerator(Voedingspunt, PuntGeometrie, VlakGeometrie):
    """Dieselmotor die een generator (machine die mechanische energie omzet in elektrische energie) aandrijft,typisch gebruikt als noodstroom aggregaat bij het wegvallen van de normale netvoeding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieselgenerator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='o')  # o = direction: outgoing

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieselgenerator.afmetingen',
                                        definition='De afmetingen van de dieselgenerator.',
                                        owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlxhInMmWaarden:
        """De afmetingen van de dieselgenerator."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)
