# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Verkeerslicht import Verkeerslicht
from otlmow_model.Datatypes.KlVriBewaking import KlVriBewaking


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeerslichtRood(Verkeerslicht):
    """Een lichtbron met rode kleur om de weggebruikers aan te geven dat het verboden is de stopstreep of, zo er geen stopstreep is, het verkeerslicht zelf, voorbij te rijden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtRood'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn')

        self._typeBewaking = OTLAttribuut(field=KlVriBewaking,
                                          naam='typeBewaking',
                                          label='type bewaking',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtRood.typeBewaking',
                                          definition='Type bewaking van het rode verkeerslicht.',
                                          owner=self)

    @property
    def typeBewaking(self) -> str:
        """Type bewaking van het rode verkeerslicht."""
        return self._typeBewaking.get_waarde()

    @typeBewaking.setter
    def typeBewaking(self, value):
        self._typeBewaking.set_waarde(value, owner=self)
