# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

This is the prompt I used to generate tests for all the edge cases below:

> This game handles the use case when a user tries to submit a string as a guess, but that may not be enough. Consider whether any other kinds of user inputs (e.g., negative numbers, decimals or extremely large values) could still break this game.
>
> Implement ways to handle such inputs gracefully, then generate a suite of pytest tests in tests/test_game_logic.py to ensure the new logic for handling extraordinary inputs works as expected.

<table>
	<tr>
		<th>Edge Case</th>
		<th>Prompt Used</th>
		<th>AI-Suggested Test</th>
		<th>Did It Pass?</th>
		<th>Your Reasoning</th>
	</tr>
	<tr>
		<td>User input is a negative number</td>
		<td>Prompt above</td>
		<td>

```
def test_decimal_input_rejected():
	ok, _, err = parse_guess("3.7", low, high)
	assert ok == False
	assert err == "Please enter a whole number."
```

		</td>
		<td>Yes</td>
		<td>My reasoning</td>
	</tr>
</table>

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
