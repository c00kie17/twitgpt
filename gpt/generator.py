import gpt_2_simple as gpt2


if __name__ == '__main__':
	sess = gpt2.start_tf_sess()
	gpt2.load_gpt2(sess, run_name='run1')
	result = gpt2.generate(sess,
              length=280,
              temperature=1.4,
              prefix="<|startoftext|>",
              truncate="<|endoftext|>",
              nsamples=20,
              batch_size=10,
              include_prefix=False,
              return_as_list=True
              )
	print(result)