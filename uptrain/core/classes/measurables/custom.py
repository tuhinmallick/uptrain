import numpy as np

from uptrain.core.classes.measurables import Measurable
from uptrain.core.classes.signals import SignalManager


class CustomMeasurable(Measurable):
    def __init__(self, framework, custom_args={}) -> None:
        super().__init__(framework)
        self._args = custom_args
        self.signal_manager = SignalManager()
        self.signal_manager.add_signal_formulae(self._args["signal_formulae"])

    def _compute(self, inputs=None, outputs=None, gts=None, extra=None) -> any:
        return self.signal_manager.evaluate_signal(
            inputs, outputs, gts=gts, extra_args=extra
        )

    def col_name(self):
        return str(self.signal_manager)

    # TODO: Decommission and find a generic way
    def extract_val_from_training_data(self, x):
        fake_inputs = {key: np.array([val]) for key, val in x.items()}
        return self.signal_manager.evaluate_signal(fake_inputs, None)
