from snakemake.shell import shell

if len(snakemake.params.keys()) != 1 or not 'script' in snakemake.params.keys():
    raise Exception('Every rule using this wrapper needs'
            'to define script as one and the only keyword param.')

# script is the only keyword param, hence it will always be last
script = snakemake.params.pop(-1)

# # Would ideally do this but snakemake can't handle nested definitions in parameters
# # ie) can't define datamodule.batch_size = 128
# for key, value in snakemake.params.items(): 
#     if key != 'script': # Can't delete this from the dict for some reason
#         command += f'{key}={value} '
params_context = snakemake.__dict__.copy()
args = []
for option in snakemake.params:
    option = option.replace("{hs:", "{")
    exec(f"arg = f'{option}'", {}, params_context)
    args.append(params_context["arg"])
args = " ".join(args)

shell(f"python {script} {args}")
