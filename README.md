# MasKorona

## Coronavirus (aka. COVID)

<img src="https://user-images.githubusercontent.com/9033365/76415349-7797ff80-63b2-11ea-867f-30a59813eb6b.png" alt="Example" width="400">

In December 2019, the world witnessed an aweful outbreak of [coronavirus disease](https://www.who.int/emergencies/diseases/novel-coronavirus-2019) in China. Not a long time later, it has been spread in more than 100 countries. No vaccine is currently available!

One underrated way of minimizing spreading the virus and protecting ourselves from it is to **wear a mask**.

<img src="https://www.who.int/images/default-source/health-topics/coronavirus/masks/masks-4.png" alt="Example2" width="400">

MasKorona utilizes Artificial Intelligence to distinguish mask-covered vs non-covered faces. MasKorona can be used in surveillance cameras in streets, offices, or crowded places such as supermarkets.

## DEMO

Video can be found [here](https://drive.google.com/file/d/1MYQ2FUgcPoH6fZs5bkoD_G3gwL6RB4zb/view?usp=sharing).

Mask is ON:
![image](https://user-images.githubusercontent.com/9033365/77861755-ffda2980-7227-11ea-9a48-1de1169f8738.png)

No mask:
![image](https://user-images.githubusercontent.com/9033365/77861733-e0430100-7227-11ea-8ed1-086818233d3f.png)

Video can be found [here](https://drive.google.com/file/d/1MYQ2FUgcPoH6fZs5bkoD_G3gwL6RB4zb/view?usp=sharing).

## Dataset
Data contains images of faces with and without masks. Data size is as follows:

|           | Mask | No Mask |
| --------- | ---- | ------- |
| Training  | 180  |   528   |
| Test      | 44   |   132   |

Data is collected & processed as following:

1. Images were downloaded from Google Images using [this chrome extension](https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm). Keywords used: face wearing corona mask, medical mask face, frontal face.
2. Faces were extracted from all downloaded images using OpenCV. Extarcted faces were converted to black & white images and saved locally.

![image](https://user-images.githubusercontent.com/9033365/77862323-bdb2e700-722b-11ea-92c7-1fb47ee0c506.png)

![image](https://user-images.githubusercontent.com/9033365/77862352-ecc95880-722b-11ea-8efd-12f207ffba1b.png)

## Training
For training, a pre-trainied ResNet34 has been fine-tuned. Full details are in [this notebook: training.ipynb](./training.ipynb)

![image](https://user-images.githubusercontent.com/9033365/77861895-f604f600-7228-11ea-950c-210649bf46f8.png)

![image](https://user-images.githubusercontent.com/9033365/77861907-03ba7b80-7229-11ea-87aa-c5cf5e4d81eb.png)

To run notebooks:

1. Download & install [Anaconda](https://www.anaconda.com/distribution/) (python 3.7 version)
2. Create a new environment & download all necessary python packages from **corona.yml**:
```
conda env create -f corona.yml
```
3. Activate created environement:
```
activate corona
```
4. Download & install Jupyter Notebook:
```
conda install -c conda-forge notebook
```
5. Run Jupyter Notebook:
```
jupyter notebook
```
and navigate to notebooks directory.



To try app with webcam, follow the previous steps till (including) step 3, then run script:
```
python corona_mask_webcam.py
```

**NOTE:** to run corona_mask_webcam.py, you need a pre-trained model, named export.pkl, in the same directory along with the script. My pre-trained model and data are not available for public yet! 
