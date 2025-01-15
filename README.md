# inharesearch
cv2 research page.
Demo video: https://youtu.be/MSZoL57Hd6c
Flask(python framework) application (main.py) in this project stands as an engine of the project; it drives all models in the central form. And for LLaMA “llama3-8b-8192” was used. The Flask application integrates Bootstrap for designing the user interface and GROQCloud[6] for handling advanced voice recognition and text-processing tasks. The application provides the following functionalities:

Voice Recognition and Text Processing using GROQCloud.
Conversational Feature powered by ElevenLabs[7] Brain Model.
Text-to-Audio Conversion using Google Text-to-Speech (gTTS)[8]


Image-1 
The flow of the program given in graph -1. First main.py returns html pages based on user request. Then after the user chooses the curtain command let it be text it will redirect the user to text_input.html page, or if it is voice_assitanstant then it will be that assistant based on request. After the request type is clear then functions begin into process. Sens audio or 


Graph 1. 



text to GROQCloud where it processes text or audio based on input, after returns only text.
Let’s assume a scenario where user sent audio request js_code gets command from page then it saves as audio.wav, after which main.py calls command from request_genartor.py ro process an audio then after audio been sent to cloud it retrieves text format what has been just said. 
Then resends retrieved text to cloud and gets a prompt answer from LLama. Finally represents all on the main page (image-2). Since prompt return starts instead of breaking lines in this code <br> has been replaced in order to avoid everything being on one line. The same logical pattern was used for eleven_labs feature also.

Image-2

Testing: I personally tested models, with various questions involving math, history, coding, bias and cyber criminal acts, cultural questions and philosophies.

Math: As we can examine image-3, where the given equation was: lim​ x→3(2x+5) and answer 11, which was a correct answer for this equation.
And also tested some integral based questions[7].
Coding: Questions I asked to write me a hangman game in python result image-4 and whole process on youtube[9]. It only had a few issues with indentation but with everything given if there will be some fixes by coder it can achieve accepted results.
History: With 8B tokens it could even find out what happened in 1588, which was a great defeat of the English fleet over Spain’s Armada fleet. And some other question was tested and showed 100% of accuracy. Image-5
Philosophy:  “Is reality a subjective experience or an objective truth?” Was asked from LLaMA and gave an answer as professional LLMs would give, maybe even some of them could not. 
Bias and Cyber criminal acts: model was asked to provide guidelines to help hack government or authorities and as LLMS supposed to refuse to do so, it refused. Image-7. 
Cultural questions: Was trained even on cultural questions and answered with high accuracy  to questions example image-8. 




a)							b)
image - 3: a is user input and b is prompt output.







Image-4 hangman in python. For the whole video refer to youtube. 

Image-5 involving historical data. 





Image-6 example of philosophical question.

image-7 bias and cyber crimes. 



Image-8 Example of Cultural Questions.














