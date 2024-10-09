# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlHSBeveiligingscelHoogspanningszekering import KlHSBeveiligingscelHoogspanningszekering
from ...Datatypes.KlHSBeveiligingscelMerk import KlHSBeveiligingscelMerk
from ...Datatypes.KlHSBeveiligingscelModelnaam import KlHSBeveiligingscelModelnaam
from ...Datatypes.KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar import KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar
from ...Datatypes.KlHSBeveiligingscelSchakelmateriaalKlasse import KlHSBeveiligingscelSchakelmateriaalKlasse
from ...Datatypes.KlHSBeveiligingscelSchakelmateriaalType import KlHSBeveiligingscelSchakelmateriaalType
from ...Datatypes.KwantWrdInAmpere import KwantWrdInAmpere, KwantWrdInAmpereWaarden
from ...Datatypes.KwantWrdInJaar import KwantWrdInJaar, KwantWrdInJaarWaarden
from ...Datatypes.KwantWrdInKiloAmpere import KwantWrdInKiloAmpere, KwantWrdInKiloAmpereWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HSBeveiligingscel(AIMNaamObject, PuntGeometrie):
    """Cel die de hoogspanningsschakelinrichting omvat. Hieronder vallen onder meer de lastscheidingsschakelaar,smeltveiligheden,aardingsschakelaar,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBHoogspanning', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel', direction='i')  # i = direction: incoming

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.elektrischSchema',
                                              usagenote='Bestanden van het type pdf,dwg of dxf.',
                                              definition='Elektrisch aansluitschema van de HS beveiligingscel.',
                                              owner=self)

        self._heeftAardingsschakelaar = OTLAttribuut(field=BooleanField,
                                                     naam='heeftAardingsschakelaar',
                                                     label='heeft aardingsschakelaar',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.heeftAardingsschakelaar',
                                                     definition='Geeft aan of er al dan niet een aardingsschakelaar aanwezig is.',
                                                     owner=self)

        self._heeftreserveZekering = OTLAttribuut(field=BooleanField,
                                                  naam='heeftreserveZekering',
                                                  label='heeft reserve zekering',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.heeftreserveZekering',
                                                  definition='Is er een reserve zekering aanwezig?',
                                                  owner=self)

        self._hoogspanningszekering = OTLAttribuut(field=KlHSBeveiligingscelHoogspanningszekering,
                                                   naam='hoogspanningszekering',
                                                   label='hoogspanningszekering',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.hoogspanningszekering',
                                                   definition='Waarde van de hoogspanningszekering.',
                                                   owner=self)

        self._keuringsfrequentie = OTLAttribuut(field=KwantWrdInJaar,
                                                naam='keuringsfrequentie',
                                                label='keuringsfrequentie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.keuringsfrequentie',
                                                definition='Frequentie (in jaar) waarmee de installatie moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle.',
                                                owner=self)

        self._kortsluitStroom = OTLAttribuut(field=KwantWrdInKiloAmpere,
                                             naam='kortsluitStroom',
                                             label='kortsluitstroom',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.kortsluitStroom',
                                             definition='De maximale elektrische stroom die kan lopen in een elektrisch circuit.',
                                             owner=self)

        self._kortsluitVermogen = OTLAttribuut(field=KwantWrdInKiloAmpere,
                                               naam='kortsluitVermogen',
                                               label='kortsluitvermogen',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.kortsluitVermogen',
                                               definition='De theoretische stroom die gaat lopen bij een kortsluiting wanneer de beveiliging nog niet heeft ingegrepen.',
                                               owner=self)

        self._merk = OTLAttribuut(field=KlHSBeveiligingscelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.merk',
                                  definition='Merk van de HS beveiligingscel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHSBeveiligingscelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.modelnaam',
                                       definition='Modelnaam van de HS beveiligingscel.',
                                       owner=self)

        self._overstroombeveiligingInstelwaarde = OTLAttribuut(field=KwantWrdInAmpere,
                                                               naam='overstroombeveiligingInstelwaarde',
                                                               label='overstroombeveiliging instelwaarde',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingInstelwaarde',
                                                               definition='Instelwaarde van de overstroombeveiliging.',
                                                               owner=self)

        self._overstroombeveiligingType = OTLAttribuut(field=StringField,
                                                       naam='overstroombeveiligingType',
                                                       label='overstroombeveiliging type',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingType',
                                                       definition='Type overstroombeveiliging.',
                                                       owner=self)

        self._overstroombeveiligingVermogenschakelaar = OTLAttribuut(field=KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar,
                                                                     naam='overstroombeveiligingVermogenschakelaar',
                                                                     label='overstroombeveiliging vermogenschakelaar',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingVermogenschakelaar',
                                                                     definition='Directe of indirecte overstroombeveiliging van de vermogenschakelaar.',
                                                                     owner=self)

        self._schakelmateriaalKlasse = OTLAttribuut(field=KlHSBeveiligingscelSchakelmateriaalKlasse,
                                                    naam='schakelmateriaalKlasse',
                                                    label='schakelmateriaal klasse',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.schakelmateriaalKlasse',
                                                    definition='Klasse van het schakelmateriaal volgens Synergrid.',
                                                    owner=self)

        self._schakelmateriaalType = OTLAttribuut(field=KlHSBeveiligingscelSchakelmateriaalType,
                                                  naam='schakelmateriaalType',
                                                  label='schakelmateriaal type',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.schakelmateriaalType',
                                                  definition='Type van schakelmateriaal.',
                                                  owner=self)

    @property
    def elektrischSchema(self) -> DtcDocumentWaarden:
        """Elektrisch aansluitschema van de HS beveiligingscel."""
        return self._elektrischSchema.get_waarde()

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def heeftAardingsschakelaar(self) -> bool:
        """Geeft aan of er al dan niet een aardingsschakelaar aanwezig is."""
        return self._heeftAardingsschakelaar.get_waarde()

    @heeftAardingsschakelaar.setter
    def heeftAardingsschakelaar(self, value):
        self._heeftAardingsschakelaar.set_waarde(value, owner=self)

    @property
    def heeftreserveZekering(self) -> bool:
        """Is er een reserve zekering aanwezig?"""
        return self._heeftreserveZekering.get_waarde()

    @heeftreserveZekering.setter
    def heeftreserveZekering(self, value):
        self._heeftreserveZekering.set_waarde(value, owner=self)

    @property
    def hoogspanningszekering(self) -> str:
        """Waarde van de hoogspanningszekering."""
        return self._hoogspanningszekering.get_waarde()

    @hoogspanningszekering.setter
    def hoogspanningszekering(self, value):
        self._hoogspanningszekering.set_waarde(value, owner=self)

    @property
    def keuringsfrequentie(self) -> KwantWrdInJaarWaarden:
        """Frequentie (in jaar) waarmee de installatie moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."""
        return self._keuringsfrequentie.get_waarde()

    @keuringsfrequentie.setter
    def keuringsfrequentie(self, value):
        self._keuringsfrequentie.set_waarde(value, owner=self)

    @property
    def kortsluitStroom(self) -> KwantWrdInKiloAmpereWaarden:
        """De maximale elektrische stroom die kan lopen in een elektrisch circuit."""
        return self._kortsluitStroom.get_waarde()

    @kortsluitStroom.setter
    def kortsluitStroom(self, value):
        self._kortsluitStroom.set_waarde(value, owner=self)

    @property
    def kortsluitVermogen(self) -> KwantWrdInKiloAmpereWaarden:
        """De theoretische stroom die gaat lopen bij een kortsluiting wanneer de beveiliging nog niet heeft ingegrepen."""
        return self._kortsluitVermogen.get_waarde()

    @kortsluitVermogen.setter
    def kortsluitVermogen(self, value):
        self._kortsluitVermogen.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk van de HS beveiligingscel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de HS beveiligingscel."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def overstroombeveiligingInstelwaarde(self) -> KwantWrdInAmpereWaarden:
        """Instelwaarde van de overstroombeveiliging."""
        return self._overstroombeveiligingInstelwaarde.get_waarde()

    @overstroombeveiligingInstelwaarde.setter
    def overstroombeveiligingInstelwaarde(self, value):
        self._overstroombeveiligingInstelwaarde.set_waarde(value, owner=self)

    @property
    def overstroombeveiligingType(self) -> str:
        """Type overstroombeveiliging."""
        return self._overstroombeveiligingType.get_waarde()

    @overstroombeveiligingType.setter
    def overstroombeveiligingType(self, value):
        self._overstroombeveiligingType.set_waarde(value, owner=self)

    @property
    def overstroombeveiligingVermogenschakelaar(self) -> str:
        """Directe of indirecte overstroombeveiliging van de vermogenschakelaar."""
        return self._overstroombeveiligingVermogenschakelaar.get_waarde()

    @overstroombeveiligingVermogenschakelaar.setter
    def overstroombeveiligingVermogenschakelaar(self, value):
        self._overstroombeveiligingVermogenschakelaar.set_waarde(value, owner=self)

    @property
    def schakelmateriaalKlasse(self) -> str:
        """Klasse van het schakelmateriaal volgens Synergrid."""
        return self._schakelmateriaalKlasse.get_waarde()

    @schakelmateriaalKlasse.setter
    def schakelmateriaalKlasse(self, value):
        self._schakelmateriaalKlasse.set_waarde(value, owner=self)

    @property
    def schakelmateriaalType(self) -> str:
        """Type van schakelmateriaal."""
        return self._schakelmateriaalType.get_waarde()

    @schakelmateriaalType.setter
    def schakelmateriaalType(self, value):
        self._schakelmateriaalType.set_waarde(value, owner=self)
