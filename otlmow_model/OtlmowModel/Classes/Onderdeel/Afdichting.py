# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereLaag import AndereLaag
from ...Classes.Abstracten.LaagDikte import LaagDikte
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAfdichtingType import KlAfdichtingType
from ...Datatypes.KlMateriaalAfdichting import KlMateriaalAfdichting


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afdichting(AndereLaag, LaagDikte):
    """Een specifieke laag in de wegdekopbouw die voorkomt dat water tot op de constructieplaat doordringt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain', direction='i')  # i = direction: incoming

        self._materiaalAfdichting = OTLAttribuut(field=KlMateriaalAfdichting,
                                                 naam='materiaalAfdichting',
                                                 label='materiaal afdichting',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichting.materiaalAfdichting',
                                                 definition='Het materiaal van de afdichting.',
                                                 owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichting.technischeFiche',
                                             definition='De technische fiche van de afdichting.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlAfdichtingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichting.type',
                                  definition='Het type afdichting dat gebruikt wordt in de wegdekopbouw.',
                                  owner=self)

    @property
    def materiaalAfdichting(self) -> str:
        """Het materiaal van de afdichting."""
        return self._materiaalAfdichting.get_waarde()

    @materiaalAfdichting.setter
    def materiaalAfdichting(self, value):
        self._materiaalAfdichting.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de afdichting."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type afdichting dat gebruikt wordt in de wegdekopbouw."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
