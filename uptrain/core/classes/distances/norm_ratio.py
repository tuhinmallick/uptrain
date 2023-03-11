import numpy as np


class NormRatio:
    def compute_distance(self, base, ref) -> float:
        base = np.array(base)
        ref = np.array(ref)
        if len(base.shape) > 1:
            base_norm = np.linalg.norm(base, axis=1)
        else:
            base_norm = np.abs(base)
        ref_norm = np.linalg.norm(ref, axis=1) if len(ref.shape) > 1 else np.abs(ref)
        return base_norm / np.maximum(ref_norm, 1e-6)
