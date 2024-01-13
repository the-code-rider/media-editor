import librosa
import json


class AudioAnalyser:

    def get_audio_features(self, audio_path):
        y, sr = librosa.load(audio_path, sr=None)

        # Extract beats
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

        # beat times
        beat_times = librosa.frames_to_time(beats, sr=sr)

        # Extract harmonic elements
        harmonic, _ = librosa.effects.hpss(y)

        # Save the extracted features
        audio_features = {
            "tempo": tempo,
            # "beats": beats.tolist(),  # Convert numpy array to list for JSON serialization
            "harmonics": harmonic.tolist(),
            "sampleRate": sr,
            "beatTimes": beat_times.tolist()
        }

        return audio_features

    def export_to_json(self, audio_features, outputfile):
        with open('audio_features.json', 'w') as f:
            json.dump(audio_features, f)
