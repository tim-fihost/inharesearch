from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from request_generator import process_audio, process_text
from text_to_audio import text_to_audio
from elevenlabs_feature import produce_audio
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'audios'
ALLOWED_EXTENSIONS = {'wav', 'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Utility: Check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ===========================================================================

# Routes
@app.route("/")
def home():
    """Render the homepage."""
    return render_template("index.html")


@app.route("/main")
def main():
    """Render the main page."""
    return render_template('main.html')


@app.route("/text-input", methods=["GET", "POST"])
def text_input():
    """Handle text input and process it."""
    result = None
    if request.method == "POST":
        user_input = request.form.get("user_input")  # Retrieve user input
        result = process_text(user_input)  # Process the input
        result = result.replace('\n', '<br>')
    return render_template("text_input.html", result=result)

@app.route('/voice-assistant', methods=['GET', 'POST'])
def voice_assistant():
    if request.method == 'GET':
        # Render the page with the voice assistant interface
        return render_template('voice_assistant.html')
    
    elif request.method == 'POST':
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file part'})

        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'No selected file'})

        if audio_file and allowed_file(audio_file.filename):
            # Save the uploaded audio file
            filename = secure_filename(audio_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            audio_file.save(filepath)
            
            # Process the audio file and generate a response
            text_output = process_audio()
            answer = process_text(text_output)
            answer = answer.replace('**', '\t') 
            text_to_audio(answer)  # Generates audio file (e.g., audios/audio.mp3)
            answer = answer.replace('\n', '<br>') 
            return jsonify({
                'response_text': answer,
                'audio_url': '/audios/audio.mp3'
            })

@app.route('/voice-assistant-elevenlabs', methods=['GET', 'POST'])
def voice_assistant_elevenlabs():
    if request.method == 'GET':
        # Render the page with the voice assistant interface
        return render_template('voice_assistant_elevenlabs.html')
    
    elif request.method == 'POST':
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file part'})

        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'No selected file'})

        if audio_file and allowed_file(audio_file.filename):
            # Save the uploaded audio file
            filename = secure_filename(audio_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            audio_file.save(filepath)
            
            # Process the audio file and generate a response
            text_output = process_audio()
            answer = process_text(text_output)
            answer = answer.replace('**', '\t') 
            produce_audio(answer)  # Generates audio file (e.g., audios/audio.mp3)
            answer = answer.replace('\n', '<br>') 
            return jsonify({
                'response_text': answer,
                'audio_url': '/audios/audio.mp3'
            })


@app.route('/audios/<filename>')
def serve_audio(filename):
    """Serve audio files from the server."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
