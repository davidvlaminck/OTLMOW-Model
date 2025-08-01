# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlKabelmofType import KlKabelmofType
from ...Datatypes.KlKabelmofVerbinding import KlKabelmofVerbinding
from ...Datatypes.KlNetwerkType import KlNetwerkType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelmof(AIMNaamObject, PuntGeometrie):
    """Een verbindingsgreep die aansluitingen van kabels rondom afsluit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TechnischePut', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DynBordGroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Z30Groep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LoopTerminationAndProtection', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus', direction='u')  # u = unidirectional

        self._netwerktype = OTLAttribuut(field=KlNetwerkType,
                                         naam='netwerktype',
                                         label='netwerktype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.netwerktype',
                                         definition='Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlKabelmofType,
                                  naam='type',
                                  label='type kabelmof',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.type',
                                  definition='Soort mof volgens een lijst van types.',
                                  owner=self)

        self._verbindingstype = OTLAttribuut(field=KlKabelmofVerbinding,
                                             naam='verbindingstype',
                                             label='verbindingstype',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.verbindingstype',
                                             definition='Geeft het type aansluiting in de mof aan.',
                                             owner=self)

    @property
    def netwerktype(self) -> str:
        """Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire."""
        return self._netwerktype.get_waarde()

    @netwerktype.setter
    def netwerktype(self, value):
        self._netwerktype.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Soort mof volgens een lijst van types."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def verbindingstype(self) -> str:
        """Geeft het type aansluiting in de mof aan."""
        return self._verbindingstype.get_waarde()

    @verbindingstype.setter
    def verbindingstype(self, value):
        self._verbindingstype.set_waarde(value, owner=self)
