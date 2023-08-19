<!-- Logo -->
<p align="center">
  <img src="logo.png" alt="Logo">
</p>

<!-- Title -->
<h1 align="center">Gender Prediction App</h1>

<!-- Description -->
<p align="center">
  Predict genders based on names using a neural network model. This Python application offers an interactive command-line interface for individual and bulk predictions.
</p>

<!-- Features -->
## Features

- Predict gender for individual names
- Bulk prediction for multiple names
- Import names from text files
- Clear and interactive command-line interface

<!-- Getting Started -->
## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `python gender_prediction_app.py`


<!-- Usage -->
## Usage

1. Select a prediction mode:
- `single`: Predict gender for a single name
- `multiple`: Bulk prediction for multiple names
- `import`: Import names from a text file

2. Follow the prompts to input names or provide a file path.

<!-- Example -->
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
```

<!-- Requirements -->
Requirements
Python 3.x
TensorFlow
NumPy
Colorama (for colored output)
<!-- License -->
License
This project is licensed under the MIT License.

<!-- Footer -->

