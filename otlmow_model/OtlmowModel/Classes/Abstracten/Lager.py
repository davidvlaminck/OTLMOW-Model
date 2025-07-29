# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlSmeringType import KlSmeringType
from ...Datatypes.KlTypeBeweging import KlTypeBeweging
from ...Datatypes.KwantWrdInKubiekeCentimeter import KwantWrdInKubiekeCentimeter, KwantWrdInKubiekeCentimeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lager(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Abstracte die alle relaties van lagers verzamelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aandrijfas', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AsMechanisch', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CilinderStangkop', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderbodem', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Halsbeugeloog', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabeltrommel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Keerwiel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lagerblok', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pendel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rol', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schommeljuk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatsschoen', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwiel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wormschroef', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging', direction='o')  # o = direction: outgoing

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager.breedte',
                                     definition='De breedte van het lager. Indien je de lager bekijkt als een cilinder, dan spreken we hier over de hoogte van de cilinder.',
                                     owner=self)

        self._hoeveelheidVetPerSmeerronde = OTLAttribuut(field=KwantWrdInKubiekeCentimeter,
                                                         naam='hoeveelheidVetPerSmeerronde',
                                                         label='hoeveelheid vet per smeerronde',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager.hoeveelheidVetPerSmeerronde',
                                                         definition='Geeft aan hoeveel vet er per smeerronde moet worden gebruikt om het lager goed te smeren.',
                                                         owner=self)

        self._inwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='inwendigeDiameter',
                                               label='inwendige diameter',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager.inwendigeDiameter',
                                               definition='De inwendige diameter van het lager bepaalt hoe groot de as die in het lager beweegt kan zijn.',
                                               owner=self)

        self._typeBeweging = OTLAttribuut(field=KlTypeBeweging,
                                          naam='typeBeweging',
                                          label='type beweging',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager.typeBeweging',
                                          definition='Geeft aan welke vorm van beweging het lager toelaat.',
                                          owner=self)

        self._typeSmering = OTLAttribuut(field=KlSmeringType,
                                         naam='typeSmering',
                                         label='type smering',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager.typeSmering',
                                         definition='Geeft aan op welke wijze het lager gesmeerd wordt.',
                                         owner=self)

        self._uitwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='uitwendigeDiameter',
                                                label='uitwendige diameter',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager.uitwendigeDiameter',
                                                definition='De uitwendige diameter van het lager.',
                                                owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van het lager. Indien je de lager bekijkt als een cilinder, dan spreken we hier over de hoogte van de cilinder."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def hoeveelheidVetPerSmeerronde(self) -> KwantWrdInKubiekeCentimeterWaarden:
        """Geeft aan hoeveel vet er per smeerronde moet worden gebruikt om het lager goed te smeren."""
        return self._hoeveelheidVetPerSmeerronde.get_waarde()

    @hoeveelheidVetPerSmeerronde.setter
    def hoeveelheidVetPerSmeerronde(self, value):
        self._hoeveelheidVetPerSmeerronde.set_waarde(value, owner=self)

    @property
    def inwendigeDiameter(self) -> KwantWrdInMillimeterWaarden:
        """De inwendige diameter van het lager bepaalt hoe groot de as die in het lager beweegt kan zijn."""
        return self._inwendigeDiameter.get_waarde()

    @inwendigeDiameter.setter
    def inwendigeDiameter(self, value):
        self._inwendigeDiameter.set_waarde(value, owner=self)

    @property
    def typeBeweging(self) -> str:
        """Geeft aan welke vorm van beweging het lager toelaat."""
        return self._typeBeweging.get_waarde()

    @typeBeweging.setter
    def typeBeweging(self, value):
        self._typeBeweging.set_waarde(value, owner=self)

    @property
    def typeSmering(self) -> str:
        """Geeft aan op welke wijze het lager gesmeerd wordt."""
        return self._typeSmering.get_waarde()

    @typeSmering.setter
    def typeSmering(self, value):
        self._typeSmering.set_waarde(value, owner=self)

    @property
    def uitwendigeDiameter(self) -> KwantWrdInMillimeterWaarden:
        """De uitwendige diameter van het lager."""
        return self._uitwendigeDiameter.get_waarde()

    @uitwendigeDiameter.setter
    def uitwendigeDiameter(self, value):
        self._uitwendigeDiameter.set_waarde(value, owner=self)
