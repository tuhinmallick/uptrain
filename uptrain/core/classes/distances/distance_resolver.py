from uptrain.core.classes.distances import (
    CosineDistance,
    L2Distance,
    NormRatio,
)


class DistanceResolver:
    def __init__(self) -> None:
        pass

    def resolve(self, distance_type):
        if distance_type == "cosine_distance":
            return CosineDistance()
        elif distance_type == "l2_distance":
            return L2Distance()
        elif distance_type == "norm_ratio":
            return NormRatio()
        else:
            raise Exception(f"distance_type {distance_type} is not defined")
