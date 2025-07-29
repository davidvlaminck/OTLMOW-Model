# coding=utf-8
from typing import List
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlIlluminatorMerk import KlIlluminatorMerk
from ...Datatypes.KlIlluminatorModelnaam import KlIlluminatorModelnaam
from ...Datatypes.KwantWrdInMaand import KwantWrdInMaand, KwantWrdInMaandWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Illuminator(AIMNaamObject, PuntGeometrie):
    """Een verlichtingscomponent gekoppeld aan een camera dat dient om voldoende belichting te bieden voor het detecteren en herkennen van oa. voertuigen, vaak door gebruik van infraroodlicht zodat de flits onzichtbaar is voor het menselijk oog."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Illuminator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', direction='i')  # i = direction: incoming

        self._merk = OTLAttribuut(field=KlIlluminatorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Illuminator.merk',
                                  definition='Het merk van de illuminator.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIlluminatorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Illuminator.modelnaam',
                                       definition='De modelnaam van de illuminator.',
                                       owner=self)

        self._plaatsingsdatum = OTLAttribuut(field=DateField,
                                             naam='plaatsingsdatum',
                                             label='plaatsingsdatum',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Illuminator.plaatsingsdatum',
                                             definition='De datum waarop de illuminator fysiek is geïnstalleerd of gemonteerd op de beoogde locatie.',
                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Illuminator.technischeFiche',
                                             usagenote='Bestanden van het type pdf.',
                                             kardinaliteit_max='*',
                                             definition='Technische fiche van dit element.',
                                             owner=self)

        self._waarborgperiode = OTLAttribuut(field=KwantWrdInMaand,
                                             naam='waarborgperiode',
                                             label='waarborgperiode',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Illuminator.waarborgperiode',
                                             definition='De aaneengesloten periode in maanden vanaf de plaatsingsdatum waarin de leverancier of fabrikant garandeert dat de illuminator vrij is van fabricage- en materiaalfouten.',
                                             owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de illuminator."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de illuminator."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def plaatsingsdatum(self) -> date:
        """De datum waarop de illuminator fysiek is geïnstalleerd of gemonteerd op de beoogde locatie."""
        return self._plaatsingsdatum.get_waarde()

    @plaatsingsdatum.setter
    def plaatsingsdatum(self, value):
        self._plaatsingsdatum.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """Technische fiche van dit element."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def waarborgperiode(self) -> KwantWrdInMaandWaarden:
        """De aaneengesloten periode in maanden vanaf de plaatsingsdatum waarin de leverancier of fabrikant garandeert dat de illuminator vrij is van fabricage- en materiaalfouten."""
        return self._waarborgperiode.get_waarde()

    @waarborgperiode.setter
    def waarborgperiode(self, value):
        self._waarborgperiode.set_waarde(value, owner=self)
