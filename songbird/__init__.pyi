from __future__ import annotations

from typing import Optional, Tuple

class SongbirdError(Exception): ...
class UseAsyncConstructorError(SongbirdError): ...
class CouldNotConnectToRTPError(SongbirdError): ...
class CouldNotOpenFileError(SongbirdError): ...
class YtdlError(SongbirdError): ...
class FfmpegError(SongbirdError): ...


class Driver:
    @staticmethod
    async def create() -> Driver: ...
    async def connect(token: str, endpoint: str, session_id: str, guild_id: int, channel_id: int, user_id: int) -> None: ...
    async def leave(self) -> None: ...
    async def mute(self) -> None: ...
    async def unmute(self) -> None: ...
    async def is_muted(self) -> bool: ...
    async def play_source(self, source: Source) -> TrackHandle: ...
    async def play_only_source(self, source: Source) -> TrackHandle: ...
    async def play(self, source: Track) -> None: ...
    async def play_only(self, source: Track) -> None: ...
    async def set_bitrate(self, bitrate: int) -> None: ...
    async def set_bitrate_to_max(self) -> None: ...
    async def set_bitrate_to_auto(self) -> None: ...
    async def stop(self) -> None: ...
    async def set_config(self, config: Config) -> None: ...


class Source:
    @staticmethod
    def bytes(bytes: bytes, stereo: bool) -> Source: ...
    @staticmethod
    def ffmpeg(filename: str) -> Source: ...
    @staticmethod
    def ytdl(url: str) -> Source: ...
    @staticmethod
    def file(url: str) -> Source: ...

class CryptoMode:
    Normal: CryptoMode
    Suffix: CryptoMode
    Lite: CryptoMode


class Strategy:
    @staticmethod
    def every(duration: float) -> Strategy: ...
    @staticmethod
    def backoff_default() -> Strategy: ...
    @staticmethod
    def backoff(min: float, max: float, jitter: float) -> Strategy: ...


class DecodeMode:
    Pass: DecodeMode
    Decrypt: DecodeMode
    Decode: DecodeMode


class Config:
    def __init__(self) -> None: ...
    def set_crypto_mode(self, crypto_mode: CryptoMode): ...
    def set_decode_mode(self, decode_mode: DecodeMode): ...
    def set_preallocated_tracks(self, preallocated_tracks: int): ...
    def set_driver_timeout(self, driver_timeout: Optional[float]): ...
    def set_driver_retry(self, strategy: Strategy, retry_limit: Optional[int]): ...
    def set_gateway_timeout(self, gateway_timeout: Optional[float]): ...

class TrackHandle:
    def play(self) -> None: ...
    def pause(self) -> None: ...
    def stop(self) -> None: ...
    def set_volume(volume: float) -> None: ...
    def make_playable(self) -> None: ...
    @property
    def is_seekable(self) -> bool: ...
    def seek_time(self, position: float) -> float: ...
    async def get_info(self) -> TrackState: ...
    def enable_loop(self) -> None: ...
    def disable_loop(self) -> None: ...
    def loop_for(self, count: int) -> None: ...
    @property
    def uuid() -> str: ...
    @property
    def metadata() -> Metadata: ...

class TrackState:
    playing: PlayMode
    volume: float
    position: float
    play_time: float
    loops: LoopCount

class PlayMode:
    Play: PlayMode
    Pause: PlayMode
    Stop: PlayMode
    End: PlayMode

class Metadata:
    track: Optional[str]
    artist: Optional[str]
    date: Optional[str]
    channels: Optional[int]
    channel: Optional[str]
    start_time: Optional[float]
    duration: Optional[float]
    sample_rate: Optional[int]
    source_url: Optional[str]
    title: Optional[str]
    thumbnail: Optional[str]

class LoopCount:
    loop_state: Optional[int]

async def create_player(source: Source) -> Tuple[Track, TrackHandle]: ...

class Track:
    async def play(self) -> None: ...
    async def pause(self) -> None: ...
    async def stop(self) -> None: ...
    async def playing(self) -> PlayMode: ...
    async def volume(self) -> None: ...
    async def set_volume(self, volume: float) -> None: ...
    async def position(self) -> float: ...
    async def play_time(self) -> float: ...
    async def set_loop_count(self, loops: LoopCount) -> LoopCount: ...
    async def make_playable(self) -> None: ...
    async def state(self) -> TrackState: ...
    async def seek_time(self, position: float) -> float: ...
    async def uuid(self) -> str: ...
