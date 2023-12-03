from api.controller.base_controller import BaseController


class TestBaseController:
    """Class for testing BaseController."""

    def test_prefix_is_empty_by_default(self):
        """Testing if atribute 'prefix' is empty as default."""
        controller = BaseController()
        assert controller.prefix == ""

    def test_prefix_can_be_set(self):
        """Testing if atribute 'prefix' can be set."""
        controller = BaseController()
        controller.prefix = "my-prefix"
        assert controller.prefix == "my-prefix"
