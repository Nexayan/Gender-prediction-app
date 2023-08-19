import os
import numpy as np
import tensorflow as tf
from colorama import init, Fore, Style

# Initialize colorama
init()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

LOGO = r'''
   _____                _                                _ _      _   _                    __   ___  
  / ____|              | |                              | (_)    | | (_)                  /_ | / _ \ 
 | |  __  ___ _ __   __| | ___ _ __   _ __  _ __ ___  __| |_  ___| |_ _  ___  _ __   __   _| || | | |
 | | |_ |/ _ \ '_ \ / _` |/ _ \ '__| | '_ \| '__/ _ \/ _` | |/ __| __| |/ _ \| '_ \  \ \ / / || | | |
 | |__| |  __/ | | | (_| |  __/ |    | |_) | | |  __/ (_| | | (__| |_| | (_) | | | |  \ V /| || |_| |
  \_____|\___|_| |_|\__,_|\___|_|    | .__/|_|  \___|\__,_|_|\___|\__|_|\___/|_| |_|   \_/ |_(_)___/ 
                                     | |                                                             
                                     |_| By Nexayan                                                                                                                         
'''
print(LOGO)

class GenderPredictor:
    def __init__(self):
        self.load_model()

    def load_model(self):
        self.model = tf.keras.models.load_model('gender_detection_model.h5')
        self.char_to_num = {char: idx for idx, char in enumerate(' abcdefghijklmnopqrstuvwxyz')}
        self.max_name_length = 50

    def preprocess_names(self, names):
        processed_names = []
        for name in names:
            encoded_name = [self.char_to_num.get(char, 0) for char in name.lower()]
            padded_name = encoded_name + [0] * (self.max_name_length - len(encoded_name))
            processed_names.append(padded_name)
        return np.array(processed_names)
    
    def predict(self, names):
        name_encoded = self.preprocess_names(names)
        predicted_probabilities = self.model.predict(name_encoded, verbose=0)
        predicted_genders = ['Male' if prob >= 0.5 else 'Female' for prob in predicted_probabilities]
        return predicted_genders

if __name__ == "__main__":
    predictor = GenderPredictor()

    while True:
        mode = input("Select mode (single/multiple/import/exit)> ").strip().lower()

        if mode == "exit":
            break

        if mode == "single":
            name = input("Enter a name> ").strip()
            if name:
                predicted_gender = predictor.predict([name])
                colored_name = f"{Fore.GREEN}{name}{Style.RESET_ALL}"
                print(f"Predicted gender for '{colored_name}': {predicted_gender[0]}")
            else:
                print("Please enter a name.")

        elif mode == "multiple":
            names = []
            while True:
                name = input("Enter a name (or 'done' to finish)> ").strip()
                if name == "done":
                    break
                names.append(name)
            if names:
                predicted_genders = predictor.predict(names)
                print("\nPredicted genders:")
                for name, gender in zip(names, predicted_genders):
                    colored_name = f"{Fore.GREEN}{name.strip()}{Style.RESET_ALL}"
                    print(f"{colored_name}: {gender}")
            else:
                print("No names provided.")

        elif mode == "import":
            file_path = input("Enter the path of the text file: ").strip()
            try:
                with open(file_path, 'r') as file:
                    names = [line.strip() for line in file.readlines()]
                    if names:
                        predicted_genders = predictor.predict(names)
                        print("\nPredicted genders from imported file:")
                        for name, gender in zip(names, predicted_genders):
                            colored_name = f"{Fore.GREEN}{name.strip()}{Style.RESET_ALL}"
                            print(f"{colored_name}: {gender}")
                    else:
                        print("No names found in the file.")
            except FileNotFoundError:
                print("File not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
