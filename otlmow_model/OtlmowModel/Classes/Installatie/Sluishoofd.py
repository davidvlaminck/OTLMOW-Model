# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Constructiehoofd import Constructiehoofd
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlHoofdtype import KlHoofdtype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sluishoofd(Constructiehoofd, AIMNaamObject):
    """Constructiehoofd van een sluis waarin één of meerdere sluisdeuren zitten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Deurloop', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Drempel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vloernis', direction='i')  # i = direction: incoming

        self._typeHoofd = OTLAttribuut(field=KlHoofdtype,
                                       naam='typeHoofd',
                                       label='type Hoofd',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd.typeHoofd',
                                       definition='Geeft het type hoofd aan van het constructiehoofd.',
                                       owner=self)

    @property
    def typeHoofd(self) -> str:
        """Geeft het type hoofd aan van het constructiehoofd."""
        return self._typeHoofd.get_waarde()

    @typeHoofd.setter
    def typeHoofd(self, value):
        self._typeHoofd.set_waarde(value, owner=self)
