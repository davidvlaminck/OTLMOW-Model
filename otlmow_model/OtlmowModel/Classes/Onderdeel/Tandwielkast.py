# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcOlieType import DtcOlieType, DtcOlieTypeWaarden
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ...Datatypes.KlTandwielkastMerk import KlTandwielkastMerk
from ...Datatypes.KlTandwielkastModelnaam import KlTandwielkastModelnaam
from ...Datatypes.KwantWrdInLiter import KwantWrdInLiter, KwantWrdInLiterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tandwielkast(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Systeem dat mechanisch vermogen van een motor omzet naar mechanisch vermogen met een kracht/snelheidsverhouding op maat van een bewegingsmechanisme."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dichting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flenskoppeling', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Naaf', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderstel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riemschijf', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwiel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging', direction='o')  # o = direction: outgoing

        self._hoeveelheidOlie = OTLAttribuut(field=KwantWrdInLiter,
                                             naam='hoeveelheidOlie',
                                             label='hoeveelheid olie',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast.hoeveelheidOlie',
                                             definition='De hoeveelheid olie die vereist is voor het normaal functioneren van de reductiekast, zoals berekend bij installatie van de reductiekast.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlTandwielkastMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast.merk',
                                  definition='Het merk van de reductiekast.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlTandwielkastModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast.modelnaam',
                                       definition='De modelnaam volgens de fabrikant van de reductiekast.',
                                       owner=self)

        self._reductieverhouding = OTLAttribuut(field=FloatOrDecimalField,
                                                naam='reductieverhouding',
                                                label='reductieverhouding',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast.reductieverhouding',
                                                definition='Geeft de reductieverhouding van het uitgaande toerental tegenover het ingaande toerental weer.',
                                                owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast.technischeFiche',
                                             definition='De technische fiche van de tandwielkast.',
                                             owner=self)

        self._typeOlie = OTLAttribuut(field=DtcOlieType,
                                      naam='typeOlie',
                                      label='type olie',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast.typeOlie',
                                      definition='Geeft aan welk type olie gebruikt wordt in deze reductiekast.',
                                      owner=self)

    @property
    def hoeveelheidOlie(self) -> KwantWrdInLiterWaarden:
        """De hoeveelheid olie die vereist is voor het normaal functioneren van de reductiekast, zoals berekend bij installatie van de reductiekast."""
        return self._hoeveelheidOlie.get_waarde()

    @hoeveelheidOlie.setter
    def hoeveelheidOlie(self, value):
        self._hoeveelheidOlie.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de reductiekast."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam volgens de fabrikant van de reductiekast."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def reductieverhouding(self) -> float:
        """Geeft de reductieverhouding van het uitgaande toerental tegenover het ingaande toerental weer."""
        return self._reductieverhouding.get_waarde()

    @reductieverhouding.setter
    def reductieverhouding(self, value):
        self._reductieverhouding.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de tandwielkast."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def typeOlie(self) -> DtcOlieTypeWaarden:
        """Geeft aan welk type olie gebruikt wordt in deze reductiekast."""
        return self._typeOlie.get_waarde()

    @typeOlie.setter
    def typeOlie(self, value):
        self._typeOlie.set_waarde(value, owner=self)
