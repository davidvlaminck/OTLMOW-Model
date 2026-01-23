# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcBeschermendeLaag import DtcBeschermendeLaag, DtcBeschermendeLaagWaarden
from ...Datatypes.DteKleurRAL import DteKleurRAL, DteKleurRALWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVConsole(NaampadObject, PuntGeometrie):
    """Een draagconstructie voor het ophangen van openbare wegverlichting op plaatsen waar er geen ruimte is voor verlichtingsmasten in de grond. Typisch wordt in dergelijke gevallen de draagconstructie met het verlichtingstoestel op hoogte bevestigd aan een gebouw of een andere constructie naast de weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVConsole'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WegverlichtingGroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming

        self._beschermendeLaag = OTLAttribuut(field=DtcBeschermendeLaag,
                                              naam='beschermendeLaag',
                                              label='beschermende laag',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVConsole.beschermendeLaag',
                                              definition='Het type van bescherming van de constructie of steun met de corresponderende corrosieklasse.',
                                              owner=self)

        self._kleur = OTLAttribuut(field=DteKleurRAL,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVConsole.kleur',
                                   definition='RAL kleur van de WVConsole.',
                                   owner=self)

    @property
    def beschermendeLaag(self) -> DtcBeschermendeLaagWaarden:
        """Het type van bescherming van de constructie of steun met de corresponderende corrosieklasse."""
        return self._beschermendeLaag.get_waarde()

    @beschermendeLaag.setter
    def beschermendeLaag(self, value):
        self._beschermendeLaag.set_waarde(value, owner=self)

    @property
    def kleur(self) -> DteKleurRALWaarden:
        """RAL kleur van de WVConsole."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)
