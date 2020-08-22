
from tests.util import BaseTest

class Test_TYCO113(BaseTest):
    def error_code(self) -> str:
        return "TYCO113"

    def activate_flag(self) -> str:
        return "--tyco_generic_alt"

    def test_pass_1(self):
        code = """
        import typing
        def foo(x: typing.ByteString):
            ...
        """
        result = self.run_flake8(code)
        assert result == []

    def test_fail_1(self):
        code = """
        import 
        def foo(x: .bytes):
            ...
        """
        result = self.run_flake8(code)
        self.assert_error_at(result, "TYCO113", 2, 12)


    def test_fail_2(self):
        code = """
        from  import bytes
        def foo(x) -> bytes:
            ...
        """
        result = self.run_flake8(code)
        self.assert_error_at(result, "TYCO113", 2, 15)
