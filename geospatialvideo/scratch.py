import pickle

with open("data/df_frames.pickle", "rb") as f:
    df_frames = pickle.loads(f.read())
with open("data/df_annotations.pickle", "rb") as f:
    df_annotations = pickle.loads(f.read())


tmp = df_frames[df_frames.scene_name == "scene-0061"]
tmp1 = tmp[tmp.frame_order == 1]


scene_name = "scene-0061"
frames = df_frames[df_frames.scene_name == scene_name]


s = set(frames.token).intersection(set(df_annotations.token_sample_data))
len(s)

tmp = df_frames[df_frames.is_key_frame]
tmp = tmp[tmp.scene_name == "scene-0061"]
joined = frames.set_index("token").join(df_annotations.set_index("token_sample_data"), rsuffix="_")
joined_ = joined[joined.is_key_frame]


search = {}
for i in range(20):
    newtmp = tmp[tmp.frame_order == i]
    search[i] = newtmp


framesv2 = df_frames.drop(["camera_heading"], axis=1)
framesv2 = framesv2.rename(columns={"token": "camera_token"})

annotationsv2 = df_annotations.rename(
    {"token": "annotation_token", "token_sample_data": "frame_token"}
)

annotationsv2 = annotationsv2.to_pickle(
    "/Users/amylu/GitHub/geospatial-video/data/df_annotations.pickle"
)
framesv2 = framesv2.to_pickle("/Users/amylu/GitHub/geospatial-video/data/df_frames.pickle")

df_frames = framesv2
df_annotations = annotationsv2
