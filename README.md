# Gender Prediction App

   _____                _                                _ _      _   _                    __   ___  
  / ____|              | |                              | (_)    | | (_)                  /_ | / _ \ 
 | |  __  ___ _ __   __| | ___ _ __   _ __  _ __ ___  __| |_  ___| |_ _  ___  _ __   __   _| || | | |
 | | |_ |/ _ \ '_ \ / _` |/ _ \ '__| | '_ \| '__/ _ \/ _` | |/ __| __| |/ _ \| '_ \  \ \ / / || | | |
 | |__| |  __/ | | | (_| |  __/ |    | |_) | | |  __/ (_| | | (__| |_| | (_) | | | |  \ V /| || |_| |
  \_____|\___|_| |_|\__,_|\___|_|    | .__/|_|  \___|\__,_|_|\___|\__|_|\___/|_| |_|   \_/ |_(_)___/ 
                                     | |                                                             
                                     |_| By Nexayan      

Gender Prediction App is a Python application that utilizes a pre-trained neural network to predict genders based on input names. It provides an interactive command-line interface for predicting the gender of individual names or multiple names at once. Additionally, it offers the option to import names from a text file for bulk predictions.

## Features

- Predict gender for individual names
- Predict genders for multiple names
- Import names from a text file for predictions
- Command-line interface with clear instructions

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt`
3. Run the application using: `python gender_prediction_app.py`

## Usage

1. Choose a prediction mode:
   - `single` for predicting the gender of a single name
   - `multiple` for predicting genders of multiple names
   - `import` to predict genders from a text file

2. Follow the on-screen prompts to input names or provide a file path.

## Example

```bash
$ python gender_prediction_app.py
Select mode (single/multiple/import/exit)> single
Enter a name> Alex
Predicted gender for 'Alex': Male

Select mode (single/multiple/import/exit)> multiple
Enter a name (or 'done' to finish)> Emma
Enter a name (or 'done' to finish)> Liam
Enter a name (or 'done' to finish)> done

Predicted genders:
Emma: Female
Liam: Male

Select mode (single/multiple/import/exit)> import
Enter the path of the text file: names.txt

Predicted genders from imported file:
Alice: Female
Bob: Male
Charlie: Male
