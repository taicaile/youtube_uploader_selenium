class Constant:
    """A class for storing constants for YoutubeUploader class"""
    YOUTUBE_URL = 'https://www.youtube.com'
    YOUTUBE_STUDIO_URL = 'https://studio.youtube.com'
    YOUTUBE_UPLOAD_URL = 'https://www.youtube.com/upload'
    USER_WAITING_TIME = 1
    VIDEO_TITLE = 'title'
    VIDEO_DESCRIPTION = 'description'
    VIDEO_TAGS = 'tags'
    THUMBNAIL_PATH = 'thumbnail_path'

    TITLE = '//*[@id="textbox"][@aria-required="true"]'
    DESCRIPTION = '//*[@id="textbox"][@aria-required="false"]'

    TEXTBOX = 'textbox'
    TEXT_INPUT = 'text-input'
    RADIO_LABEL = 'radioLabel'
    STATUS_CONTAINER = '//span[contains(concat(" ",normalize-space(@class)," ")," ytcp-video-upload-progress ")]'
    NOT_MADE_FOR_KIDS_LABEL = 'NOT_MADE_FOR_KIDS'
    MORE_BUTTON = '//ytcp-button[contains(concat(" ",normalize-space(@class)," ")," ytcp-video-metadata-editor ")]'
    TAGS_INPUT_CONTAINER = '//input[@id="text-input"][@aria-label="Tags"]'
    TAGS_INPUT = 'text-input'
    NEXT_BUTTON = 'next-button'
    H1_DETAILS = '//h1[contains(concat(" ",normalize-space(@class)," ")," ytcp-uploads-dialog ")]'
    H1_CHECKS = '//h1[contains(concat(" ",normalize-space(@class)," ")," ytcp-uploads-checks ")]'
    H1_VIDEO_ELEMENTS = '//h1[contains(concat(" ",normalize-space(@class)," ")," ytcp-uploads-video-elements ")]'

    PUBLIC_BUTTON = 'PUBLIC'
    VIDEO_URL_CONTAINER = "//span[@class='video-url-fadeable style-scope ytcp-video-info']"
    VIDEO_URL_ELEMENT = "//a[@class='style-scope ytcp-video-info']"
    HREF = 'href'
    UPLOADED = 'Uploading'
    ERROR_CONTAINER = '//*[@id="error-message"]'
    VIDEO_NOT_FOUND_ERROR = 'Could not find video_id'
    DONE_BUTTON = 'done-button'
    INPUT_FILE_VIDEO = "//input[@type='file']"
    INPUT_FILE_THUMBNAIL = "//input[@id='file-loader']"
