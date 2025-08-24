import cv2
from roboflow import Roboflow

# Roboflow setup
rf = Roboflow(api_key="your_roboflow_api_key")
project = rf.workspace().project("your-project-name")
model = project.version("your_version_number").model

# Waste category mapping
category_map = {
    "Battery": "Hazardous Waste",
    "Biological": "Organic Waste",
    "Cardboard": "Recyclable",
    "Clothes": "Textile Waste",
    "Glass": "Recyclable",
    "Metal": "Recyclable",
    "Paper": "Recyclable",
    "Plastic": "Recyclable",
    "Shoes": "Textile Waste",
    "Trash": "General Waste"
}

# Open camera
cam_index = 1  # Use 0 for built-in webcam or 1 for virtual input
cap = cv2.VideoCapture(cam_index)

if not cap.isOpened():
    print(f"Cannot open camera at index {cam_index}")
    exit()

window_name = "Waste Classifier - Press 'c' to Capture, 'q' to Quit"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

print("Ready. Press 'c' to capture, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow(window_name, frame)
    key = cv2.waitKey(1)

    if key == ord('c'):
        filename = "capture.jpg"
        resized = cv2.resize(frame, (416, 416))
        cv2.imwrite(filename, resized)

        # Predict with retry
        try:
            result = model.predict(filename).json()
        except Exception as e:
            print(f"Prediction failed: {e}. Retrying...")
            try:
                result = model.predict(filename).json()
            except Exception as e:
                print(f"Retry failed: {e}")
                continue

        print("Raw Result:", result)

        # Extract prediction
        predicted_class = "Unknown"
        confidence = 0.0

        outer_preds = result.get("predictions", [])
        if outer_preds and "predictions" in outer_preds[0]:
            inner_preds = outer_preds[0]["predictions"]
            if inner_preds:
                prediction = inner_preds[0]
                predicted_class = prediction.get("class", "Unknown")
                confidence = prediction.get("confidence", 0.0) * 100

        category = category_map.get(predicted_class, "Unknown")
        line1 = f"{predicted_class} ({confidence:.1f}%)"
        line2 = f"{category}"

        # Font settings
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.9
        thickness = 2

        # Text size for padding
        size1, _ = cv2.getTextSize(line1, font, font_scale, thickness)
        size2, _ = cv2.getTextSize(line2, font, font_scale, thickness)
        text_width = max(size1[0], size2[0])
        text_height = size1[1] + size2[1] + 30

        # Add top padding
        padded_img = cv2.copyMakeBorder(
            resized, text_height, 0, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0)
        )

        # Draw background box for text
        cv2.rectangle(padded_img, (0, 0), (text_width + 20, text_height), (0, 0, 0), -1)

        # Put both lines of text
        cv2.putText(padded_img, line1, (10, size1[1] + 10), font, font_scale, (0, 255, 0), thickness)
        cv2.putText(padded_img, line2, (10, size1[1] + size2[1] + 20), font, font_scale, (0, 255, 0), thickness)

        # Show prediction result
        cv2.imshow("Prediction Result (press any key)", padded_img)
        cv2.waitKey(0)
        cv2.destroyWindow("Prediction Result (press any key)")

    elif key == ord('q') or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        print("Exiting...")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
