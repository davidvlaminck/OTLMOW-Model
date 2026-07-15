# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VPlan(AIMNaamObject):
    """Beschrijving van de werking en sturing van een verkeersregelinstallatie, waarin de fasering, conflicten, prioriteiten en schakellogica van de verkeerslichten eenduidig worden vastgelegd, zodat de regeling correct kan worden geïmplementeerd, geconfigureerd en beheerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VPlan'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVPlan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVPlan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', direction='i')  # i = direction: incoming

        self._plannummer = OTLAttribuut(field=StringField,
                                        naam='plannummer',
                                        label='plannummer',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VPlan.plannummer',
                                        definition='Nummer van het V-plan.',
                                        owner=self)

    @property
    def plannummer(self) -> str:
        """Nummer van het V-plan."""
        return self._plannummer.get_waarde()

    @plannummer.setter
    def plannummer(self, value):
        self._plannummer.set_waarde(value, owner=self)
