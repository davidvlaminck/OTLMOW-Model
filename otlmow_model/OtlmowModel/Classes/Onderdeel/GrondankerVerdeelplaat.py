# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcAfmetingBxlxhInCm import DtcAfmetingBxlxhInCm, DtcAfmetingBxlxhInCmWaarden
from ...Datatypes.DtcConstructiestaalspecificaties import DtcConstructiestaalspecificaties, DtcConstructiestaalspecificatiesWaarden
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GrondankerVerdeelplaat(AIMObject, PuntGeometrie):
    """Dikke staalplaat tussen de te verankeren constructie en ankerkop. Wordt toegepast om de ankerkracht te spreiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrondankerVerdeelplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInCm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrondankerVerdeelplaat.afmetingen',
                                        definition='Afmetingen van de verdeeplaat van het grondanker.',
                                        owner=self)

        self._diameterOpeningDoorgangAnker = OTLAttribuut(field=KwantWrdInCentimeter,
                                                          naam='diameterOpeningDoorgangAnker',
                                                          label='afmetingen',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrondankerVerdeelplaat.diameterOpeningDoorgangAnker',
                                                          definition='De diameter van de opening van de doorgang van het anker.',
                                                          owner=self)

        self._staalspecificaties = OTLAttribuut(field=DtcConstructiestaalspecificaties,
                                                naam='staalspecificaties',
                                                label='staalspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrondankerVerdeelplaat.staalspecificaties',
                                                definition='Specificaties van het staal.',
                                                owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlxhInCmWaarden:
        """Afmetingen van de verdeeplaat van het grondanker."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def diameterOpeningDoorgangAnker(self) -> KwantWrdInCentimeterWaarden:
        """De diameter van de opening van de doorgang van het anker."""
        return self._diameterOpeningDoorgangAnker.get_waarde()

    @diameterOpeningDoorgangAnker.setter
    def diameterOpeningDoorgangAnker(self, value):
        self._diameterOpeningDoorgangAnker.set_waarde(value, owner=self)

    @property
    def staalspecificaties(self) -> DtcConstructiestaalspecificatiesWaarden:
        """Specificaties van het staal."""
        return self._staalspecificaties.get_waarde()

    @staalspecificaties.setter
    def staalspecificaties(self, value):
        self._staalspecificaties.set_waarde(value, owner=self)
