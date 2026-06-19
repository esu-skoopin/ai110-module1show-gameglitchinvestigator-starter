from logic_utils import check_guess

# FIX: Fix the asserts for all of the tests below using the Claude Code CLI tool in "accepts edits" permission mode
def test_winning_guess():
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    result, _ = check_guess(40, 50)
    assert result == "Too Low"
