from unittest.mock import MagicMock


class ProductionClass:
    def method (self):
        pass


thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')

thing.method.assert_called_with(3, 4, 5, key='value')