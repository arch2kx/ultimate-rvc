"""Module which defines extra types for the frontend."""

from typing import Any, TypedDict

from collections.abc import Callable, Sequence
from enum import StrEnum

from typing_extra import AudioExt, F0Method

DropdownChoices = Sequence[str | int | float | tuple[str, str | int | float]] | None

DropdownValue = (
    str | int | float | Sequence[str | int | float] | Callable[..., Any] | None
)


class SourceType(StrEnum):
    """The type of source providing the song to generate a cover of."""

    PATH = "YouTube link/local path"
    LOCAL_FILE = "Local file"
    CACHED_SONG = "Cached song"


class ComponentVisibilityKwArgs(TypedDict):
    """
    Keyword arguments for setting component visibility.

    Attributes
    ----------
    visible : bool
        Whether the component should be visible.
    value : Any
        The value of the component.

    """

    visible: bool
    value: Any


class UpdateDropdownKwArgs(TypedDict, total=False):
    """
    Keyword arguments for updating a dropdown component.

    Attributes
    ----------
    choices : DropdownChoices
        The updated choices for the dropdown component.
    value : DropdownValue
        The updated value for the dropdown component.

    """

    choices: DropdownChoices
    value: DropdownValue


class TextBoxKwArgs(TypedDict, total=False):
    """
    Keyword arguments for updating a textbox component.

    Attributes
    ----------
    value : str | None
        The updated value for the textbox component.
    placeholder : str | None
        The updated placeholder for the textbox component.

    """

    value: str | None
    placeholder: str | None


class UpdateAudioKwArgs(TypedDict, total=False):
    """
    Keyword arguments for updating an audio component.

    Attributes
    ----------
    value : str | None
        The updated value for the audio component.

    """

    value: str | None


RunPipelineHarnessArgs = tuple[
    str,  # source
    str,  # model_name
    int,  # n_octaves
    int,  # n_semitones
    F0Method,  # f0_method
    float,  # index_rate
    int,  # filter_radius
    float,  # rms_mix_rate
    float,  # protect
    int,  # hop_length
    float,  # room_size
    float,  # wet_level
    float,  # dry_level
    float,  # damping
    int,  # main_gain
    int,  # inst_gain
    int,  # backup_gain
    int,  # output_sr
    AudioExt,  # output_format
    str,  # output_name
    bool,  # return_immediate
]
