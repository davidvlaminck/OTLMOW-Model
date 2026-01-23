# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.Bewegingsmechanisme import Bewegingsmechanisme
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cilindermechanisme(Bewegingsmechanisme):
    """Abstracte om relaties en attributen te bundelen voor cilindermechanismen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Grendelmechanisme', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CilinderStangkop', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderbodem', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderkop', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang', direction='i')  # i = direction: incoming

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme.gewicht',
                                     definition='Het gewicht, uitgedrukt in kilogram.',
                                     owner=self)

        self._maximaleKracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                            naam='maximaleKracht',
                                            label='maximale kracht',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme.maximaleKracht',
                                            definition='De kracht die overeenstemt met belastingsniveau 2 volgend uit de belastingscombinatie 2 van het SB270.',
                                            owner=self)

        self._slag = OTLAttribuut(field=KwantWrdInMillimeter,
                                  naam='slag',
                                  label='slag',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme.slag',
                                  definition='Afstand waarover de cilinder kan uitgeschoven worden.',
                                  owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht, uitgedrukt in kilogram."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def maximaleKracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De kracht die overeenstemt met belastingsniveau 2 volgend uit de belastingscombinatie 2 van het SB270."""
        return self._maximaleKracht.get_waarde()

    @maximaleKracht.setter
    def maximaleKracht(self, value):
        self._maximaleKracht.set_waarde(value, owner=self)

    @property
    def slag(self) -> KwantWrdInMillimeterWaarden:
        """Afstand waarover de cilinder kan uitgeschoven worden."""
        return self._slag.get_waarde()

    @slag.setter
    def slag(self, value):
        self._slag.set_waarde(value, owner=self)
