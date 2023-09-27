# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VentilatieAfsluitklep(AIMObject, PuntGeometrie):
    """Constructie voor het fysiek afsluiten van een ventilatieschacht die verhindert dat luchtstromen van de (dwars)ventilatie door de schachten gaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VentilatieAfsluitklep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart')

        self._heeftManueleBediening = OTLAttribuut(field=BooleanField,
                                                   naam='heeftManueleBediening',
                                                   label='Heeft manuele bediening',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VentilatieAfsluitklep.heeftManueleBediening',
                                                   definition='Geeft aan of de afsluitklep manueel kan bediend worden.',
                                                   owner=self)

    @property
    def heeftManueleBediening(self) -> bool:
        """Geeft aan of de afsluitklep manueel kan bediend worden."""
        return self._heeftManueleBediening.get_waarde()

    @heeftManueleBediening.setter
    def heeftManueleBediening(self, value):
        self._heeftManueleBediening.set_waarde(value, owner=self)
