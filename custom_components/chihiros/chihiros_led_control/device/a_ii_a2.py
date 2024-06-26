"""A II A2 device Model."""

from .base_device import BaseDevice


class AIIA2(BaseDevice):
    """Chihiros A II A 2 device Class."""

    _model_name = "A II A2"
    _model_code = "DYNA2"
    _colors: dict[str, int] = {
        # TODO validate that
        "white": 0,
    }
