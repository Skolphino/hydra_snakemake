from snakemake.shell import shell

params = snakemake.params
if not hasattr(params, 'script'):
    raise Exception('Every rule using this wrapper needs to define script under params.')
script = params['script']
command = f'python {script} '
# # Would ideally do this but snakemake can't handle nested definitions in parameters
# # ie) can't define datamodule.batch_size = 128
# for key, value in snakemake.params.items(): 
#     if key != 'script': # Can't delete this from the dict for some reason
#         command += f'{key}={value} '
for cmnd in snakemake.params[:-1]:
    for opt in ['input.', 'output.', 'params.', 'wildcards.']:
        if opt in cmnd:
            cmnd = cmnd.replace(opt, f'snakemake.{opt}')
    cmnd = eval(f'f"""{cmnd}"""')
    command += f'{cmnd} '
shell(command)
# # Not sure how else to debug except to print the command
# print(command)
# shell(f'touch {snakemake.output}')
