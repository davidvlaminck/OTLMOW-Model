# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlKabelFabrikant import KlKabelFabrikant
from ...Datatypes.KlKabelLeidingBescherming import KlKabelLeidingBescherming
from ...Datatypes.KlKabelmantelKleur import KlKabelmantelKleur
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabel(AIMNaamObject, LijnGeometrie):
    """Abstracte voor attributen en relaties van allerlei types kabels."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorverbinddoos', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', direction='i')  # i = direction: incoming

        self._buitenmantelDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                  naam='buitenmantelDiameter',
                                                  label='buitenmantel diameter',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.buitenmantelDiameter',
                                                  definition='De buitenste afmeting van de kabel in millimeter.',
                                                  owner=self)

        self._buitenmantelKleur = OTLAttribuut(field=KlKabelmantelKleur,
                                               naam='buitenmantelKleur',
                                               label='buitenmantel kleur',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.buitenmantelKleur',
                                               definition='De hoofdkleur(en) die voor een waarnemer onmiddellijk zichtbaar is (zijn) zonder de kabel te ontmantelen, de kleur van de markeringen op die buitenste mantel buiten beschouwing gelaten.',
                                               owner=self)

        self._fabrikant = OTLAttribuut(field=KlKabelFabrikant,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.fabrikant',
                                       definition='De naam van de producent van de kabel.',
                                       owner=self)

        self._typeBescherming = OTLAttribuut(field=KlKabelLeidingBescherming,
                                             naam='typeBescherming',
                                             label='type bescherming',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.typeBescherming',
                                             definition='Geeft aan of en hoe de leiding bijkomend mechanisch beschermd nadat ze in de sleuf gelegd is.',
                                             owner=self)

    @property
    def buitenmantelDiameter(self) -> KwantWrdInMillimeterWaarden:
        """De buitenste afmeting van de kabel in millimeter."""
        return self._buitenmantelDiameter.get_waarde()

    @buitenmantelDiameter.setter
    def buitenmantelDiameter(self, value):
        self._buitenmantelDiameter.set_waarde(value, owner=self)

    @property
    def buitenmantelKleur(self) -> str:
        """De hoofdkleur(en) die voor een waarnemer onmiddellijk zichtbaar is (zijn) zonder de kabel te ontmantelen, de kleur van de markeringen op die buitenste mantel buiten beschouwing gelaten."""
        return self._buitenmantelKleur.get_waarde()

    @buitenmantelKleur.setter
    def buitenmantelKleur(self, value):
        self._buitenmantelKleur.set_waarde(value, owner=self)

    @property
    def fabrikant(self) -> str:
        """De naam van de producent van de kabel."""
        return self._fabrikant.get_waarde()

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def typeBescherming(self) -> str:
        """Geeft aan of en hoe de leiding bijkomend mechanisch beschermd nadat ze in de sleuf gelegd is."""
        return self._typeBescherming.get_waarde()

    @typeBescherming.setter
    def typeBescherming(self, value):
        self._typeBescherming.set_waarde(value, owner=self)
