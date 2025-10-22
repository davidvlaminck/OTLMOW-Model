# coding=utf-8
from datetime import datetime
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkObjectSV import LinkObjectSV
from otlmow_model.OtlmowModel.BaseClasses.DateTimeField import DateTimeField
from ...Datatypes.KlSignalisatieOntwerpStatus import KlSignalisatieOntwerpStatus
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SignalisatieOntwerp(LinkObjectSV):
    """TODO"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Verkeersteken.bevatVerkeersteken', target='https://data.vlaanderen.be/ns/mobiliteit#OntwerpVerkeersteken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/todo#bevatOntwerp', target='https://data.vlaanderen.be/ns/mobiliteit#AanvullendReglementOntwerp', direction='o')  # o = direction: outgoing

        self._datum = OTLAttribuut(field=DateTimeField,
                                   naam='datum',
                                   label='datum',
                                   objectUri='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp.datum',
                                   definition='TODO',
                                   owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp.naam',
                                  definition='TODO',
                                  owner=self)

        self._status = OTLAttribuut(field=KlSignalisatieOntwerpStatus,
                                    naam='status',
                                    label='status',
                                    objectUri='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp.status',
                                    definition='TODO',
                                    owner=self)

        self._verantwoordelijkeOrganisatie = OTLAttribuut(field=StringField,
                                                          naam='verantwoordelijkeOrganisatie',
                                                          label='verantwoordelijke organisatie',
                                                          objectUri='https://data.vlaanderen.be/ns/mobiliteit#SignalisatieOntwerp.verantwoordelijkeOrganisatie',
                                                          definition='TODO',
                                                          owner=self)

    @property
    def datum(self) -> datetime:
        """TODO"""
        return self._datum.get_waarde()

    @datum.setter
    def datum(self, value):
        self._datum.set_waarde(value, owner=self)

    @property
    def naam(self) -> str:
        """TODO"""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)

    @property
    def status(self) -> str:
        """TODO"""
        return self._status.get_waarde()

    @status.setter
    def status(self, value):
        self._status.set_waarde(value, owner=self)

    @property
    def verantwoordelijkeOrganisatie(self) -> str:
        """TODO"""
        return self._verantwoordelijkeOrganisatie.get_waarde()

    @verantwoordelijkeOrganisatie.setter
    def verantwoordelijkeOrganisatie(self, value):
        self._verantwoordelijkeOrganisatie.set_waarde(value, owner=self)
