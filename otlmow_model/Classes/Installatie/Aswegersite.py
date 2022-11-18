# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcBereikInKg import DtcBereikInKg, DtcBereikInKgWaarden
from otlmow_model.Datatypes.DtcKwaliteitscertifcaat import DtcKwaliteitscertifcaat, DtcKwaliteitscertifcaatWaarden
from otlmow_model.Datatypes.KlAfmetingAswegerzone import KlAfmetingAswegerzone
from otlmow_model.Datatypes.KlAswegersiteTypeMarkering import KlAswegersiteTypeMarkering
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aswegersite(AIMNaamObject, VlakGeometrie):
    """Het geheel van infrastructuurelementen en toestellen op één locatie voor de exploitatie van een asweger."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._afmetingAswegerZone = OTLAttribuut(field=KlAfmetingAswegerzone,
                                                 naam='afmetingAswegerZone',
                                                 label='afmeting aswegerzone',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.afmetingAswegerZone',
                                                 definition='De afmeting van de zone voor en na de weegplaat, inclusief de weegplaat zelf, als een waarde uit een vaste lijst van standaard afmetingen.',
                                                 owner=self)

        self._kwaliteitscertificaat = OTLAttribuut(field=DtcKwaliteitscertifcaat,
                                                   naam='kwaliteitscertificaat',
                                                   label='kwaliteitscertificaat',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.kwaliteitscertificaat',
                                                   definition='Het certificaat uitgereikt bij de eerste ijk nodig voor de rechtsgeldige uitbating van de aswegersite.',
                                                   owner=self)

        self._typeMarkering = OTLAttribuut(field=KlAswegersiteTypeMarkering,
                                           naam='typeMarkering',
                                           label='type markering',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.typeMarkering',
                                           definition='Geeft welke wegmarkering er aanwezig zijn rond de aswegerzone als een waarde uit een vaste lijst van mogelijkheden.',
                                           owner=self)

        self._weegvermogenBereik = OTLAttribuut(field=DtcBereikInKg,
                                                naam='weegvermogenBereik',
                                                label='weegvermogen bereik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.weegvermogenBereik',
                                                definition='Het bereik (gewicht) dat de asweger kan wegen, uitgedrukt in kilo.',
                                                owner=self)

    @property
    def afmetingAswegerZone(self) -> str:
        """De afmeting van de zone voor en na de weegplaat, inclusief de weegplaat zelf, als een waarde uit een vaste lijst van standaard afmetingen."""
        return self._afmetingAswegerZone.get_waarde()

    @afmetingAswegerZone.setter
    def afmetingAswegerZone(self, value):
        self._afmetingAswegerZone.set_waarde(value, owner=self)

    @property
    def kwaliteitscertificaat(self) -> DtcKwaliteitscertifcaatWaarden:
        """Het certificaat uitgereikt bij de eerste ijk nodig voor de rechtsgeldige uitbating van de aswegersite."""
        return self._kwaliteitscertificaat.get_waarde()

    @kwaliteitscertificaat.setter
    def kwaliteitscertificaat(self, value):
        self._kwaliteitscertificaat.set_waarde(value, owner=self)

    @property
    def typeMarkering(self) -> str:
        """Geeft welke wegmarkering er aanwezig zijn rond de aswegerzone als een waarde uit een vaste lijst van mogelijkheden."""
        return self._typeMarkering.get_waarde()

    @typeMarkering.setter
    def typeMarkering(self, value):
        self._typeMarkering.set_waarde(value, owner=self)

    @property
    def weegvermogenBereik(self) -> DtcBereikInKgWaarden:
        """Het bereik (gewicht) dat de asweger kan wegen, uitgedrukt in kilo."""
        return self._weegvermogenBereik.get_waarde()

    @weegvermogenBereik.setter
    def weegvermogenBereik(self, value):
        self._weegvermogenBereik.set_waarde(value, owner=self)
