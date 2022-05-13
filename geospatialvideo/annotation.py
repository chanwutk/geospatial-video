import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame
    from geospatialvideo.instance import Instance

DATA_DIR = Path("./data/")

# COLUMNS_OF_INTEREST = [
#         'translation', 'size', 'rotation', 'heading', 'camera_heading',
#         'timestamp', 'filename', 'camera_translation', 'camera_rotation',
#         'camera_intrinsic', 'ego_rotation', 'ego_translation', 'filename',
#         'ego_heading', "category"
# ]


def _read_pickle(fpath):
    try:
        with open(fpath, "rb") as f:
            df = pickle.loads(f.read())
    except BaseException:
        raise FileExistsError(f"File not found at {fpath}.")

    return df


@dataclass
class Annotation:
    instance: Optional["Instance"]
    frame: Optional["Frame"]
    property: Dict[str, Any]

    @staticmethod
    def from_db(scene_id: str, frame_order: int) -> "Annotation":
        df_frames = _read_pickle(DATA_DIR / "df_frames.pickle")
        df_annotations = _read_pickle(DATA_DIR / "df_annotations.pickle")
        df_annotations = df_annotations.reset_index(drop=True)
        frames = df_frames[df_frames.scene_name == scene_id]
        frames = frames[frames.frame_order == frame_order]

        # Keep key frames only
        frames = frames[frames.is_key_frame]

        if frames.shape[0] <= 0:
            raise Exception("Invalid combination of arguments passed to `from_db`")

        # Some frames have more than one image due to multiple cameras
        # For now, we only return the first entry (front camera)
        frame_token = frames.token.values[0]
        assert isinstance(frame_token, str)

        if frames.shape[0] > 1:
            frames = frames.iloc[:1, :]

        annotations = df_annotations[df_annotations["token_sample_data"] == frame_token]
        frame_properties = frames.to_dict(orient="list")
        instance_properties = annotations.set_index("instance_token").to_dict(orient="index")
        properties = {}

        for token, prop in instance_properties.items():
            properties[token] = prop | frame_properties

        return Annotation(None, None, properties)
