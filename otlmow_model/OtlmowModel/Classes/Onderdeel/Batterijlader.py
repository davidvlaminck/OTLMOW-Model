# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlBatterijladerMerk import KlBatterijladerMerk
from ...Datatypes.KlBatterijladerModelnaam import KlBatterijladerModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Batterijlader(SerienummerObject, AIMObject, PuntGeometrie):
    """Een aparte permanente lader die een batterij oplaadt. Deze wordt ook wel een druppelaar of druppellader genoemd. Doorgaans wordt de batterij opgeladen door gebruik te maken van de netvoeding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterijlader'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij', direction='o')  # o = direction: outgoing

        self._merk = OTLAttribuut(field=KlBatterijladerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterijlader.merk',
                                  definition='Het merk van de batterijlader.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBatterijladerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterijlader.modelnaam',
                                       definition='De modelnaam van de batterijlader.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de batterijlader."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de batterijlader."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
