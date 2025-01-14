"""Module which defines extra types for the backend."""

from collections.abc import Callable
from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from typing_extra import F0Method

# Voice model management


class ModelTagName(StrEnum):
    """Names of valid voice model tags."""

    ENGLISH = "English"
    JAPANESE = "Japanese"
    OTHER_LANGUAGE = "Other Language"
    ANIME = "Anime"
    VTUBER = "Vtuber"
    REAL_PERSON = "Real person"
    GAME_CHARACTER = "Game character"


class ModelTagMetaData(BaseModel):
    """
    Metadata for a voice model tag.

    Attributes
    ----------
    name : ModelTagName
        The name of the tag.
    description : str
        The description of the tag.

    """

    name: ModelTagName
    description: str


class ModelMetaData(BaseModel):
    """
    Metadata for a voice model.

    Attributes
    ----------
    name : str
        The name of the voice model.
    description : str
        A description of the voice model.
    tags : list[ModelTagName]
        The tags associated with the voice model.
    credit : str
        Who created the voice model.
    added : str
        The date the voice model was created.
    url : str
        An URL pointing to a location where the voice model can be
        downloaded.

    """

    name: str
    description: str
    tags: list[ModelTagName]
    credit: str
    added: str
    url: str


class ModelMetaDataTable(BaseModel):
    """
    Table with metadata for a set of voice models.

    Attributes
    ----------
    tags : list[ModelTagMetaData]
        Metadata for the tags associated with the given set of voice
        models.
    models : list[ModelMetaData]
        Metadata for the given set of voice models.

    """

    tags: list[ModelTagMetaData]
    models: list[ModelMetaData]


ModelMetaDataPredicate = Callable[[ModelMetaData], bool]

ModelMetaDataList = list[list[str | list[ModelTagName]]]


# Song cover generation


class SourceType(StrEnum):
    """The type of source providing the song to generate a cover of."""

    URL = "url"
    FILE = "file"
    SONG_DIR = "song_dir"


class AudioExtInternal(StrEnum):
    """Audio file formats for internal use."""

    MP3 = "mp3"
    WAV = "wav"
    FLAC = "flac"
    OGG = "ogg"
    IPOD = "ipod"
    ADTS = "adts"


class FileMetaData(BaseModel):
    """
    Metadata for a file.

    Attributes
    ----------
    name : str
        The name of the file.
    hash_id : str
        The hash ID of the file.

    """

    name: str
    hash_id: str


class ConvertedVocalsMetaData(BaseModel):
    """
    Metadata for an RVC converted vocals track.

    Attributes
    ----------
    vocals_track : FileMetaData
        Metadata for the vocals track that was converted.
    model_name : str
        The name of the model used for vocal conversion.
    n_semitones : int
        The number of semitones the converted vocals were pitch-shifted
        by.
    f0_method : F0Method
        The method used for pitch detection.
    index_rate : float
        The influence of the index file on the vocal conversion.
    filter_radius : int
        The filter radius used for the vocal conversion.
    rms_mix_rate : float
        The blending of the volume envelope of the converted vocals.
    protect : float
        The protection rate used for consonants and breathing sounds.
    hop_length : int
        The hop length used for crepe-based pitch detection.

    """

    vocals_track: FileMetaData
    model_name: str
    n_semitones: int
    f0_method: F0Method
    index_rate: float
    filter_radius: int
    rms_mix_rate: float
    protect: float
    hop_length: int
    model_config = ConfigDict(protected_namespaces=())


class EffectedVocalsMetaData(BaseModel):
    """
    Metadata for an effected vocals track.

    Attributes
    ----------
    vocals_track : FileMetaData
        Metadata for the vocals track that effects were applied to.
    room_size : float
        The room size of the reverb effect applied to the vocals track.
    wet_level : float
        The wetness level of the reverb effect applied to the vocals
        track.
    dry_level : float
        The dryness level of the reverb effect. applied to the vocals
        track.
    damping : float
        The damping of the reverb effect applied to the vocals track.

    """

    vocals_track: FileMetaData
    room_size: float
    wet_level: float
    dry_level: float
    damping: float
