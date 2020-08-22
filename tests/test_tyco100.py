from tests.util import BaseTest


class Test_TYCO100(BaseTest):
    def error_code(self) -> str:
        return "TYCO100"

    def activate_flag(self) -> str:
        return "--tyco_generic_alt"

    def test_pass_1(self):
        code = """
        import typing
        def foo(x: typing.Iterable):
            ...
        """
        result = self.run_flake8(code)
        assert result == []

    def test_fail_1(self):
        code = """
        import collections.abc
        def foo(x: collections.abc.Iterable):
            ...
        """
        result = self.run_flake8(code)
        self.assert_error_at(result, "TYCO100", 2, 12)


    def test_fail_2(self):
        code = """
        from collections.abc import Iterable
        def foo(x) -> Iterable:
            ...
        """
        result = self.run_flake8(code)
        self.assert_error_at(result, "TYCO100", 2, 15)
