"""Test cases for hello module."""

from yt_investing_kb.hello import main
import pytest


@pytest.mark.parametrize(
    "expected",
    [
        "Hello from yt-investing-kb!\n",  # The expected correct output from main()
        pytest.param(
            "Wrong output", marks=pytest.mark.xfail
        ),  # A test case we expect to fail
    ],
)
def test_dump(capsys, expected):
    """Test the main() function's output against expected values.

    This test uses pytest's parametrize to run multiple test cases:
    1. Tests that main() outputs the expected greeting
    2. Includes a deliberately failing test marked with xfail

    Args:
        capsys: pytest fixture to capture stdout/stderr
        expected: parametrized input containing the expected output string
    """
    main()  # Call the main function
    captured = capsys.readouterr()  # Capture what was printed to stdout
    assert captured.out == expected  # Verify the output matches expected
