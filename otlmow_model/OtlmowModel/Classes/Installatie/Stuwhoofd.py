# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Constructiehoofd import Constructiehoofd
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlProfielVastAanslag import KlProfielVastAanslag


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stuwhoofd(Constructiehoofd, AIMNaamObject):
    """Constructiehoofd van een stuw waarin één of meerdere stuwelementen zitten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuwhoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', direction='i')  # i = direction: incoming

        self._heeftAanslagprofiel = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAanslagprofiel',
                                                 label='heeft aanslagprofiel',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuwhoofd.heeftAanslagprofiel',
                                                 definition='Geeft aan of er een aanslagprofiel aanwezig is.',
                                                 owner=self)

        self._profielVastAanslag = OTLAttribuut(field=KlProfielVastAanslag,
                                                naam='profielVastAanslag',
                                                label='materiaal aanslagprofiel',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuwhoofd.profielVastAanslag',
                                                definition='Het gebruikte materiaal van het aanslagprofiel.',
                                                owner=self)

    @property
    def heeftAanslagprofiel(self) -> bool:
        """Geeft aan of er een aanslagprofiel aanwezig is."""
        return self._heeftAanslagprofiel.get_waarde()

    @heeftAanslagprofiel.setter
    def heeftAanslagprofiel(self, value):
        self._heeftAanslagprofiel.set_waarde(value, owner=self)

    @property
    def profielVastAanslag(self) -> str:
        """Het gebruikte materiaal van het aanslagprofiel."""
        return self._profielVastAanslag.get_waarde()

    @profielVastAanslag.setter
    def profielVastAanslag(self, value):
        self._profielVastAanslag.set_waarde(value, owner=self)
