# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Detectielus import Detectielus
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlVerkeersdeelnemer import KlVerkeersdeelnemer
from ...Datatypes.KlVriLusFunctie import KlVriLusFunctie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRIVirtueleDetectiezone(Detectielus, VlakGeometrie):
    """Een virtuele detectiezone is een draadloos alternatief voor een traditionele lus. Op basis van GPS gegevens wordt een zone of traject vastgelegd waarbinnen er (al dan niet selectieve) input dient geleverd te worden aan de verkeersregelaar. De virtuele detectiezone kan ook gebruikt worden om de detectiezones van detectiecamera's en radars te inventariseren. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar', direction='u')  # u = unidirectional

        self._functie = OTLAttribuut(field=KlVriLusFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone.functie',
                                     definition='Functie van de VRI detectiezone.',
                                     owner=self)

        self._isRichtingsgevoelig = OTLAttribuut(field=BooleanField,
                                                 naam='isRichtingsgevoelig',
                                                 label='is richtingsgevoelig',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone.isRichtingsgevoelig',
                                                 definition='Geeft aan of de virtuele detectielus gevoelig is voor de richting waarin het voertuig het gevoeligheidsgebied van de lus al dan niet binnenkomt.',
                                                 owner=self)

        self._soortVerkeersdeelnemer = OTLAttribuut(field=KlVerkeersdeelnemer,
                                                    naam='soortVerkeersdeelnemer',
                                                    label='soort verkeersdeelnemer',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone.soortVerkeersdeelnemer',
                                                    kardinaliteit_max='*',
                                                    definition='Soort verkeersdeelnemer dat de detectiezone volgens zijn instellingen kan detecteren.',
                                                    owner=self)

    @property
    def functie(self) -> str:
        """Functie van de VRI detectiezone."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def isRichtingsgevoelig(self) -> bool:
        """Geeft aan of de virtuele detectielus gevoelig is voor de richting waarin het voertuig het gevoeligheidsgebied van de lus al dan niet binnenkomt."""
        return self._isRichtingsgevoelig.get_waarde()

    @isRichtingsgevoelig.setter
    def isRichtingsgevoelig(self, value):
        self._isRichtingsgevoelig.set_waarde(value, owner=self)

    @property
    def soortVerkeersdeelnemer(self) -> List[str]:
        """Soort verkeersdeelnemer dat de detectiezone volgens zijn instellingen kan detecteren."""
        return self._soortVerkeersdeelnemer.get_waarde()

    @soortVerkeersdeelnemer.setter
    def soortVerkeersdeelnemer(self, value):
        self._soortVerkeersdeelnemer.set_waarde(value, owner=self)
