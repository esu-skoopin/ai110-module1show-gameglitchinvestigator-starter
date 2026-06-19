from logic_utils import check_guess

# FIX: Fix the asserts for all of the tests below using the Claude Code CLI tool in "accepts edits" permission mode
def test_winning_guess():
    _, message = check_guess(50, 50)
    assert message == "🎉 Correct!"

def test_guess_too_high():
    _, message = check_guess(60, 50)
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    _, message = check_guess(40, 50)
    assert message == "📈 Go HIGHER!"
