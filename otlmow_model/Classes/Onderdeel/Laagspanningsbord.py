# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlAardingAardingsnet import KlAardingAardingsnet
from otlmow_model.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere, KwantWrdInAmpereWaarden
from otlmow_model.Datatypes.KwantWrdInKiloAmpere import KwantWrdInKiloAmpere, KwantWrdInKiloAmpereWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Laagspanningsbord(AIMNaamObject, PuntGeometrie):
    """Verzameling van alle elektrische componenten nodig voor de voeding en sturing van applicaties die erop aangesloten zijn. Omvat onder andere automaten,klemmenblokken,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDerden')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais')

        self._aardingsnet = OTLAttribuut(field=KlAardingAardingsnet,
                                         naam='aardingsnet',
                                         label='aardingsnet',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.aardingsnet',
                                         definition='De manier waarop respectievelijk de bron en de verbruiker met de aarde verbonden worden om op die manier foutstromen af te voeren.',
                                         owner=self)

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.elektrischSchema',
                                              usagenote='Bestanden van het type pdf,dwg of dxf.',
                                              definition='Het elektrisch aansluitschema van het laagspanningsbord.',
                                              owner=self)

        self._kortsluitVermogen = OTLAttribuut(field=KwantWrdInKiloAmpere,
                                               naam='kortsluitVermogen',
                                               label='kortsluitvermogen',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.kortsluitVermogen',
                                               definition='De theoretische stroom die gaat lopen bij een kortsluiting wanneer de beveiliging nog niet heeft ingegrepen.',
                                               owner=self)

        self._nominaleStroom = OTLAttribuut(field=KwantWrdInAmpere,
                                            naam='nominaleStroom',
                                            label='nominale stroom',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.nominaleStroom',
                                            definition='De maximale stroom die door de installatie continu mag vloeien onder normale omstandigheden.',
                                            owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInAmpere,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.vermogen',
                                      usagenote='Attribuut uit gebruik sinds versie 2.7.0 ',
                                      deprecated_version='2.7.0',
                                      definition='Het vermogen van het laagspanningsbord.',
                                      owner=self)

    @property
    def aardingsnet(self) -> str:
        """De manier waarop respectievelijk de bron en de verbruiker met de aarde verbonden worden om op die manier foutstromen af te voeren."""
        return self._aardingsnet.get_waarde()

    @aardingsnet.setter
    def aardingsnet(self, value):
        self._aardingsnet.set_waarde(value, owner=self)

    @property
    def elektrischSchema(self) -> DtcDocumentWaarden:
        """Het elektrisch aansluitschema van het laagspanningsbord."""
        return self._elektrischSchema.get_waarde()

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def kortsluitVermogen(self) -> KwantWrdInKiloAmpereWaarden:
        """De theoretische stroom die gaat lopen bij een kortsluiting wanneer de beveiliging nog niet heeft ingegrepen."""
        return self._kortsluitVermogen.get_waarde()

    @kortsluitVermogen.setter
    def kortsluitVermogen(self, value):
        self._kortsluitVermogen.set_waarde(value, owner=self)

    @property
    def nominaleStroom(self) -> KwantWrdInAmpereWaarden:
        """De maximale stroom die door de installatie continu mag vloeien onder normale omstandigheden."""
        return self._nominaleStroom.get_waarde()

    @nominaleStroom.setter
    def nominaleStroom(self, value):
        self._nominaleStroom.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInAmpereWaarden:
        """Het vermogen van het laagspanningsbord."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
