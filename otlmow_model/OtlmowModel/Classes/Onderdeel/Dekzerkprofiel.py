# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcVerankeringDekzerkprofiel import DtcVerankeringDekzerkprofiel, DtcVerankeringDekzerkprofielWaarden
from ...Datatypes.KlConstructiestaalsoort import KlConstructiestaalsoort
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dekzerkprofiel(AIMNaamObject, PuntGeometrie, LijnGeometrie):
    """Dit zijn stalen voorzieningen bedoeld om hoekige kanten van het verticale vlak met het horizontale vlak van betonconstructies tegen schade te beschermen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dekzerkprofiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional

        self._detailplanDekzerkprofiel = OTLAttribuut(field=DtcDocument,
                                                      naam='detailplanDekzerkprofiel',
                                                      label='detailplan',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dekzerkprofiel.detailplanDekzerkprofiel',
                                                      definition='Het plan van de geometrie van het dekzerkprofiel dat informatie bevat over de ontluchtingsgaten, materiaalkwaliteit, conserveringssysteem en verankeringssysteem.',
                                                      owner=self)

        self._materiaal = OTLAttribuut(field=KlConstructiestaalsoort,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dekzerkprofiel.materiaal',
                                       definition='De verschillende opties van materiaal voor dekzerkprofielen.',
                                       owner=self)

        self._verankering = OTLAttribuut(field=DtcVerankeringDekzerkprofiel,
                                         naam='verankering',
                                         label='verankering',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dekzerkprofiel.verankering',
                                         definition='Bevat informatie m.b.t. het materiaal en type van verankering.',
                                         owner=self)

    @property
    def detailplanDekzerkprofiel(self) -> DtcDocumentWaarden:
        """Het plan van de geometrie van het dekzerkprofiel dat informatie bevat over de ontluchtingsgaten, materiaalkwaliteit, conserveringssysteem en verankeringssysteem."""
        return self._detailplanDekzerkprofiel.get_waarde()

    @detailplanDekzerkprofiel.setter
    def detailplanDekzerkprofiel(self, value):
        self._detailplanDekzerkprofiel.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """De verschillende opties van materiaal voor dekzerkprofielen."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def verankering(self) -> DtcVerankeringDekzerkprofielWaarden:
        """Bevat informatie m.b.t. het materiaal en type van verankering."""
        return self._verankering.get_waarde()

    @verankering.setter
    def verankering(self, value):
        self._verankering.set_waarde(value, owner=self)
