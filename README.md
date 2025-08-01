# 🐾 Animal Recognizer

An AI-powered tool to **detect animals in images**, identify whether they're **juvenile or adult**, classify them as **herbivores or carnivores**, and—if multiple animals are present—**summarize how many herbivores and carnivores** are in the image.

Includes a user-friendly **GUI** to make predictions interactively and visually.

---

## 🌟 Features

✅ Detects multiple animals in a single image
✅ Classifies animals by:

* **Age**: Juvenile or Adult
* **Diet**: Herbivore or Carnivore
  ✅ Counts herbivores and carnivores when multiple animals are present
  ✅ Built-in **GUI interface** for image upload and prediction
  ✅ Supports **image and video input**

---

## 🖼️ Graphical User Interface (GUI)

The GUI makes it simple to test the model with your own images or videos.

### 💡 Key Functions:

* Upload an image or video
* View bounding boxes, age, and diet classification for each animal
* See a summary of animal counts by diet

### ▶️ Demo Video

🎥 **Demo**: [`task 3.mp4`](./task%203.mp4)
*(Ensure this file is present in the root directory of the repository.)*

### 🧪 Running the GUI

```bash
python gui.py
```

Make sure you have a trained model saved in the `models/` directory before launching the GUI.

---

## 📦 Dataset

* Dataset created using **web scraping** techniques.
* Images collected include a variety of animals across:

  * Species
  * Age (juvenile/adult)
  * Diet type (herbivore/carnivore)

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/jayantkathuria7/animal-recognizer.git
cd animal-recognizer
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

> Make sure dependencies for your GUI library (e.g., `PyQt5`, `Tkinter`) are included in `requirements.txt`.

---

## 🚀 Usage

### 🔧 Training the Model

```bash
python train.py --dataset path/to/data --output models/
```

### 📷 Predict from Image

```bash
python predict.py --image path/to/image.jpg --model models/latest.pth
```

### 🎞️ Predict from Video (optional feature)

```bash
python predict_video.py --video path/to/video.mp4 --model models/latest.pth
```

---

## 🧠 Model Output Example

```json
{
  "animals": [
    {
      "species": "zebra",
      "age": "juvenile",
      "diet": "herbivore",
      "bbox": [x1, y1, x2, y2]
    },
    {
      "species": "lion",
      "age": "adult",
      "diet": "carnivore",
      "bbox": [x1, y1, x2, y2]
    }
  ],
  "summary": {
    "total": 2,
    "herbivores": 1,
    "carnivores": 1
  }
}
```

---

## 📊 Architecture Overview

* **Detection model** (e.g., Faster R-CNN, YOLOv5) detects animal regions.
* **Age classifier** labels animals as child or adult.
* **Diet classifier** (based on species knowledge) labels as herbivore or carnivore.
* **Post-processing** compiles group stats.

---

## 🧪 Evaluation

* Detection accuracy: **mAP (mean Average Precision)**
* Classification metrics: **Accuracy**, **Precision**, **Recall**, **F1-score**
* Evaluation results stored in training logs and visualized during GUI inference.

---

## 📚 References & Sources

* Animal species classification inspired by public datasets and encyclopedic sources.
* Web scraping tools: BeautifulSoup, Selenium
* Herbivore vs Carnivore classification based on animal species knowledge
* Animal detection models adapted from open-source frameworks

---

## 📌 Future Improvements

* [ ] Add omnivore classification
* [ ] Improve species-level recognition (e.g., zebra, lion, elephant, etc.)
* [ ] Integrate live webcam prediction
* [ ] Export results to CSV or JSON
* [ ] Package GUI as standalone app (PyInstaller, etc.)
