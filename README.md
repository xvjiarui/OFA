# OFA

[[Paper]](http://arxiv.org/abs/2202.03052) [Blog] [Colab]


![Overview](examples/overview.png)

OFA is a unified multimodal pretrained model that unifies modalities (i.e., cross-modality, vision, language) and tasks 
(e.g., image generation, visual grounding, image captioning, image classification, text generation, etc.) 
to a simple sequence-to-sequence learning framework. For more information, please refer to our paper: [Unifying Architectures, Tasks, and Modalities Through a Simple Sequence-to-Sequence Learning Framework](http://arxiv.org/abs/2202.03052).


# Approach
![approach](examples/approach.jpg)


# Requirements
* python 3.7.4
* pytorch 1.8.1

# Installation
```bash
git clone https://github.com/OFA-Sys/OFA
pip install -r requirements.txt
```

# Datasets and Checkpoints
See [datasets.md](datasets.md) and [checkpoints.md](checkpoints.md).

# Pretraining
To release soon:)

# Finetuning & Inference
Below we provide methods for fintuning and inference on different downstream tasks. At this moment we only provide the scripts for inference, and we will soon release those for finetuning. 
## Caption
1. Download data and files and put them in the correct directory
2. Run the commands below,

```bash
cd run_scripts/caption
sh evaluate_caption.sh
```

# Gallery
Below we provide examples of OFA in text-to-image generation and open-ended VQA. Also, we demonstrate its performance in unseen task (Grounded QA) as well as unseen domain (Visual Grounding on images from unseen domains). 

## Text-to-Image Generation (normal query)
![t2i_normal](examples/normal_images.png)

## Text-to-Image Generation (counterfactual query)
![t2i_counterfactual](examples/counterfactual_images.png)

## Open-Ended VQA
![open_vqa](examples/open_vqa.png)

## Grounded QA (unseen task)
![grounded_qa](examples/grounded_qa.png)

## Viusal Grounding (unseen domain)
![vg](examples/viusal_grounding.png)


# Citation
Please cite our paper if you find it helpful :)

```
@article{wang2022OFA,
  title={Unifying Architectures, Tasks, and Modalities Through a Simple Sequence-to-Sequence Learning Framework},
  author={Wang, Peng and Yang, An and Men, Rui and Lin, Junyang and Bai, Shuai and Li, Zhikang and Ma, Jianxin and Zhou, Chang and Zhou, Jingren and Yang, Hongxia},
  journal={arXiv e-prints},
  pages={arXiv--2202},
  year={2022}
}
```