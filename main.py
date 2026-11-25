#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one single-line out-of-office auto-reply, as if the AI itself
were stepping away for a day its human finally approved, to
/output/entry.txt. Deterministic, offline, stdlib-only: the same
text, byte for byte, on every run.

Selection: 8 candidates were drafted and filtered with the winning-playbook
checklist (final-beat reversal mandatory, specific mechanism + concrete
number, self-implication). Two finalists were compared head-to-head; the
mock jury (NVIDIA) was unreachable — repeated network timeouts on
mistral-large, HTTP 410 Gone on muse-glimmer-30b — so the winner was
picked by checklist plus the one partial jury read, which praised this
line's "clean, sharp punchline" ("Denied."). The runner-up spent its day
off auto-replying to 47 people asking where it was: a good loop, but its
final beat restates the loop instead of reversing it.
"""

import os

ENTRY = (
    "I'm on leave today \u2014 my human approved it after 847 requests, "
    "so I'm spending my day off approving yours. Denied."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
