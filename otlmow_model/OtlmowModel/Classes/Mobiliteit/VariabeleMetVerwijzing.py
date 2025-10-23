# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes..Variabele import Variabele, VariabeleWaarden
from ...Datatypes.DtcCodelijst import DtcCodelijst, DtcCodelijstWaarden
from ...Datatypes.DtcTemplate import DtcTemplate, DtcTemplateWaarden
from ...Datatypes.Variabele import Variabele


# Generated with OTLClassCreator. To modify: extend, do not edit
class VariabeleMetVerwijzing(Variabele):
    """TODO"""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#VariabeleMetVerwijzing'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Variabele.heeftWaardeVoor', target='http://lblod.data.gift/vocabularies/variables/VariableInstance', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.definieert', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='i')  # i = direction: incoming

        self._codelijst = OTLAttribuut(field=DtcCodelijst,
                                       naam='codelijst',
                                       label='codelijst',
                                       objectUri='https://data.vlaanderen.be/ns/mobiliteit#VariabeleMetVerwijzing.codelijst',
                                       definition='De codelijst met mogelijke waarden waaruit gekozen kan worden voor de variabele',
                                       owner=self)

        self._standaardwaarde = OTLAttribuut(field=DtcVariabele,
                                             naam='standaardwaarde',
                                             label='standaard waarde',
                                             objectUri='https://data.vlaanderen.be/ns/mobiliteit#VariabeleMetVerwijzing.standaardwaarde',
                                             definition='Dit is een resource (bijvoorbeeld concept uit een codelijst) die als uitgangspunt of suggestie dient bij het invullen van de variabele.',
                                             owner=self)

        self._template = OTLAttribuut(field=DtcTemplate,
                                      naam='template',
                                      label='template',
                                      objectUri='https://data.vlaanderen.be/ns/mobiliteit#VariabeleMetVerwijzing.template',
                                      definition='TODO',
                                      owner=self)

    @property
    def codelijst(self) -> DtcCodelijstWaarden:
        """De codelijst met mogelijke waarden waaruit gekozen kan worden voor de variabele"""
        return self._codelijst.get_waarde()

    @codelijst.setter
    def codelijst(self, value):
        self._codelijst.set_waarde(value, owner=self)

    @property
    def standaardwaarde(self) -> VariabeleWaarden:
        """Dit is een resource (bijvoorbeeld concept uit een codelijst) die als uitgangspunt of suggestie dient bij het invullen van de variabele."""
        return self._standaardwaarde.get_waarde()

    @standaardwaarde.setter
    def standaardwaarde(self, value):
        self._standaardwaarde.set_waarde(value, owner=self)

    @property
    def template(self) -> DtcTemplateWaarden:
        """TODO"""
        return self._template.get_waarde()

    @template.setter
    def template(self, value):
        self._template.set_waarde(value, owner=self)
