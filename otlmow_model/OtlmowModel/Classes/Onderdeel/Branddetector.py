# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlBranddetectorSensortype import KlBranddetectorSensortype
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Branddetector(NaampadObject, PuntGeometrie):
    """Een toestel dat automatisch kenmerken van brand, zoals rook, warmte of vlammen, waarneemt en een alarmsignaal doorgeeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Branddetector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming

        self._meldtAutomatisch = OTLAttribuut(field=BooleanField,
                                              naam='meldtAutomatisch',
                                              label='meldt automatisch',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Branddetector.meldtAutomatisch',
                                              definition='Geeft aan of de branddetector bij het detecteren van kenmerken van brand automatisch een brandmelding of alarmsignaal doorgeeft.',
                                              owner=self)

        self._sensortype = OTLAttribuut(field=KlBranddetectorSensortype,
                                        naam='sensortype',
                                        label='sensortype',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Branddetector.sensortype',
                                        definition='Geeft aan welk kenmerk van brand de branddetector waarneemt, bv. rook, koolmonoxide (CO) of hitte.',
                                        owner=self)

    @property
    def meldtAutomatisch(self) -> bool:
        """Geeft aan of de branddetector bij het detecteren van kenmerken van brand automatisch een brandmelding of alarmsignaal doorgeeft."""
        return self._meldtAutomatisch.get_waarde()

    @meldtAutomatisch.setter
    def meldtAutomatisch(self, value):
        self._meldtAutomatisch.set_waarde(value, owner=self)

    @property
    def sensortype(self) -> str:
        """Geeft aan welk kenmerk van brand de branddetector waarneemt, bv. rook, koolmonoxide (CO) of hitte."""
        return self._sensortype.get_waarde()

    @sensortype.setter
    def sensortype(self, value):
        self._sensortype.set_waarde(value, owner=self)
