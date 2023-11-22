from abc import ABC
from otlmow_model.BaseClasses.OTLField import OTLField


class ComplexField(OTLField, ABC):
    def __str__(self):
        return OTLField.__str__(self)

    waarde_shortcut_applicable = False
