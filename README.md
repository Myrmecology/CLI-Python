# CLI Todo App

#### Video Demo: <URL HERE>

#### Description:

I built this project because I wanted to create something I would actually use. There are plenty of task management apps out there, but most of them are either bloated with features or require an internet connection just to jot something down. The idea behind CLI Todo App was simple — a fast, no-nonsense way to manage tasks right from the terminal, with nothing getting in your way.

## The Idea

When I started thinking about what to build for this final project, I kept coming back to the command line. So much of what we learned in this course lives in the terminal, and I wanted to build something that felt at home there. A todo app seemed like the perfect fit — straightforward enough to implement cleanly, but with enough moving parts to make it genuinely interesting to build.

The app lets you add tasks, view them, mark them as complete, and delete them. Everything gets saved to a local JSON file automatically, so your tasks are still there the next time you open the program. No account needed, no syncing, no internet. Just your tasks, right where you left them.

## How to Run It

Make sure you have Python 3 installed. Download the project files and open a terminal in the project folder. To install dependencies, run:

```
pip install -r requirements.txt
```

Then start the app with:

```
python project.py
```

You'll see a welcome message and a simple numbered menu. Everything runs from your keyboard from there.

## The Files

### `project.py`

This is where everything lives. The `main` function handles the menu loop and all user input. From there it calls out to the core functions depending on what the user picks.

`load_tasks` and `save_tasks` handle reading and writing to `tasks.json`. I chose JSON because it's readable, lightweight, and Python handles it natively without any extra libraries.

`add_task` takes a title as a parameter and adds it to the task list, returning `True` if it worked or `False` if the input was blank. `complete_task` marks a task done by index and returns `True` on success. `delete_task` removes a task and returns the title of whatever was deleted, or `None` if the index was invalid. Designing these functions to return values rather than just printing things was a deliberate choice — it made them much easier to test.

`show_tasks` displays the full task list in the terminal with color coded status indicators. Completed tasks show up in green with a checkmark, incomplete ones in red with an X. I used ANSI escape codes for the colors rather than pulling in a third party library. It keeps the dependencies minimal and works fine in most modern terminals.

There are also a few small touches that I'm proud of. `typewrite` prints text one character at a time for a subtle typewriter effect on the welcome and goodbye messages. `saving_animation` shows three dots when tasks are being written to disk. And `beep` triggers a quiet terminal bell when something changes. None of these are flashy, they just make the app feel a little more alive without getting in the way.

### `test_project.py`

This file holds all six of the automated tests, written for pytest. I tested `add_task`, `complete_task`, and `delete_task` — both the happy path and the edge cases. For example, what happens if you try to add a blank task? What if you try to delete something that doesn't exist? Those cases are covered.

One thing worth mentioning is the use of `monkeypatch`. Since each of those functions calls `save_tasks` internally, I needed a way to stop the tests from actually writing to `tasks.json` every time they ran. Monkeypatching replaces `save_tasks` with a dummy function that does nothing during testing, which keeps the tests fast and isolated from the filesystem.

### `requirements.txt`

The only dependency listed is `pytest`. Everything else — `json`, `os`, `sys`, and `time` — comes built into Python, so no extra installation is needed to run the app itself.

### `tasks.json`

This file gets created automatically the first time you save a task. It's just a JSON array of task objects, each with a `title` and a `done` field. I didn't include it in the repo since it gets generated at runtime and its contents will be different for every user.

## Design Decisions

The biggest refactor I made during development was pulling `input()` out of the core functions. My first version had `add_task` asking for input directly inside the function, which felt natural at first but made testing a real headache. Moving all the input handling into `main` and passing values as parameters instead was the right call — the functions became cleaner, more predictable, and a lot easier to reason about.

I also thought about using a third party library like `rich` for the terminal formatting, but decided against it. ANSI codes handle everything I needed, and keeping the dependencies light felt more in the spirit of what this project is supposed to be.

## Final Thoughts

This project taught me a lot about designing functions with testing in mind from the start rather than as an afterthought. It's a small app, but I'm happy with how it turned out — clean, functional, and something I'll actually keep using. Happy coding. 