# Hydra and Snakemake
[![hydra](https://img.shields.io/badge/-Hydra_1.3-89b8cd&logoColor=white)](https://hydra.cc/)
[![snakemake](https://img.shields.io/badge/-Snakemake_8.3.2-039475)](https://snakemake.readthedocs.io/)

Very often we build our ML jobs such that they are configured by Hydra, and this is nice for quick development of projects. But this becomes a problem when you want to integrate this into a workflow management system like Snakemake.

This repo is trying to develop a wrapper such that Hydra and Snakemake can play nice together without needing to modify how existing scripts (completely configured with hydra) are written and called. 

The proposed solution is to modify the params filed of such Snakemake rules such that they contain Hydra 

```
rule all:
    input:
        "output1.txt",
        "output2.txt",

rule get_data:
    input:
        model = "dummy.txt"
    output:
        output_file = "output{i}.txt"
    params:
        "datamodule.batch_size={i}",
        "model.ckpt_path={input.model.split('.txt')[0]}/{output.output_file}",
        script = "scripts/train.py"
    wrapper:
        "file:hydra_cli"
```

TODO check this in deployed setting across jobs and once settled on a good enough set up push to the snakemake wrappers repo.
