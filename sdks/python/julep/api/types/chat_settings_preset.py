# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChatSettingsPreset(str, enum.Enum):
    """
    Generation preset name (problem_solving|conversational|fun|prose|creative|business|deterministic|code|multilingual)
    """

    PROBLEM_SOLVING = "problem_solving"
    CONVERSATIONAL = "conversational"
    FUN = "fun"
    PROSE = "prose"
    CREATIVE = "creative"
    BUSINESS = "business"
    DETERMINISTIC = "deterministic"
    CODE = "code"
    MULTILINGUAL = "multilingual"

    def visit(
        self,
        problem_solving: typing.Callable[[], T_Result],
        conversational: typing.Callable[[], T_Result],
        fun: typing.Callable[[], T_Result],
        prose: typing.Callable[[], T_Result],
        creative: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        deterministic: typing.Callable[[], T_Result],
        code: typing.Callable[[], T_Result],
        multilingual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatSettingsPreset.PROBLEM_SOLVING:
            return problem_solving()
        if self is ChatSettingsPreset.CONVERSATIONAL:
            return conversational()
        if self is ChatSettingsPreset.FUN:
            return fun()
        if self is ChatSettingsPreset.PROSE:
            return prose()
        if self is ChatSettingsPreset.CREATIVE:
            return creative()
        if self is ChatSettingsPreset.BUSINESS:
            return business()
        if self is ChatSettingsPreset.DETERMINISTIC:
            return deterministic()
        if self is ChatSettingsPreset.CODE:
            return code()
        if self is ChatSettingsPreset.MULTILINGUAL:
            return multilingual()