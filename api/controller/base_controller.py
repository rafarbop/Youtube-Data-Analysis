class BaseController:
    """Base for creating controllers.

    Properties:
        prefix: Prefix for API routes.
    Methods:
        __init__(prefix: str = ""): Class constructor.
        prefix: Property getter for prefix.
        prefix.setter: Property setter for prefix.
    """

    def __init__(self, prefix: str = ""):
        self._prefix = prefix

    @property
    def prefix(self):
        """Property getter for prefix.

        Returns:
            Prefix for API routes.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        """Property setter for prefix.

        Args:
            value: New value for the prefix.
        Raises:
            ValueError: If the prefix is invalid.
        """
        self._prefix = value
        print(f'Set property prefix: "{value}"')
