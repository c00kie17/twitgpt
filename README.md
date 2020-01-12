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

* Pleace check the function [remove_unwated](https://github.com/c00kie17/twitgpt/blob/7d93ec5d4348a021a4ffe39636a620742f71b96f/twitter/tgpt_twitter.py#L20), to check current filters or add any new filters you need to your tweets
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
The dataset was created by using the following tech news accounts:
* [observer](https://twitter.com/observer)
* [mashable](https://twitter.com/mashable)
* [TechCrunch](https://twitter.com/TechCrunch)
* [thenextweb](https://twitter.com/thenextweb)
* [WIRED](https://twitter.com/WIRED)
* [verge](https://twitter.com/verge)
* [DigitalTrends](https://twitter.com/DigitalTrends)
* [arstechnica](https://twitter.com/arstechnica)
* [CNET](https://twitter.com/CNET)
* [androidcentral](https://twitter.com/androidcentral)
* [engadget](https://twitter.com/engadget)
* [ForbesTech](https://twitter.com/ForbesTech)
* [Gizmodo](https://twitter.com/Gizmodo)
* [BBCTech](https://twitter.com/BBCTech)
* [cnntech](https://twitter.com/cnntech)
* [HuffPostTech](https://twitter.com/HuffPostTech)
* [guardiantech](https://twitter.com/guardiantech)
* [WiredUK](https://twitter.com/WiredUK)
* [techreview](https://twitter.com/techreview)
* [WIREDScience](https://twitter.com/WIREDScience)
* [gadgetlab](https://twitter.com/gadgetlab)
* [Recode](https://twitter.com/Recode)
* [Techmeme](https://twitter.com/Techmeme)
* [slashdot](https://twitter.com/slashdot)
* [WSJTech](https://twitter.com/WSJTech)
* [technology](https://twitter.com/technology)
* [fttechnews](https://twitter.com/fttechnews)
* [ZDNet](https://twitter.com/ZDNet)
* [ReutersTech](https://twitter.com/ReutersTech)
* [usatodaytech](https://twitter.com/usatodaytech)

Download the dataset [here](https://drive.google.com/file/d/1yZfDvdb26kJl18i6pPhsQIFRauM3DFs6/view?usp=sharing)

The pretrained models 124M was finetuned on the dataset using a NVIDIA Tesla v100 GPU:

### 124M
The trained model zip can be found [here](https://drive.google.com/file/d/1KuGlj-BIIcfc6etYYWRiwtYRk8ZbFn2I/view?usp=sharing)
The command used to generate the text is `python3 generator.py --run_name=tech124M --model_name=124M --return_as_list=True --truncate="<|endoftext|>" --prefix="<|startoftext|>" --nsamples=10 --batch_size=10 --include_prefix=False --temperature=1.4 `
Trained for 30000 steps and a average loss of 0.25

				Mathematicians have been searching, but the answer lies in physics
				Has Dyson released a true wireless earbudsaker?
				Facebook co-founder Eduardo Saverin backtracks on controversial college admissions decisions
				 If money allowed enters the smart home wars, who wouldn't have thought paying taxes at a tech company is a subset of normal life?
				 attractive new Camry airbag touting current lineup
				Art Banks Are Using AI-Powered Cameras To Detect Stealing
				‘Kids can fall down and he’s the only one who can’t they stop’ …?
				Twitter chemical plants leak sign Zuckerberg doesn’t understand what the hell is going on
				Oxford Algorithms fail to produce longest-ever delayed signal, say experts
				Congress invoked the Foreign Relations Secrecy Act to shield the US government from foreign meddling in the politics of reasons of individuals










