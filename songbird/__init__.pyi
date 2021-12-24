from typing import Optional

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
    async def is_muted(self) -> None: ...
    async def play_source(self, source: Source) -> TrackHandle: ...
    async def play_only_source(self, source: Source) -> TrackHandle: ...
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
    loops: LoopState

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

class LoopState:
    loop_state: Optional[int]

async def create_player(source: Source) -> Track: ...

class Track:
    def play(self) -> None: ...
    def pause(self) -> None: ...
    def stop(self) -> None: ...
    @property
    def playing(self) -> PlayMode: ...
    @property
    def volume(self) -> None: ...
    def set_volume(self, volume: float) -> None: ...
    @property
    def position(self) -> float: ...
    @property
    def play_time(self) -> float: ...
    def set_loops(self, loops: LoopState) -> LoopState: ...
    def make_playable(self) -> None: ...
    @property
    def state(self) -> TrackState: ...
    def seek_time(self, position: float) -> float: ...
    @property
    def uuid(self) -> str: ...
