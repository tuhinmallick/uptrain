from uptrain.core.classes.measurables import Measurable, FeatureMeasurable


class ConditionMeasurable(Measurable):
    def __init__(self, framework, underlying, condition) -> None:
        super().__init__(framework)
        self.underlying = underlying
        self.condition = condition
        self.feature = FeatureMeasurable(
            framework, underlying["feature_name"], underlying["dictn_type"]
        )
        if "formulae" in condition:
            formulae = condition["formulae"]
            if formulae in ["leq", "<="]:
                condition_func = lambda x: (x <= condition["threshold"])
            elif formulae in ["le", "<"]:
                condition_func = lambda x: (x < condition["threshold"])
            elif formulae in ["geq", ">="]:
                condition_func = lambda x: (x >= condition["threshold"])
            elif formulae in ["ge", ">"]:
                condition_func = lambda x: (x > condition["threshold"])
            elif formulae in ["eq", "=="]:
                condition_func = lambda x: (x == condition["threshold"])
            else:
                raise Exception(f"Condition Formulae {formulae} is not supported")
        elif "func" in condition:
            condition_func = condition["func"]
        else:
            raise Exception(
                "Either func or formulae should be defined to resolve condition"
            )
        self.condition_func = condition_func

    def _compute(self, inputs=None, outputs=None, gts=None, extra=None) -> any:
        return self.condition_func(
            self.feature._compute(inputs=inputs, outputs=outputs, gts=gts, extra=extra)
        )

    def col_name(self):
        return (
            "Condition("
            + self.feature.col_name()
            + ","
            + str(self.condition)
            + ")"
        )
