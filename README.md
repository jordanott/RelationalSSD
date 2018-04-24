# Relational Localization

### Author

Jordan Ott and Josh Graves

### Relational Questions

[examples of rq's]

### Relation Networks

Relational reasoning is an essential component of intelligent systems. To this end, Relation Networks (RNs) are proposed to solve problems hinging on inherently relational concepts. To be more specific, RN is a composite function:

<p align="center">
    <img src="figure/rn_eq.png" height="72"/>,
</p>

where *o* represents inidividual object while *f* and *g* are functions dealing with relational reasoning which are implemented as MLPs. Note that objects mentioned here are not necessary to be real objects; instead, they could consist of the background, particular physical objects, textures, conjunctions of physical objects, etc. In the implementation, objects are defined by convoluted features. The model architecture proposed to solve Visual Question Answering (VQA) problems is as follows.

<p align="center">
    <img src="figure/RN.png" height="350"/>
</p>

In addition to the RN model, **a baseline model** which consists of convolutional layers followed by MLPs is also provided in this implementation.

### Sort-of-CLEVR Cube World

To verify the effectiveness of RNs, a synthesized **VQA dataset** is proposed in the paper named Sort-of-CLEVR. The dataset consists of paired questions and answers as well as images containing colorful shapes.

Each **image** has a number of shapes (rectangle or circle) which have different colors (red, blue, green, yellow, cyan,  or magenta). Here are some examples of images.

<p align="center">
    <img src="figure/samples.png" width="720"/>
</p>

**Questions** are separated into relational and non-relational questions which are encoded as binary strings to prevent the effect of language parsing and embedding; while **answers** are represented as one-hot vectors. Examples of images, questions and answers are as follow.

<p align="center">
    <img src="figure/iqa.png" width="850"/>
</p>

Given a queried color, all the possible questions are as follows.

**Non-relational questions**

* Is it a circle or a rectangle?
* Is it closer to the bottom of the image?
* Is it on the left of the image?

**Relational questions**

* The color of the nearest object?
* The color of the farthest object?

And the possible answer is a fixed length one-hot vector whose elements represent

*[red, blue, green, yellow, cyan, magenta, circle, rectangle, yes, no]*

**File format**

Generated files use HDF5 file format. Each data point contains an *image*, an one-hot vector *q* encoding a question, and an one-hot vector *a* encoding the corresponding answer.

Note that this implementation only follows the main idea of the original paper while differing a lot in implementation details such as model architectures, hyperparameters, applied optimizer, etc. Also, the design of Sort-of-CLEVR only follows the high-level ideas of the one proposed in the orginal paper.

\*This code is still being developed and subject to change.

### Intersection over Union (IoU)

#TODO

## Results

| | RN (Ans, Loc) | Baseline (Ans, Loc) | RN (Ans) | Baseline (Ans)
| --- | --- | --- | --- | --- |
| Non-relational question | 98.93% | 78.89% | **99.17%** | 77.87% |
| Relational question | **73.26%** | 42.82% | 71.82% | 45.71% |
| Overall Acc | **88.69%** | 64.43% | 88.19% | 65.03% |
| Non-relational IoU | **0.61** | 0.11 | ----------- | ----------- |
| Relational IoU | **0.17** | 0.09 | ----------- | ----------- |
| Overall IoU | **0.43** | 0.10 | ----------- | ----------- |

# Visual Genome Dataset


## Related works

* [A Simple Neural Network Module for Relational Reasoning](https://arxiv.org/abs/1706.01427)
* [Visual Interaction Networks](https://arxiv.org/abs/1706.01433) by Watters et. al.
* [Interaction networks for learning about objects, relations and physics](https://arxiv.org/abs/1612.00222) by Battaglia et. al.
* Shao-Hua Sun's [implementation](https://github.com/gitlimlab/Relation-Network-Tensorflow)

## Prerequisites

- Python 2.7 or Python 3.3+
- [Tensorflow 1.0.0](https://github.com/tensorflow/tensorflow/tree/r1.0)
- [NumPy](http://www.numpy.org/)
- [PIL](http://pillow.readthedocs.io/en/3.1.x/installation.html)
- [matplotlib](https://matplotlib.org/)
- [h5py](http://docs.h5py.org/en/latest/)
- [progressbar](http://progressbar-2.readthedocs.io/en/latest/index.html)
- [colorlog](https://github.com/borntyping/python-colorlog)

### To Do
- [x] Modify RN for localization
- [x] Create dataset from real images
  - [x] Relational questions
  - [x] Non-relational questions
  - [x] Bounding box coordinates (x,y,w,h)
  - [x] Visualize dataset examples
- [x] Experiments
  - [x] CNN without RN
    - [x] Non-relational questions
    - [x] Non-relational & relational questions
  - [x] CNN with RN
    - [x] Non-relational questions
    - [x] Non-relational & relational questions
  - [ ] Question embedding options
    - [ ] Preset one-hot questions (no RNN)
    - [ ] With RNN to process questions
- [x] Visualize bounding box results on images
