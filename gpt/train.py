import gpt_2_simple as gpt2
import argparse
import os


def get_args():
		parser = argparse.ArgumentParser(description='Training GPT2 on sample')
		parser.add_argument('--model_name',metavar='MODEL', help='name of the model you want to download 124M,355M,774M,1558M', required=True)
		parser.add_argument('--csv_file',metavar='PATH', help='path of the csv file to train with', required=True)
		parser.add_argument('--steps', help='how many steps you want to train for',type=int, required=True)
		parser.add_argument('--run_name', help='name of the run you want to save in checkpoints folder', required=True)
		parser.add_argument('--models_dir',metavar='PATH', help='name of the directory where the model is saved ', default='./models')
		parser.add_argument('--combine',metavar='CHARS' ,help='Concatenate files with <|endoftext|> separator into chunks of this minimum size',type=int ,default=50000)
		parser.add_argument('--batch_size', metavar='SIZE',help='number of examples it will train on at a time ', default=1,type=int)
		parser.add_argument('--learning_rate', metavar='LR', help='learning rate of the optimizer', default=0.0001,)
		parser.add_argument('--accumulate_gradients', type=int, default=1, help='Accumulate gradients across N minibatches.')
		parser.add_argument('--checkpoint_dir', metavar='PATH',default='./checkpoint', help='The directory to save checkpoints in')
		parser.add_argument('--sample_every', type=int,metavar='N', default=100, help='After how many steps do you want to generate a sample')
		parser.add_argument('--sample_length', type=int,metavar='TOKENS', default=1024, help='size of the generated sameple')
		parser.add_argument('--sample_num', type=int,metavar='N', default=1, help='number of samples you want to generate')
		parser.add_argument('--multi_gpu', type=bool, default=False, help='if you have multiple GPUs')
		parser.add_argument('--save_every', type=int, default=1000, help='after how many steps should the model save')
		parser.add_argument('--print_every', type=int, default=1, help='how often should the model print progress')
		parser.add_argument('--max_checkpoints', type=int, default=1, help='how many checkpoints can exists together in the directory')
		parser.add_argument('--use_memory_saving_gradients', type=bool, default=False, help='Use gradient checkpointing to reduce vram usage')
		parser.add_argument('--only_train_transformer_layers', type=bool, default=False, help='Restrict training to the transformer blocks')
		parser.add_argument('--optimizer', default="adam", help='Optimizer to use while training defauls to adam')
		parser.add_argument('--overwrite', default=False,type=bool, help='Overwrite the last run')
		parser.add_argument('--restore_from', type=str, default='latest', help='Either "latest", "fresh", or a path to a checkpoint file')
		return parser.parse_args()

def download_model(args):
	if not os.path.isdir(os.path.join("models",args.model_name)):
		print(f"Downloading {args.model_name} model...")
		gpt2.download_gpt2(model_name=args.model_name)
	else:
		print(f"Model {args.model_name}  already downloaded")



if __name__ == '__main__':
	args = get_args()
	download_model(args)
	sess = gpt2.start_tf_sess()
	gpt2.finetune(sess,
		args.csv_file,
		model_name=args.model_name,
		steps=args.steps,
		run_name=args.run_name,
		model_dir=args.models_dir,
		combine=args.combine,
		batch_size=args.batch_size,
		learning_rate=args.learning_rate,
		accumulate_gradients=args.accumulate_gradients,
		checkpoint_dir=args.checkpoint_dir,
		sample_every=args.sample_every,
		sample_length=args.sample_length,
		sample_num=args.sample_num,
		multi_gpu=args.multi_gpu,
		save_every=args.save_every,
		print_every=args.print_every,
		max_checkpoints=args.max_checkpoints,
		use_memory_saving_gradients=args.use_memory_saving_gradients,
		only_train_transformer_layers=args.only_train_transformer_layers,
		optimizer=args.optimizer,
		overwrite=args.overwrite,
		restore_from=args.restore_from
		)