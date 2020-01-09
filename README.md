# TwitGPT
> a GPT2 traininer using twitter posts

## Installation
* Clone the repo.
* run the following command to download all dependencies `pip3 install pyyaml python-twitter pandas gpt-2-simple`
* You need to create a file called `/twitter/settings.yaml` with the following information

		twitter_consumer_key: your twitter comsumer key
		twitter_comsumer_secret: your twitter comsumer secret
		twitter_access_token_key: your twitter access token
		twitter_access_token_secret:  your twitter token secret
		handles:
			- KeetPotato
			- david8hughes
			- Shen_the_Bird

* Please take a look at the [Twitter API](https://developer.twitter.com/en/docs) page for key information

## Usage

### Dataset

* To create a tweet dataset populate the `settings.yaml` with the handles you want to fetch the tweets for.
* Run `twitter/tgpt_twiiter.py` by running the command `python3 tgpt_twitter.py --csv_file_name=my_file_name`
* Once done the script will save the dataset in a `my_file_name.csv` file in `./csv` folder

### Training

* To start training run the file `./gpt/train.py` by running `python3 train.py --model_name=124M --csv_file=../csv/my_file_name.csv --steps=1000  --run_name=myrun`
* If the model has not been downloaded it will download the model and save it in `./gpt/models` directory unless changed by `--models_dir` parameter
* The training results will be saved in the directory `./gpt/checkpoint` unless changed by the `--checkpoint_dir` parameter
* To see all the possible parameters for trianing run `python3 train.py -h`

### Generation

* Once done training we can generate text using our model by running the `./gpt/generate.py`
* We can run the file by running the command `python3 generate.py --run_name=myrun --model_name=124M`
* If you want to save the generated text to the file you the paramerter `--destination_path`
* To see all the possible parameters for generation run `python3 generate.py -h`

## Results


