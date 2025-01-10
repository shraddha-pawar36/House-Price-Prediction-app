# House Price Prediction App

## Overview
This repository contains a web-based application built using **Dash** that predicts house prices based on user input. The model is trained using **Linear Regression** on the **USA Housing** dataset.

---

## Features
- **User Input Form:** Enter details about a house such as number of rooms, area, population, etc.
- **Price Prediction:** Predicts the house price based on user inputs.
- **Interactive Interface:** Built with Dash for a user-friendly experience.
- **Pre-trained Model:** The model is already trained and saved for quick deployment.

---

## Files and Directories

1. **app.py** - Main script to run the Dash app.
2. **model_training.py** - Script used to train the Linear Regression model and save it as a pickle file (`train.pkl`).
3. **train.pkl** - Serialized Linear Regression model used for predictions.
4. **USA_Housing.csv** - Dataset used to train the model.
5. **Screenshots/** - Folder containing screenshots of the application interface.
6. **requirements.txt** - List of required Python libraries to run the app.

---

## Setup Instructions

### 1. Clone the repository:
```
gh repo clone shraddha-pawar36/House-Price-Prediction-app
```

### 2. Create a virtual environment (optional but recommended):
```
python3 -m venv venv
source venv/bin/activate   # On Linux/MacOS
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies:
```
pip install -r requirements.txt
```

### 4. Run the app:
```
python app.py
```

### 5. Open in browser:
Navigate to:
```
http://127.0.0.1:8050/
```

---

## Dependencies
- Dash
- Pandas
- Scikit-learn
- Numpy
- Pickle

---

## How It Works
1. The `model_training.py` file loads the **USA Housing** dataset and trains a **Linear Regression** model.
2. The model is saved as `model.pkl` using **Pickle**.
3. The `app.py` file loads this model and serves the web interface.
4. Users can enter details about the house, and the app predicts the price based on the inputs.

---

## Screenshots
Screenshots of the application interface can be found in the `Screenshots` folder.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## Contact
For any questions or suggestions, feel free to reach out:
- Email: shradhapawar522@gmail.com
- GitHub: https://github.com/shraddha-pawar36

