from youtube_transcript_api import YouTubeTranscriptApi


def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        if isinstance(transcript_list, list) and all(isinstance(item, dict) for item in transcript_list):
            transcript_text = ' '.join([transcript['text'] for transcript in transcript_list])
            return transcript_text
        else:
            return 'Unexpected response format'
    except Exception as e:
        return str(e)
        
print(get_video_transcript("n2t47V5Z56U"))