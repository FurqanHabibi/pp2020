## Requirements
- Install conda (if you haven't).
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
- Create a conda environment and use it.
```
conda create -n <env_name> python=3.8
conda activate <env_name>
```
- Install GPU requirements for Tensorflow.
   - please refer [here](https://www.tensorflow.org/install/gpu#install_cuda_with_apt)

- Install Tensorflow 2 (we use nightly here to get latest features)
```
pip install tf-nightly-gpu==2.4.0.dev20201023
```
- Install PyTorch.
```
pip install torch==1.7.0+cu110 torchvision==0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```
- Install ONNX.
```
pip install tensorflow-addons
pip install git+https://github.com/onnx/onnx-tensorflow.git
```
- Install other requirements.
```
conda install -c conda-forge notebook ipywidgets tqdm matplotlib
conda install pandas scipy
```

## Quickstart
- Convert the BIQA PyTorch model to Tensorflow 2-compatible ONNX model by running [this notebook](BIQA_model/convert_to_tensorflow.ipynb).
- Run [this notebook](CarliniWagnerL2.ipynb) to perform the attack and generate the adversarial examples.

Some things to note:
- The classifier threshold(s) for the biqa model are tunable.
- Various hyperparameters are supported by the C&W algorithm. Please refer to the [code](carlini_wagner_l2.py).

---
# 2020-Pixel-Privacy-Task: Quality Camouflage for Social Images
This task develops image modification technology that helps to protect user privacy. In this year, it is dedicated to creating (adversarial) camouflage approaches that invisibly change or visibly enhance images in such a way that the Blind Image Quality Assessment (BIQA) algorithm predicts modified images as low quality.
The quality camouflage will help to ensure that personal photos reflecting sensitive scene information, e.g., vacation photos depicting people, are less easily findable via image search engines. The task is "whitebox" in the sense that you have full knowledge of the BIQA algorithm that makes predictions. 

This page contains information on participating in the task. We welcome innovative approaches in 2020: we are interested in what works, and what does not work.

For more information contact Zhuoran Liu (z.liu@cs.ru.nl)

## Instructions
In this task, the quality camouflage should achieve two goals: (1) Protection: It must block the ability of a binary BIQA classifier, which has been trained on the KonIQ-10k data set, from correctly predicting the quality of images and (2) Appeal: The changes made to the image must be as imperceptible to the human eye as possible, or the changes must contribute to enhancing the appeal of the image. Note that the task is not focused on concealing sensitive information from humans, rather from automatic inference.

Note that submissions that can be easily deflected by practical image operations are not encouraged. We will pre-process submitted images with JPEG compression (quality factor = 90%)  before calculating the BIQA scores. Such slight JPEG compression could mitigate the adversarial effects to a certain extent, but has little impact on BIQA scores.

The task provides:
* a list of 1000 images from the KonIQ-10k data set to use as a development set to develop your approach(es).

* a list of 550 images from the Places365-Standard data set to use as a test set to test your approach(es). These are the images with good quality (BIQA score > **50**) selected from the test set last year, but with a higher image resolution (512x384).

To participate in the task, you must submit versions of the test images to which your protective modification has been applied. The task organizers will then evaluate your approach(es) and return the results to you. Then, you write up your findings in a 2-page paper to submit to the MediaEval 2020 working notes proceedings. We are especially interested in identifying highly creative promising approaches, but also in negative results that provide information on what does not work.

**Participants are strongly encouraged to release their code when submitting their runs.**

## Task schedule
* **Saturday 31 October 2020:** Upload your images (see submission instructions below)
* Begin writing your 2-page working notes paper, see information at MediaEval 2020 Working Notes for format and instructions.
* **Sunday 15 November 2020:** Results are returned to you
* Add the results to your working notes paper, and complete writing the discussion and outlook sections
* **Monday 30 November 2020:** Finalize your working notes paper and submit

## Necessary resources
You will get all the necessary resources by following the **Easy preparation** steps.  
### Easy preparation:
0. Clone the Pixel Privacy 2020 repository```git clone https://github.com/multimediaeval/2020-Pixel-Privacy-Task.git```
1. Download and prepare data: ```bash task_prepare.sh```
2. Download pre-trained model from [here](https://surfdrive.surf.nl/files/index.php/s/oeGv7wEyyMwwbIO), and save the model in folder ```./BIQA_model```.
### Detailed instructions:
  * The BIQA model (PyTorch) that is used as the target white-box model to block can be downloaded [here](https://surfdrive.surf.nl/files/index.php/s/oeGv7wEyyMwwbIO). Given an image, the BIQA model can predict a score ranging from 0 to 100, and a higher score indicates better image quality. More details can be found in the overview paper. To calculated the BIQA score by our pre-trained model, please follow this [notebook](https://github.com/multimediaeval/2020-Pixel-Privacy-Task/blob/master/BIQA_model/BIQA_score.ipynb).

  * The development set `MEPP20dev`, i.e., the validation set of KonIQ-10k, can be downloaded [here](http://datasets.vqa.mmsp-kn.de/archives/koniq10k_512x384.zip). Ground truth scores for all images are available [here](https://github.com/subpic/koniq/blob/master/metadata/koniq10k_distributions_sets.csv) under the column name ‘MOS’.
  
  * The test set `MEPP20test` is a subset of the validation images from the Places365-Standard data set, which can be downloaded [here](http://data.csail.mit.edu/places/places/val_large.tar).
  
  * `MEPP20test_manual` (relevant if you are applying image modifications by hand): Focus on these images if you are applying protective modifications by manually manipulating the images (instead of using an automatic filter). This file can be found [here](https://github.com/multimediaeval/2020-Pixel-Privacy-Task/blob/master/MEPP20labels/MEPP20test_manual.csv).
 
  * The overview paper is under construction now. We will disseminate it soon. Please cite this paper in your MediaEval 2020 Working Notes paper and wherever you use the dataset, along with the citation for the Places365-Standard and KonIQ-10k data sets.

## How to submit
* Make sure that you have signed up to participate in the task and have returned your usage agreement. Confirm with Martha Larson (m.larson at cs.ru.nl) that you would like to participate in the task if you signed up but did not receive an email.
* You will then receive a Google drive folder in which to submit your runs. 
  * A "run" is a single image modification algorithm, or type of image modification, which you apply to the images in the test set.
  * For each run, please invent a unique run code that includes your team name (i.e., the team name is the one that you used to register). For example, `rteam_base`. 
  * When you carry out the run, append the unique run code to each image filename, e.g., `rteam_base_Places365_val_00014191.jpg`
  * Create a .zip file for each run that contains the modified test set images. Use the unique run code as the .zip file filename. 
* You can submit maximally **five** runs. If you have more than five approaches, you need to decide which of them are most promising and submit only those. This helps you focus on quality rather than quantity (and to fit your entire description into a 2-page paper).


## Motivation and larger objectives
The objective of the MediaEval Pixel Privacy task is to promote the innovation of protective technologies that make it safer to share social multimedia online. Here, we briefly sketch two motivations for the task.

First, recently, we are becoming better aware of how easy it is for social network data to be misappropriated (cf. https://www.theguardian.com/commentisfree/2018/mar/19/facebook-data-cambridge-analytica-privacy-breach) or how quickly companies and citizens can diverge in their idea of what constitutes appropriate use of social network data (cf. https://www.theguardian.com/technology/2017/may/01/facebook-advertising-data-insecure-teens).
It is clearly important to be able to trust social networks.
However, these examples underline that users *also* need technologies that they can apply locally before sharing images, so that it is not necessary to place their trust completely in the hands of social networks.

Second, as computer vision and artificial intelligence advances, it will be increasingly difficult for individual users to estimate the danger of sharing any particular image online.
Even if they do understand the capabilities of modern technology to infer information from their images, it is difficult to stay focused on this danger during the act of image sharing.
Specifically, when users take images to share online, they are focused on the specific subject matter that they have chosen for the image, and may not be paying attention to background detail.
It is exactly this background that can leak private information, for example, revealing that a user is traveling.
The aim of Pixel Privacy is to develop fun-to-use technologies, so that users protect their privacy in the act of enhancing their images, without having to think separately about privacy risks.
As users *dress up* their images, they are automatically contributing to their privacy without having to pay attention to background detail, or to understand the capabilities of artificial intelligence approaches to infer sensitive information about individuals using large quantities of data.
