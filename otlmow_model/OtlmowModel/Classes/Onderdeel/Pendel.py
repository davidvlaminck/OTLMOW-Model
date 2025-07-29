# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pendel(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Dit is een verticaal element, dubbelzijdig scharnierend, waarmee de roldeur ophangt aan de bovenrolwagen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pendel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen', direction='o')  # o = direction: outgoing

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pendel.gewicht',
                                     definition='Het gewicht van de pendel, uitgedrukt in kilogram.',
                                     owner=self)

        self._heeftMeetcel = OTLAttribuut(field=BooleanField,
                                          naam='heeftMeetcel',
                                          label='heeft meetcel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pendel.heeftMeetcel',
                                          definition='Geeft aan of de pendel een meetcel heeft of niet.',
                                          owner=self)

        self._karakteristiekeToelaatbareKracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                              naam='karakteristiekeToelaatbareKracht',
                                                              label='karakteristieke toelaatbare kracht',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pendel.karakteristiekeToelaatbareKracht',
                                                              definition='De maximale toelaatbare kracht.',
                                                              owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht van de pendel, uitgedrukt in kilogram."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def heeftMeetcel(self) -> bool:
        """Geeft aan of de pendel een meetcel heeft of niet."""
        return self._heeftMeetcel.get_waarde()

    @heeftMeetcel.setter
    def heeftMeetcel(self, value):
        self._heeftMeetcel.set_waarde(value, owner=self)

    @property
    def karakteristiekeToelaatbareKracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De maximale toelaatbare kracht."""
        return self._karakteristiekeToelaatbareKracht.get_waarde()

    @karakteristiekeToelaatbareKracht.setter
    def karakteristiekeToelaatbareKracht(self, value):
        self._karakteristiekeToelaatbareKracht.set_waarde(value, owner=self)
