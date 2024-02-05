#!/usr/bin/python3

"""bae geometry"""


class MyInt(int):
    """
    MyInt class inherits from int and has inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Parameters:
            other (int): The other value to compare.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Parameters:
            other (int): The other value to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
