import argparse
import json
import logging
from collections import defaultdict
from typing import DefaultDict, Optional

from youtube_selenium import YouTubeUploader

logging.basicConfig(level=logging.DEBUG)


def load_metadata(metadata_json_path: Optional[str] = None) -> DefaultDict[str, str]:
    if metadata_json_path is None:
        return defaultdict(str)
    with open(metadata_json_path) as metadata_json_file:
        return defaultdict(str, json.load(metadata_json_file))


def main(video_path: str, metadict: Optional[defaultdict] = None):
    uploader = YouTubeUploader(video_path, metadict)
    was_video_uploaded, video_id = uploader.upload()
    return was_video_uploaded


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", help="Path to the video file", required=True)
    parser.add_argument("--meta", help="Path to the JSON file with metadata")
    args = parser.parse_args()
    metadict = load_metadata(args.meta)
    main(args.video, metadict)
