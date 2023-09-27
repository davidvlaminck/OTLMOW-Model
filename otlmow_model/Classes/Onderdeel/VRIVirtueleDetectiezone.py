# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Detectielus import Detectielus
from otlmow_model.Datatypes.KlVriLusFunctie import KlVriLusFunctie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRIVirtueleDetectiezone(Detectielus, VlakGeometrie):
    """Een virtuele detectiezone is een draadloos alternatief voor een traditionele lus. Op basis van GPS gegevens wordt een zone of traject vastgelegd waarbinnen er (al dan niet selectieve) input dient geleverd te worden aan de verkeersregelaar. De virtuele detectiezone kan ook gebruikt worden om de detectiezones van detectiecamera's en radars te inventariseren. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar')

        self._functie = OTLAttribuut(field=KlVriLusFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone.functie',
                                     definition='Functie van de VRI detectiezone.',
                                     owner=self)

    @property
    def functie(self) -> str:
        """Functie van de VRI detectiezone."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)
