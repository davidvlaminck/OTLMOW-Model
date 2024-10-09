# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.NietWeggebondenDetectie import NietWeggebondenDetectie
from ...Classes.Abstracten.TypeWeggebruiker import TypeWeggebruiker
from ...Datatypes.KlDetectiecameraDetectieprincipe import KlDetectiecameraDetectieprincipe
from ...Datatypes.KlDetectiecameraMerk import KlDetectiecameraMerk
from ...Datatypes.KlDetectiecameraModelnaam import KlDetectiecameraModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DetectieCamera(NietWeggebondenDetectie, TypeWeggebruiker):
    """Deze camera's worden onder andere opgesteld op kruispunten om de aanwezigheid van voertuigen te detecteren. De detectie kan optisch en/of thermografisch gebeuren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone', direction='u')  # u = unidirectional

        self._detectieprincipe = OTLAttribuut(field=KlDetectiecameraDetectieprincipe,
                                              naam='detectieprincipe',
                                              label='detectieprincipe',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.detectieprincipe',
                                              kardinaliteit_max='*',
                                              definition='Geeft aan of de camera optisch en/of thermografisch werkt.',
                                              owner=self)

        self._merk = OTLAttribuut(field=KlDetectiecameraMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.merk',
                                  definition='Merknaam van de detectiecamera.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDetectiecameraModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.modelnaam',
                                       definition='De modelnaam van de detectiecamera.',
                                       owner=self)

    @property
    def detectieprincipe(self) -> List[str]:
        """Geeft aan of de camera optisch en/of thermografisch werkt."""
        return self._detectieprincipe.get_waarde()

    @detectieprincipe.setter
    def detectieprincipe(self, value):
        self._detectieprincipe.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de detectiecamera."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de detectiecamera."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
