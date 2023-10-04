from abc import abstractmethod

from otlmow_model.BaseClasses.OTLObject import OTLObject


class OTLAsset(OTLObject):
    @abstractmethod
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
