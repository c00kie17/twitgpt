import gpt_2_simple as gpt2
import argparse

def get_args():
       parser = argparse.ArgumentParser(description='Generating snippets from trained data')
       parser.add_argument('--run_name', help='name of the run you want to generate text from', required=True)
       parser.add_argument('--checkpoint_dir', metavar='PATH',default='./checkpoint', help='The directory to load checkpoints from')
       parser.add_argument('--models_dir',metavar='PATH', help='name of the directory where the model are loaded from ', default='./models')
       parser.add_argument('--model_name',metavar='MODEL', help='name of the model the run was trained on 124M,355M,774M,1558M', required=True)
       parser.add_argument('--return_as_list',type=bool,default=False, help='If the genereated result should return as a list')
       parser.add_argument('--truncate',default=None, help='an end of sample delimiter')
       parser.add_argument('--destination_path',metavar='PATH',default=None, help='a path to save your generated text')
       parser.add_argument('--prefix',default=None, help='a start of sample delimiter')
       parser.add_argument('--seed',default=None, help='Integer seed for random number generators, fix seed to reproduce results')
       parser.add_argument('--nsamples',default=1,metavar='N',type=int, help=' Number of samples to return total')
       parser.add_argument('--batch_size',default=1,metavar='SIZE',type=int, help='Number of batches (only affects speed/memory).  Must divide nsamples.')
       parser.add_argument('--length',default=1023,metavar='TOKENS',type=int, help='Number of tokens in generated text')
       parser.add_argument('--temperature',default=0.7,type=float, help='Float value controlling randomness in boltzmann distribution. Lower temperature results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Higher temperature results in more random completions.')
       parser.add_argument('--top_k',default=0,type=int, help='N Integer value controlling diversity. 1 means only 1 word is considered for each step (token), resulting in deterministic completions, while 40 means 40 words are considered at each step. 0 (default) is a special setting meaning no restrictions. 40 generally is a good value.')
       parser.add_argument('--top_p',default=0.0,type=float, help='The probibility to control sampling of token, this helps us preserve variety when the highest scoring tokens have low confidence,setting this to 0.0 will take all the tokens possible and select the highest scoring one')
       parser.add_argument('--include_prefix',default=True,type=bool, help='if the generated text should have prefixes')
       return parser.parse_args()

if __name__ == '__main__':
       args = get_args()
       sess = gpt2.start_tf_sess()
       gpt2.load_gpt2(sess, run_name=args.run_name)
       results = gpt2.generate(sess,
              run_name=args.run_name,
              length=args.length,
              temperature=args.temperature,
              prefix=args.prefix,
              truncate=args.truncate,
              nsamples=args.nsamples,
              batch_size=args.batch_size,
              include_prefix=args.include_prefix,
              return_as_list=args.return_as_list,
              checkpoint_dir=args.checkpoint_dir,
              model_dir=args.models_dir,
              destination_path=args.destination_path,
              seed=args.seed,
              top_k=args.top_k,
              top_p=args.top_p,
              )
       for result in results:
              print(result)
              print("=================================================")