from tgpt_global import globalManager
import gpt_2_simple as gpt2




if __name__ == '__main__':
	sess = gpt2.start_tf_sess()
	gpt2.finetune(sess,
		globalManager.args.csv_file,
		model_name=globalManager.args.model_name,
		steps=globalManager.args.steps,
		run_name=globalManager.args.run_name)