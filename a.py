from faster_whisper import WhisperModel
model_size="large-v3"
model= WhisperModel(model_size,device="cpu",compute_type="default")

def transcribe_file(filepath):
  segments,info= model.transcribe(filepath,language="en")
  transcription_text=""
  for segment in segments:
    transcription_text+=segment.text+"\n"
  return transcription_text 

filepath="0401-[AudioTrimmer.com] (1).mp3"
result=transcribe_file(filepath)
print(result)   