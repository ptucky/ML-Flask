### Conda Installation 
https://linuxhint.com/fix-zsh-command-not-found-conda-mac/

1. Step 1: Check Conda Installation 
> conda --version

1. Install Conda on Mac 
> wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh


/Users/pravee/miniconda.sh               100%[===============================================================================>]  69.55M  22.3MB/s    in 3.1s    
2023-08-23 09:08:13 (22.3 MB/s) - ‘/Users/pravee/miniconda.sh’ saved [72930976/72930976]


3. Step 3: Give Execute Permission to the File
> chmod +x ./miniconda.sh
or
> chmod +x /Users/pravee/miniconda.sh

4. Step 4: Execute the Conda Script File
> ./miniconda.sh
  or
> /Users/pravee/miniconda.sh


installation finished.
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[yes] >>> yes
no change     /Users/pravee/miniconda3/condabin/conda
no change     /Users/pravee/miniconda3/bin/conda
no change     /Users/pravee/miniconda3/bin/conda-env
no change     /Users/pravee/miniconda3/bin/activate
no change     /Users/pravee/miniconda3/bin/deactivate
no change     /Users/pravee/miniconda3/etc/profile.d/conda.sh
no change     /Users/pravee/miniconda3/etc/fish/conf.d/conda.fish
no change     /Users/pravee/miniconda3/shell/condabin/Conda.psm1
modified      /Users/pravee/miniconda3/shell/condabin/conda-hook.ps1
no change     /Users/pravee/miniconda3/lib/python3.11/site-packages/xontrib/conda.xsh
no change     /Users/pravee/miniconda3/etc/profile.d/conda.csh
modified      /Users/pravee/.zshrc


5. Step 5: Reload the Changes
> source /Users/pravee/miniconda3/bin/activate

6. Step 6: Test the Conda Installation
> conda --version
```
conda 23.5.2
```
###

## VDO 1 : Build a Machine Learning App From Scratch with Flask & Docker ##
VDO Part1: https://www.youtube.com/watch?v=S--SD4QbGps
VDO Part2: https://www.youtube.com/watch?v=zGP_nYmZd9c
VDO Simple Falsk API: https://www.youtube.com/watch?v=zsYIw6RXjfM&list=PL5hH4_l-LhbKMWMtfxdHo8AKV9aYI1bSV&index=2&t=620s

  > cd ml-dev
  > conda create -n nlp puythion=3.9

  > conda activate nlp
  ```
  EnvironmentNameNotFound: Could not find conda environment: nlp
  You can list all discoverable environments with `conda info --envs`.
  ```

  > conda info --envs
  ```
  # conda environments:
  #
  base                  *  /Users/pravee/miniconda3
  ```

  > conda config --show envs_dirs
  ```
  envs_dirs:
    - /Users/pravee/miniconda3/envs
    - /Users/pravee/.conda/envs
  ```

- Activate conda on mac
  > conda activate /Users/pravee/miniconda3
  or deactivate
  > conda deactivate 

- install
  step1
  > conda install jupyter ipykernel 
  > conda install scikit-learn 
  > conda install nltk

  step2
  > jupyter notebok
  it will redirect to http://localhost:8888/tree

  step3 open a new terminal
  > conda activate /Users/pravee/miniconda3
  > conda install pandas 


  ## run jupyter notebook จะเห็น folder directory บน webbrowser
  > cd ml-dev/
  > jupyter notebook 


  ### Folow vdo until 14:20 https://youtu.be/S--SD4QbGps?t=860
  > cd app/api
  > python utilities.py

  ## Install Falsk API
  > cd app/api
  > pip install Flask

  - creste app.py + utitlities.py
  
  > cd app/api/
  > python app.py

- open browser http://127.0.0.1:5000/predict
  it will show Method Not Allowed
- CURL Command
> curl -X POST -H "Content-Type: application/json" -d '{"text": "May the Force be with you"}' 127.0.0.1:5000/predict
> curl -X POST -H "Content-Type: application/json" -d '{"text": "I hate twitte"}' 127.0.0.1:5000/predict


## library list requirement.txt
> conda list

- create requirements.txt

```
flask>=2.3.3
scikit-learn==1.0.1
nltk==3.6.6
# "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"
```  

## VDO 2 : Create Dockerfile ##
- Create Dockerfile
- Create docker-compose
> docker compose up --build