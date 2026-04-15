# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlConserveringssysteem import KlConserveringssysteem
from ...Datatypes.KlCorrosieCategorie import KlCorrosieCategorie
from ...Datatypes.KlOppervlaktevoorbereiding import KlOppervlaktevoorbereiding
from ...Datatypes.KlReinheidsgraad import KlReinheidsgraad
from ...GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ConserveringStaal(AIMObject, GeenGeometrie):
    """Geheel van beschermingsmaatregelen, inclusief conserveringssysteem en oppervlaktevoorbereiding, dat de corrosiebescherming van een stalen object specificeert."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConserveringStaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement', direction='u')  # u = unidirectional

        self._conserveringssysteem = OTLAttribuut(field=KlConserveringssysteem,
                                                  naam='conserveringssysteem',
                                                  label='conserveringssysteem',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConserveringStaal.conserveringssysteem',
                                                  definition='Samenstel van beschermingslagen of -technieken dat wordt toegepast op een stalen oppervlak om corrosie te beheersen.',
                                                  owner=self)

        self._corrosiecategorie = OTLAttribuut(field=KlCorrosieCategorie,
                                               naam='corrosiecategorie',
                                               label='corrosiecategorie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConserveringStaal.corrosiecategorie',
                                               definition='Indeling van de omgevingsgebonden corrosiebelasting waaraan het stalen object wordt blootgesteld.',
                                               owner=self)

        self._oppervlaktevoorbereiding = OTLAttribuut(field=KlOppervlaktevoorbereiding,
                                                      naam='oppervlaktevoorbereiding',
                                                      label='oppervlaktevoorbereiding',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConserveringStaal.oppervlaktevoorbereiding',
                                                      definition='Methode waarmee het stalen oppervlak wordt behandeld voorafgaand aan het aanbrengen van het conserveringssysteem.',
                                                      owner=self)

        self._reinheidsgraad = OTLAttribuut(field=KlReinheidsgraad,
                                            naam='reinheidsgraad',
                                            label='reinheidsgraad',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConserveringStaal.reinheidsgraad',
                                            definition='Niveau van zuiverheid van het staaloppervlak na oppervlaktevoorbereiding.',
                                            owner=self)

    @property
    def conserveringssysteem(self) -> str:
        """Samenstel van beschermingslagen of -technieken dat wordt toegepast op een stalen oppervlak om corrosie te beheersen."""
        return self._conserveringssysteem.get_waarde()

    @conserveringssysteem.setter
    def conserveringssysteem(self, value):
        self._conserveringssysteem.set_waarde(value, owner=self)

    @property
    def corrosiecategorie(self) -> str:
        """Indeling van de omgevingsgebonden corrosiebelasting waaraan het stalen object wordt blootgesteld."""
        return self._corrosiecategorie.get_waarde()

    @corrosiecategorie.setter
    def corrosiecategorie(self, value):
        self._corrosiecategorie.set_waarde(value, owner=self)

    @property
    def oppervlaktevoorbereiding(self) -> str:
        """Methode waarmee het stalen oppervlak wordt behandeld voorafgaand aan het aanbrengen van het conserveringssysteem."""
        return self._oppervlaktevoorbereiding.get_waarde()

    @oppervlaktevoorbereiding.setter
    def oppervlaktevoorbereiding(self, value):
        self._oppervlaktevoorbereiding.set_waarde(value, owner=self)

    @property
    def reinheidsgraad(self) -> str:
        """Niveau van zuiverheid van het staaloppervlak na oppervlaktevoorbereiding."""
        return self._reinheidsgraad.get_waarde()

    @reinheidsgraad.setter
    def reinheidsgraad(self, value):
        self._reinheidsgraad.set_waarde(value, owner=self)
