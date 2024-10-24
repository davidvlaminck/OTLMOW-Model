# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Detectie import Detectie
from ...Classes.Abstracten.FirmwareObject import FirmwareObject
from ...Datatypes.KlWeggebondendetectorDetectieprincipe import KlWeggebondendetectorDetectieprincipe
from ...Datatypes.KlWeggebondendetectorMerk import KlWeggebondendetectorMerk
from ...Datatypes.KlWeggebondendetectorModelnaam import KlWeggebondendetectorModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WeggebondenDetector(Detectie, FirmwareObject, PuntGeometrie):
    """Weggebonden detectoren zijn draadloze in het wegdek geïntegreerde radars of magnetische inductiesensoren. Ze zitten ingebed in een cilinder, die geplaatst wordt in het wegdek en die draadloos communiceert met een access point die met de verkeersregelaar verbonden is"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij', direction='i')  # i = direction: incoming

        self._detectieprincipe = OTLAttribuut(field=KlWeggebondendetectorDetectieprincipe,
                                              naam='detectieprincipe',
                                              label='detectieprincipe',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.detectieprincipe',
                                              definition='Het detectieprincipe geeft aan hoe de weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler.',
                                              owner=self)

        self._merk = OTLAttribuut(field=KlWeggebondendetectorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.merk',
                                  definition='Merknaam van een weggebonden detector.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWeggebondendetectorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.modelnaam',
                                       definition='De modelnaam van een weggebonden detector.',
                                       owner=self)

    @property
    def detectieprincipe(self) -> str:
        """Het detectieprincipe geeft aan hoe de weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler."""
        return self._detectieprincipe.get_waarde()

    @detectieprincipe.setter
    def detectieprincipe(self, value):
        self._detectieprincipe.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van een weggebonden detector."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van een weggebonden detector."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
