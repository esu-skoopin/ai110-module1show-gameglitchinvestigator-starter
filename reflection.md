# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The hints are backwards (tells you to guess higher when you should guess lower and vice versa)
- You start out with one less guess than you're supposed to (i.e., for any playing difficulty, it shows that you've already used an attempt in the developer debug section of the page for fresh instances of the app)
- You're unable to start a new game using the "New Game" button at the bottom of the page once you complete a game
- The score and history for a game don't reset when you start a new game, according to the developer debug section of the page
- You can change the playing difficulty for the game you're currently playing mid-game just by changing the difficulty dropdown in the left panel of the page. This can result in you having zero or negative attempts for playing modes that have less allowed attempts than the one you were originally playing in (i.e., if you switched over to hard mode after you had already started the game in normal mode and used up 6 guesses, the app would show you that you have -1 attempts left).
- The secret number is not confined by the valid guessing ranges shown in the left panel of the page for the easy and hard playing difficulties
	- The valid guessing range for easy mode in the left panel: 1 to 20
	- The valid guessing range for hard mode in the left panel: 1 to 50
	- The secret number has been observed to fall outside of the ranges above while playing on easy or hard mode
- The blue banner at the top of the page also does not update to reflect the ranges shown above when playing on easy or hard mode
- The app lets you guess outside of the valid guessing range (e.g., you can guess outside of the valid guessing range of 1 <= n <= 100 for the normal playing difficulty)
- If you guess a number higher than the secret number when you have an even number of attempts left, your score goes up by 5 points, instead of down by 5 points

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess: 30, secret: 87 | Hint: "Go HIGHER!" | Hint: "Go LOWER!" | None |
| Guess: 115, range: 1 - 100 | Invalid guess | Valid guess | None |
| Start a new instance of the app | Attempts used: 0 | Attempts used: 1 | None |
| Click "New Game" button on win or lose | App starts new game | App changes banner at the bottom of the screen once, but doesn't start new game | None |
| Click "New Game" button before win or lose | Score and guess history reset | Score and guess history don't reset | None |
| Guess: 50, secret: 34, attempts left: 6 | Score -= 5 | Score += 5 | None |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

The only AI tool I used to work on this project was the Claude CLI tool.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

An example of a suggestion that Claude gave that was correct was the one that it gave for fixing the backwards hints bug. It correctly identified that the code was returning the right result in the first part of the tuple (i.e., "Too High" or "Too Low"), but was returning the wrong hint message in the second part of the tuple (i.e., "📈 Go HIGHER!" or "📉 Go LOWER!") and applied the correct fix to fix that issue. I verified that the fix Claude applied was correct by visually confirming in the UI that the hints were correct when I guessed higher/lower than the secret number.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Claude didn't really suggest anything incorrect, to my knowledge, while I was working on this project, but I did ask it to tweak one of its fixes in the `test_game_logic.py`. It initially changed the assert for each test case to use `in` instead of `==` which I personally didn't see a whole lot of point in doing (doesn't matter too much for use cases like this that only involve relatively short strings, but `in` is slower than `==`), so I asked it to change it back to using `==`.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided whether the bugs I decided to tackle were really fixed by first looking at the diff to see if the changes that were made made sense to me and then by verifying that the fix works in the UI for the application.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

Running the preexisting tests in `test_game_logic.py` revealed that some issues existed in the provided tests, as well. Each of the three preexisting tests that test `check_guess()` failed even though the fix for the backwards hints bug had already been enacted and verified at that point. Upon closer inspection, it was revealed that the reason why the tests were failing was because `check_guess()` returns a tuple and each of those tests was trying to assert that tuple return value from `check_guess()` against a string.

- Did AI help you design or understand any tests? How?

Yes, like I outlined above, working with AI did help me understand the preexisting tests in `test_game_logic.py` better. Not only did Claude bring the type mismatch in the asserts for each of the tests to my attention, but it also incidentally taught me the syntax for multi-variable assignment in Python (i.e., `var_name, _ = function_that_returns_a_tuple()`) which I was not familiar with prior to working on this project.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
