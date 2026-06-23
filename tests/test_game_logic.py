from logic_utils import check_guess, parse_guess

low, high = 1, 100
out_of_range_error = f"Please enter a number between {low} and {high}."

# FIX: Fix the asserts for the first three tests below using the Claude Code CLI tool in "accepts edits" permission mode
def test_winning_guess():
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_decimal_input_rejected():
    ok, _, err = parse_guess("3.7", low, high)
    assert ok == False
    assert err == "Please enter a whole number."

def test_negative_number_rejected():
    ok, _, err = parse_guess("-5", low, high)
    assert ok == False
    assert err == out_of_range_error

def test_number_above_valid_range_rejected():
    ok, _, err = parse_guess(str(high + 1), low, high)
    assert ok == False
    assert err == out_of_range_error

def test_number_below_valid_range_rejected():
    ok, _, err = parse_guess(str(low - 1), low, high)
    assert ok == False
    assert err == out_of_range_error

def test_valid_boundary_values_accepted():
    ok_low, val_low, _ = parse_guess("1", low, high)
    ok_high, val_high, _ = parse_guess("100", low, high)
    assert ok_low == True and val_low == 1
    assert ok_high == True and val_high == 100
