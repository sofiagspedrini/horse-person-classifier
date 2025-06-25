# Horse-Person Classifier

A CNN-based image classification API that distinguishes between horses and people.

## Project Structure
```bash
horse-person-classifier/
├── app/
│   ├── main.py                 
│   ├── model/
│   │   └── horse_person_cnn_model.keras
│   └── utils/
│       └── preprocessing.py     
├── Dataset/
│   ├── Test   
│       ├── horses/                
│       └── humans/             
│   └──  Train/
│       ├── horses/                
│       └── humans/  
├── notebooks/
│   └── Experiments.ipynb  
├── Results/
│   ├── Part1/                
│   └── Part2/   
├── README.md             
└── requirements.txt                           
```          

## How to Run

1. Open the horse-person-classifier folder in your terminal.

2. Create new environment:

```bash
conda create -n horse-person-api python=3.8 -y
conda activate horse-person-api
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Run the API:

```bash
python -m app.main
```

5. In other terminal, send a POST request to `/predict` with an image:

```bash
curl.exe -X POST -F "file=@path/image.jpg" http://127.0.0.1:5000/predict 
```

6. Check folder 