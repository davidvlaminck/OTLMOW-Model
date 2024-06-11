# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMIVComkaartType import KlMIVComkaartType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVCommunicatiekaart(AIMNaamObject, PuntGeometrie):
    """Meten in Vlaanderen : interface tussen LVE en het telematica netwerk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie', deprecated='2.9.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie', deprecated='2.9.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart')

        self._type = OTLAttribuut(field=KlMIVComkaartType,
                                  naam='type',
                                  label='type MIV communicatiekaart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart.type',
                                  definition='Geeft het type interface aan tussen LVE en het telematica netwerk.',
                                  owner=self)

    @property
    def type(self) -> str:
        """Geeft het type interface aan tussen LVE en het telematica netwerk."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
