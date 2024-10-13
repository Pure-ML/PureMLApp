import reflex as rx
from typing import Literal, Callable



LiteralButtonVariant = Literal[
    "primary", "success", "destructive", "secondary", "muted"
]

default_class_name = "font-smbold rounded-xl cursor-pointer inline-flex items-center justify-center px-[0.875rem] py-2 relative transition-bg border-t border-[rgba(255,255,255,0.21)]"

after_class_name = "after:absolute after:inset-[1px] after:border-t after:rounded-[11px] after:border-white after:opacity-[0.22]"


def get_variant_class(variant: str) -> str:
    return (
        f"bg-gradient-to-b from-[--{variant}-9] to-[--{variant}-9] hover:to-[--{variant}-10] text-white"
        + " "
    )


variant_styles = {

    # "primary": {
    #     "class_name": get_variant_class("violet"),
    # },

    "primary": {
        "class_name": get_variant_class("indigo"),
    },

    "success": {
        "class_name": get_variant_class("green"),
    },
    "destructive": {
        "class_name": get_variant_class("red"),
    },
    "muted": {
        "class_name": "bg-slate-3 hover:bg-slate-5 text-slate-9 border-t !border-slate-5",
    },
    "secondary": {
        "class_name": "bg-slate-4 hover:bg-slate-5 text-slate-10 !border-none",
    },
}
