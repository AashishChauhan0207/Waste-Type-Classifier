# Waste Type Classifier

A real-time waste classification system using computer vision and machine learning to identify and categorize different types of waste materials through camera input. The model is trained using Roboflow's computer vision platform.

## Model Details

- **Dataset**: 3500 images across different waste categories
- **Model Type**: Single-Label Classification
- **Training Platform**: Roboflow
- **Model Performance**: Trained with validation accuracy reaching ~95%

### Dataset Categories
- Battery (Hazardous Waste)
- Biological (Organic Waste)
- Cardboard (Recyclable)
- Clothes (Textile Waste)
- Glass (Recyclable)
- Metal (Recyclable)
- Paper (Recyclable)
- Plastic (Recyclable)
- Shoes (Textile Waste)
- Trash (General Waste)

## Features

- Real-time waste classification through camera feed
- Supports multiple waste categories:
  - Hazardous Waste (Batteries)
  - Organic Waste (Biological)
  - Recyclable (Cardboard, Glass, Metal, Paper, Plastic)
  - Textile Waste (Clothes, Shoes)
  - General Waste (Trash)
- Live display of classification results with confidence scores
- User-friendly interface with keyboard controls

## Requirements

- Python 3.x
- OpenCV
- Roboflow

## Installation

1. Clone this repository
2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up Roboflow integration:
   - Create a free account at [Roboflow](https://roboflow.com)
   - Get your API key from your Roboflow account settings
   - Replace the placeholder API key in the code with your actual Roboflow API key
   - Update the project name and model version in the code:
     ```python
     project = rf.workspace().project("your-project-name")
     model = project.version("your_version_number").model
     ```

### Roboflow Model Access
The project uses a trained model hosted on Roboflow. The model was trained on a custom dataset of 3,500 images with various waste types. To use this classifier:

1. Create your Roboflow account
2. Either:
   - Use your own trained model by updating the project and version numbers
   - Or request access to our pre-trained model by contacting us

## Usage

1. Run the script:
```bash
python WasteTypeClassificationWithCameraAccess.py
```

2. Controls:
- Press 'c' to capture and classify an image
- Press 'q' to quit the application

## Sample Images

Here are some sample images from our test dataset:

![Sample 1](Images/1.jpg)
![Sample 2](Images/2.jpg)
![Sample 3](Images/3.jpg)
![Sample 4](Images/4.jpg)
![Sample 5](Images/5.jpg)
![Sample 6](Images/6.jpg)
![Sample 7](Images/7.jpg)

## Configuration

You can modify the `category_map` dictionary in the code to customize waste categories according to your needs.

## Note

Make sure to set up your camera properly. The default camera index is 1 (for virtual input), change to 0 for built-in webcam or adjust according to your setup.
