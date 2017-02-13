
_Warning: work in progress..._

# Transfer Learning for Tensorflow

* Object Detection based on [TensorBox - GoogleNet/Overfeat/Rezoom](https://github.com/TensorBox/TensorBox)
* Classification based on [Tensorflow - InceptionV3](https://www.tensorflow.org/how_tos/image_retraining/)

## Setup

```bash
pip -r requirements.txt
make
make download
```

## Unit Tests

```bash
make test
```
## Todo

* Create validation set facility
* Improve model persistence
* Untangle rectangle stitching and results from the image rendering
* Make threads shut down gracefully
* Bring in classification retrain code from TF
* Add unit tests for Classification
* Refactor
* Get rid of Tensorflow deprecation warnings
* Upgrade Tensorflow version
* Allow for more fine grained training controls + unit tests
* Experiment with different base models
