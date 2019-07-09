### 1.Tale
#### 1) Original upload
1. Airbnb sydney.csv
2. IS457_SP19_138.R
3. IS457_SP19_138.Rmd

#### 2) Bundle
1. metadata
 - environment.json
 - manifest.json
2. workspace
 - Airbnb sydney.csv
 - IS457_SP19_138.R
 - IS457_SP19_138.Rmd
3. LICENSE
4. README.md

### 2.Popper
#### 1) Original upload
##### [popper_demo](./popper_demo)
1. requirements.txt
2. scripts
 - generate_data.py
 - generate_figures.py
3. main.workflow

#### 2) Bundle
##### Import workflow from remote repo.

`$ popper add https://github.com/Yang9508/internship/popper_demo`

##### get same thing as what uploaded

### 3.reprozip
#### 1) Original upload
1. [digitRecognition](./digitRecognition)
 - generateClassifier.py
 - performRecognition.py
 - photo.jpg

#### 2) Bundle
##### Use reprozip as a .rpz file, named as [digitRecognition.rpz](https://osf.io/5ztp2/download).
`$ reprozip trace python generateClassifier.py`

`$ reprozip trace --continue python performRecognition.py`

`$ reprozip pack digitRecognition.rpz`

##### Then unzip it, named as [reprozip_demo](./reprozip_demo).
`$ reprounzip info digitRecognition.rpz`

- Total software packages: 118
- Packed software packages: 118

`$ reprounzip showfiles digitRecognition.rpz`

`$ reprounzip vagrant setup digitRecognition.rpz reprozip_demo/`

1. Input files:
 - arg0
 - arg1
 - digits_cls.pkl
 - mnist-original.mat
 - photo.jpg
2. Output files:
 - digits_cls.pkl
 - output.jpg

### 4.Sumatra
#### 1) Original upload
1.

#### 2) Bundle

### 5.Occam
#### 1) Original upload
1. A workflow created on Occam platform. The workflow contains four simulations--four simulators-- a vedio result

#### 2) Bundle
1. https://occam.cs.pitt.edu/QmS9BPf6AGk1qZ3tht541211DY2yQi7UzJ6eZqGZGQ3xy4/5dt2r3Nq9kKrXfbbmucY3JKvTDF8oh?embed=true&link=93

### 7.Binder
#### 1) Original upload

#### 2) Bundle
1. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Yang9508/IS457/master)
2. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Yang9508/ggplot.git/master)
3. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Yang9508/ggplot/master?urlpath=rstudio)
4. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Yang9508/ggplot/master?urlpath=index.ipynb)
5. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Yang9508/ggplot/master?urlpath=shiny/bus-dashboard/)
