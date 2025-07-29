# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMantelHydraulischeCilinderophanging import KlMantelHydraulischeCilinderophanging
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cilindermantel(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Het onderdeel van de cilinder waarin de cilinderstang heen en weer beweegt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderbodem', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderkop', direction='u')  # u = unidirectional

        self._binnendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='binnendiameter',
                                            label='binnendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel.binnendiameter',
                                            definition='De binnendiameter van de mantel, uitgedrukt in millimeter.',
                                            owner=self)

        self._buitendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel.buitendiameter',
                                            definition='De buitendiameter van de mantel, uitgedrukt in millimeter.',
                                            owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel.lengte',
                                    definition='De lengte van de buitenkant van de mantel, uitgedrukt in millimeter. Gezien het om een cilinder gaat, zou men dit ook de hoogte van de cilinder kunnen noemen.',
                                    owner=self)

        self._ophanging = OTLAttribuut(field=KlMantelHydraulischeCilinderophanging,
                                       naam='ophanging',
                                       label='ophanging',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel.ophanging',
                                       definition='Geeft aan hoe de mantel aan het kunstwerk is opgehangen.',
                                       owner=self)

    @property
    def binnendiameter(self) -> KwantWrdInMillimeterWaarden:
        """De binnendiameter van de mantel, uitgedrukt in millimeter."""
        return self._binnendiameter.get_waarde()

    @binnendiameter.setter
    def binnendiameter(self, value):
        self._binnendiameter.set_waarde(value, owner=self)

    @property
    def buitendiameter(self) -> KwantWrdInMillimeterWaarden:
        """De buitendiameter van de mantel, uitgedrukt in millimeter."""
        return self._buitendiameter.get_waarde()

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de buitenkant van de mantel, uitgedrukt in millimeter. Gezien het om een cilinder gaat, zou men dit ook de hoogte van de cilinder kunnen noemen."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def ophanging(self) -> str:
        """Geeft aan hoe de mantel aan het kunstwerk is opgehangen."""
        return self._ophanging.get_waarde()

    @ophanging.setter
    def ophanging(self, value):
        self._ophanging.set_waarde(value, owner=self)
