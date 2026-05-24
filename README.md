# Password Generator 🔐

A simple CLI tool that generates secure passwords with a balanced mix of uppercase letters, lowercase letters, digits, and punctuation.

---

## Features

- Generates a password of any length (minimum 6 characters)
- 60% letters (uppercase + lowercase)
- 40% digits and punctuation
- Shuffled randomly every time
- Input validation with helpful error messages

---

## Usage

Run the program:

```bash
python password_generator.py
```

Then enter the number of characters you want:

```
enter the number of characters: 12
Output: @4Kj!9Lm#2Qw
```

---

## Password Composition

| Character type | Percentage |
|---|---|
| Lowercase letters | 30% |
| Uppercase letters | 30% |
| Digits | 20% |
| Punctuation | 20% |

---

## Requirements

- Python 3.x
- No external libraries — uses built-in `random` and `string` modules only

---

## What I learned

- Python `string` module (`ascii_lowercase`, `ascii_uppercase`, `digits`, `punctuation`)
- `random.shuffle()` to randomize lists
- `try/except ValueError` for input validation
- List manipulation and `''.join()` to build strings

---

## Author

Built from scratch as a beginner Python project. soufian!
