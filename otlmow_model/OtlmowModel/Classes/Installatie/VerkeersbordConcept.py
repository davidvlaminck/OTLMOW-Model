# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcExterneReferentie import DtcExterneReferentie, DtcExterneReferentieWaarden
from ...Datatypes.KlVerkeersbordCategorie import KlVerkeersbordCategorie
from ...Datatypes.KlVerkeersbordCode import KlVerkeersbordCode
from ...Datatypes.KlVerkeersbordconceptStatus import KlVerkeersbordconceptStatus
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeersbordConcept(AIMNaamObject, GeenGeometrie):
    """Inhoudelijke definitie van de betekenis van een verkeersbord zoals opgenomen in de wegcode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken', direction='i')  # i = direction: incoming

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.afbeelding',
                                        kardinaliteit_max='*',
                                        definition='De afbeelding van het verkeersbordconcept.',
                                        owner=self)

        self._betekenis = OTLAttribuut(field=StringField,
                                       naam='betekenis',
                                       label='betekenis',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.betekenis',
                                       definition='Betekenis die gegeven wordt aan dit soort verkeersbord volgens de wegcode.',
                                       owner=self)

        self._rechtsgrondOnderdeel = OTLAttribuut(field=DtcExterneReferentie,
                                                  naam='rechtsgrondOnderdeel',
                                                  label='rechtsgrondonderdeel',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.rechtsgrondOnderdeel',
                                                  usagenote='Verwijst meestal naar een artikel in de wegcode die informatie over dit verkeersbordconcept bevat. Bijvoorbeeld: artikel 68.3 voor verbodsborden.',
                                                  definition='Verwijst naar een rechtsgrondonderdeel over dit verkeersbordconcept.',
                                                  owner=self)

        self._status = OTLAttribuut(field=KlVerkeersbordconceptStatus,
                                    naam='status',
                                    label='status',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.status',
                                    usagenote='Bijvoorbeeld: stabiel, onstabiel, afgeschaft. Een bord met snelheidslimiet van 60 km/u is bijvoorbeeld afgeschaft.',
                                    definition='Duidt of het verkeersbordconcept nog gebruikt wordt.',
                                    owner=self)

        self._verkeersbordCategorie = OTLAttribuut(field=KlVerkeersbordCategorie,
                                                   naam='verkeersbordCategorie',
                                                   label='verkeersbord categorie',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.verkeersbordCategorie',
                                                   definition='Categorie van het verkeersbordconcept.	.',
                                                   owner=self)

        self._verkeersbordCode = OTLAttribuut(field=KlVerkeersbordCode,
                                              naam='verkeersbordCode',
                                              label='verkeersbordcode',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept.verkeersbordCode',
                                              definition='Code die aan dit soort bord gegeven wordt binnen de wegcode.',
                                              owner=self)

    @property
    def afbeelding(self) -> List[DtcDocumentWaarden]:
        """De afbeelding van het verkeersbordconcept."""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def betekenis(self) -> str:
        """Betekenis die gegeven wordt aan dit soort verkeersbord volgens de wegcode."""
        return self._betekenis.get_waarde()

    @betekenis.setter
    def betekenis(self, value):
        self._betekenis.set_waarde(value, owner=self)

    @property
    def rechtsgrondOnderdeel(self) -> DtcExterneReferentieWaarden:
        """Verwijst naar een rechtsgrondonderdeel over dit verkeersbordconcept."""
        return self._rechtsgrondOnderdeel.get_waarde()

    @rechtsgrondOnderdeel.setter
    def rechtsgrondOnderdeel(self, value):
        self._rechtsgrondOnderdeel.set_waarde(value, owner=self)

    @property
    def status(self) -> str:
        """Duidt of het verkeersbordconcept nog gebruikt wordt."""
        return self._status.get_waarde()

    @status.setter
    def status(self, value):
        self._status.set_waarde(value, owner=self)

    @property
    def verkeersbordCategorie(self) -> str:
        """Categorie van het verkeersbordconcept.	."""
        return self._verkeersbordCategorie.get_waarde()

    @verkeersbordCategorie.setter
    def verkeersbordCategorie(self, value):
        self._verkeersbordCategorie.set_waarde(value, owner=self)

    @property
    def verkeersbordCode(self) -> str:
        """Code die aan dit soort bord gegeven wordt binnen de wegcode."""
        return self._verkeersbordCode.get_waarde()

    @verkeersbordCode.setter
    def verkeersbordCode(self, value):
        self._verkeersbordCode.set_waarde(value, owner=self)
