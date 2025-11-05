class ExtendedMarkEvaluator(MarkEvaluator):
    def _getglobals(self):
        d = super()._getglobals()
        d.update(self.item._request._fixture_values)
        return d

    def _istrue(self):
        if self.holder:
            self.result = False
            args = self.holder.args
            kwargs = self.holder.kwargs
            for expr in args:
                import _pytest._code
                self.expr = expr
                d = self._getglobals()
                # Non cached eval to reload fixture values
                exprcode = _pytest._code.compile(expr, mode="eval")
                result = eval(exprcode, d)

                if result:
                    self.result = True
                    self.reason = expr
                    self.expr = expr
                    break
            return self.result
        return False
