import numpy as np
import os
from pynput.keyboard import Controller as KeyboardController, KeyCode

import tensorflow as tf
from tensorflow.keras import models

from helpers.preprocess import preprocess_audiobuffer
from helpers.recording import record_audio, terminate
from helpers.commands import speech_to_command

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0: all messages are logged (default), 1: INFO messages are not printed, 2: INFO and WARNING messages are not printed, 3: INFO, WARNING, and ERROR messages are not printed

MODEL_DIR = "saved_model"
MODEL_NAME = "LSTM_8words_4"
loaded_model = tf.saved_model.load(os.path.join(MODEL_DIR, MODEL_NAME))

def predict_mic():
    audio = record_audio()
    waveform = preprocess_audiobuffer(audio)[tf.newaxis, :]
    
    # Set the confidence threshold
    threshold = 0.6
    prediction = loaded_model(waveform)['predictions']
    confidence = tf.reduce_max(prediction).numpy()
    if confidence >= threshold:
        command = loaded_model(waveform)['class_names'].numpy()[0].decode('utf-8')
        return command, confidence
    else : return None, None

if __name__ == "__main__":
    # from turtle_helper import move_turtle
    print("===REAL-TIME SPEECH RECOGNITION==")
    print("Say ON to start the app")
    print()
    keyboard = KeyboardController()
    commands = ['down','go','left','off','on','right','stop','up']
    
    app_state = True
    speech_state = False
    while app_state:
        command, confidence = predict_mic()
        if (command == 'on') and (speech_state == False):
            speech_state = True
            print("The APP is ON")
            print("We Are hearing You right now!")
            print("===================================")
            print()
        if (command == 'off') and (speech_state == True):
            speech_state = False
            print("The APP is OFF")
            print("Say ON so we can hear your command!")  
            print("===================================")
            print()
        if speech_state:
            if command != None:
                speech_to_command(command, commands, keyboard)
                print("Predicted label:", command)
                print("Confidence:", confidence)
                print()
        else :
            if (command == "stop"):
                terminate()
                app_state = False
                    
    print("===================================")
    print("The APP has Stopped!")
    print("Thank you for using me!")
    print("===================================")
    exit()
        
                