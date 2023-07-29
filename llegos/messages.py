from typing import TYPE_CHECKING, Iterable, Literal

if TYPE_CHECKING:
    from llegos.ephemeral import EphemeralMessage

Intent = Literal[
    "ask",
    "be",
    "chat",
    "do",
    "error",
    "info",
    "inform",
    "log",
    "proxy",
    "query",
    "request",
    "response",
    "step",
    "system",
    "warn",
]


def message_chain(
    message: "EphemeralMessage", height: int = 12
) -> Iterable["EphemeralMessage"]:
    if message.reply and height > 0:
        yield from message_chain(message.reply, height - 1)
    yield message


def message_list(
    message: "EphemeralMessage", height: int = 12
) -> list["EphemeralMessage"]:
    return list(message_chain(message, height))
