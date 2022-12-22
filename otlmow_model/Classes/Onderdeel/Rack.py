# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.BaseClasses.IntegerField import IntegerField
from otlmow_model.Datatypes.KlRackMerk import KlRackMerk
from otlmow_model.Datatypes.KlRackModelnaam import KlRackModelnaam
from otlmow_model.Datatypes.KlRackType import KlRackType
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rack(AIMNaamObject, PuntGeometrie):
    """Interne draagstructuur binnen een behuizing voor (elektromechanische) toestellen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#RHZModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVVoedingsmodule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#RHZModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVVoedingsmodule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC')

        self._diepte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.diepte',
                                    definition='De diepte van het rack tussen de voorste en achterste rails.',
                                    owner=self)

        self._hoogteInRU = OTLAttribuut(field=IntegerField,
                                        naam='hoogteInRU',
                                        label='hoogte in RU',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.hoogteInRU',
                                        definition='Bruikbare ruimte om toestellen te monteren, uitgedrukt in RU (rack units).',
                                        owner=self)

        self._huidigBeeld = OTLAttribuut(field=DtcDocument,
                                         naam='huidigBeeld',
                                         label='huidig beeld',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.huidigBeeld',
                                         definition='Foto of schematische voorstelling van de huidige samenstelling van de samenstelling in het rack.',
                                         owner=self)

        self._merk = OTLAttribuut(field=KlRackMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.merk',
                                  definition='Merk waarmee de fabrikant dit type rack identificeert.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlRackModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.modelnaam',
                                       definition='Modelnaam waarmee de fabrikant dit type toestel identificeert.',
                                       owner=self)

        self._rackType = OTLAttribuut(field=KlRackType,
                                      naam='rackType',
                                      label='Rack type',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.rackType',
                                      definition='Geeft het type aan voor een rack volgens een keuzelijst van beschikbare types.',
                                      owner=self)

    @property
    def diepte(self) -> KwantWrdInCentimeterWaarden:
        """De diepte van het rack tussen de voorste en achterste rails."""
        return self._diepte.get_waarde()

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def hoogteInRU(self) -> int:
        """Bruikbare ruimte om toestellen te monteren, uitgedrukt in RU (rack units)."""
        return self._hoogteInRU.get_waarde()

    @hoogteInRU.setter
    def hoogteInRU(self, value):
        self._hoogteInRU.set_waarde(value, owner=self)

    @property
    def huidigBeeld(self) -> DtcDocumentWaarden:
        """Foto of schematische voorstelling van de huidige samenstelling van de samenstelling in het rack."""
        return self._huidigBeeld.get_waarde()

    @huidigBeeld.setter
    def huidigBeeld(self, value):
        self._huidigBeeld.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk waarmee de fabrikant dit type rack identificeert."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def rackType(self) -> str:
        """Geeft het type aan voor een rack volgens een keuzelijst van beschikbare types."""
        return self._rackType.get_waarde()

    @rackType.setter
    def rackType(self, value):
        self._rackType.set_waarde(value, owner=self)
