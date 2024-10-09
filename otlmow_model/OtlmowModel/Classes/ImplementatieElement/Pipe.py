# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Leiding import Leiding
from ...Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from ...Datatypes.KlBeschermbuisKleur import KlBeschermbuisKleur
from ...Datatypes.KlNetwerkType import KlNetwerkType
from ...Datatypes.KlPipeContainerType import KlPipeContainerType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pipe(Leiding, OmhullendeInrichting):
    """Een buis die dienst kan doen als object voor het omhullen van meerdere kabels of andere (kleinere) leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', direction='i')  # i = direction: incoming

        self._containerType = OTLAttribuut(field=KlPipeContainerType,
                                           naam='containerType',
                                           label='containertype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe.containerType',
                                           definition='Attribuut dat het soort van kabel- en leidingcontainer aangeeft.',
                                           owner=self)

        self._kleur = OTLAttribuut(field=KlBeschermbuisKleur,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe.kleur',
                                   definition='Kleur van buitenmantel volgens een vaste lijst.',
                                   owner=self)

        self._netwerkType = OTLAttribuut(field=KlNetwerkType,
                                         naam='netwerkType',
                                         label='netwerktype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe.netwerkType',
                                         definition='Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire.',
                                         owner=self)

    @property
    def containerType(self) -> str:
        """Attribuut dat het soort van kabel- en leidingcontainer aangeeft."""
        return self._containerType.get_waarde()

    @containerType.setter
    def containerType(self, value):
        self._containerType.set_waarde(value, owner=self)

    @property
    def kleur(self) -> str:
        """Kleur van buitenmantel volgens een vaste lijst."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def netwerkType(self) -> str:
        """Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire."""
        return self._netwerkType.get_waarde()

    @netwerkType.setter
    def netwerkType(self, value):
        self._netwerkType.set_waarde(value, owner=self)
