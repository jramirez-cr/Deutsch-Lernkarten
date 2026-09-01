# Deutsch-Lernkarten

A CLI flashcard application for learning German A1 vocabulary, with weighted selection based on user-rated difficulty.

![Tests](https://github.com/jramirez-cr/Deutsch-Lernkarten/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.14-blue)

## About

Personal project to practice A1 German vocabulary from the console. Words are shown in random order, but weighted so that unseen words and words previously marked as hard appear more often than easy ones.

The project doubles as a hands-on exercise in Python architecture, relational schema design with SQLite, testing with pytest, and continuous integration with GitHub Actions.

Current state: working CLI with SQLite persistence. Web version is planned.

## Tech Stack

- Python 3.14
- SQLite for persistence
- pytest and pytest-cov for testing and coverage
- GitHub Actions for CI
- 

## Development Approach

This project is built with AI (Claude) as a conceptual tutor and code reviewer. No function is auto-generated. All code is written by hand, with the AI acting as:

- A source of explanations for concepts before I implement them.
- A sounding board for design decisions and their trade-offs.
- A reviewer that gives targeted feedback on code I've written.
- A debugging partner when things break.
- A rubber duck.


## Use

On start, the app displays a German word. The flow:

1. Press Enter to show translation, conjugations (if applicable), and example sentences.
2. Rate difficulty: `1` (I remember it), `2` (kind of), `3` (didn't remember).
3. Press Enter for the next word, or type `salir` to quit.

The selection algorithm adjusts how often each word reappears based on the difficulty you record.


## Roadmap

- [ ] Rewrite as web app with FastAPI + HTMX
- [ ] Spaced repetition scheduling (SM-2 style)
- [ ] Multi-user support with authentication
- [ ] Vocabulary import from user-supplied lists in other languages
- [ ] Full rewrite in Java as a separate project

## License

Personal project, no formal license. Free for educational use.
