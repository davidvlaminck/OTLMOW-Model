# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlDetectieVeCommunicatiewijze import KlDetectieVeCommunicatiewijze
from ...Datatypes.KlDetectieVeMerk import KlDetectieVeMerk
from ...Datatypes.KlDetectieVeModelnaam import KlDetectieVeModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Detectieverwerkingseenheid(AIMNaamObject, PuntGeometrie):
    """Een interface die rauwe detectiedata omzet naar input die gebruikt kan worden door een verkeersregelaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Detectieverwerkingseenheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', direction='u')  # u = unidirectional

        self._communicatiewijze = OTLAttribuut(field=KlDetectieVeCommunicatiewijze,
                                               naam='communicatiewijze',
                                               label='communicatiewijze',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Detectieverwerkingseenheid.communicatiewijze',
                                               definition='De communicatiewijze van de verwerkingseenheid.',
                                               owner=self)

        self._merk = OTLAttribuut(field=KlDetectieVeMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Detectieverwerkingseenheid.merk',
                                  definition='Het merk van de detectieverwerkingseenheid.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDetectieVeModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Detectieverwerkingseenheid.modelnaam',
                                       definition='De modelnaam van de detectieverwerkingseenheid.',
                                       owner=self)

    @property
    def communicatiewijze(self) -> str:
        """De communicatiewijze van de verwerkingseenheid."""
        return self._communicatiewijze.get_waarde()

    @communicatiewijze.setter
    def communicatiewijze(self, value):
        self._communicatiewijze.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de detectieverwerkingseenheid."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de detectieverwerkingseenheid."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
