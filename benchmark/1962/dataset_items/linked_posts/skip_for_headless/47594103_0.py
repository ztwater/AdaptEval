from _pytest.skipping import MarkEvaluator

class ExtendedMarkEvaluator(MarkEvaluator):
    def _getglobals(self):
        d = super()._getglobals()
        d.update(self.item._request._fixture_values)
        return d
