# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlAutoOmschakelaarWerking import KlAutoOmschakelaarWerking
from ...Datatypes.KlSTSMerk import KlSTSMerk
from ...Datatypes.KlSTSModelnaam import KlSTSModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AutomatischeOmschakelaar(SerienummerObject, AIMObject, PuntGeometrie):
    """Automatische omschakelmodule voor voeding, ook gekend als Static Transfer Switch of STS."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AutomatischeOmschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlSTSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AutomatischeOmschakelaar.merk',
                                  definition='Het merk van de automatische omschakelaar.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSTSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AutomatischeOmschakelaar.modelnaam',
                                       definition='De modelnaam van de automatische omschakelaar.',
                                       owner=self)

        self._werkingsprincipe = OTLAttribuut(field=KlAutoOmschakelaarWerking,
                                              naam='werkingsprincipe',
                                              label='werkingsprincipe',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AutomatischeOmschakelaar.werkingsprincipe',
                                              definition='Geeft het werkingsprincipe aan volgens hetwelk kan gewisseld worden tussen twee bronnen zonder of met minmaal verlies in de werking van een gekoppelde techniek, bv. bij gebruik van een UPS voor de geleverde spanning voor een toestel.',
                                              owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de automatische omschakelaar."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de automatische omschakelaar."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def werkingsprincipe(self) -> str:
        """Geeft het werkingsprincipe aan volgens hetwelk kan gewisseld worden tussen twee bronnen zonder of met minmaal verlies in de werking van een gekoppelde techniek, bv. bij gebruik van een UPS voor de geleverde spanning voor een toestel."""
        return self._werkingsprincipe.get_waarde()

    @werkingsprincipe.setter
    def werkingsprincipe(self, value):
        self._werkingsprincipe.set_waarde(value, owner=self)
