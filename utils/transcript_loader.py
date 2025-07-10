# ========================
# Indexing - YouTube Transcript Ingestion
# ========================

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, RequestBlocked
import re
from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str) -> str:
    """Extracts the YouTube video ID from a standard or shortened URL."""
    parsed_url = urlparse(url)

    if 'youtube.com' in parsed_url.netloc:
        query_params = parse_qs(parsed_url.query)
        return query_params.get('v', [None])[0]
    elif 'youtu.be' in parsed_url.netloc:
        return parsed_url.path.lstrip('/')
    else:
        raise ValueError("Invalid YouTube URL")

def load_transcript(video_url):
    """Loads transcript for a given YouTube video URL."""
    try:
        video_id = extract_video_id(video_url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        transcript = " ".join(chunk['text'] for chunk in transcript_list)
        transcript = re.sub(r'\[.*?\]', '', transcript)  
        transcript = re.sub(r'\b(uh+|umm+|ah+|er+)\b', '', transcript, flags=re.IGNORECASE)
        transcript = re.sub(r'\([^)]*\)', '', transcript) 
        transcript = re.sub(r'\b(thank you|welcome back|hey guys|subscribe)\b', '', transcript, flags=re.I)
        transcript = re.sub(r'\s+', ' ', transcript).strip() 

        return transcript
        
    except (TranscriptsDisabled, NoTranscriptFound, RequestBlocked):
        return ''