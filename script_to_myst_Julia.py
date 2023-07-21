import os
import shutil

import sys
sys.stdout.reconfigure(encoding='utf-8')

root_src_dir = './source_code/'
root_dst_dir = './juliabook/'

shutil.copytree(root_src_dir, root_dst_dir, dirs_exist_ok=True)

#import script_to_myst_Julia as jlscript

def remove_files(root_src_dir, root_dst_dir):
    for file in os.listdir(root_src_dir):
        if os.path.isfile(os.path.join(root_src_dir, file)):
            os.remove(os.path.join(root_dst_dir, file))
        else:
            shutil.rmtree(os.path.join(root_dst_dir, file))

header = """---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Julia
  language: julia
  name: julia-1.9
---

(getting_started)=
```{raw} html
<div id="qe-notebook-header" style="text-align:right;">
        <a href="https://quantecon.org/" title="quantecon.org">
                <img style="width:250px;display:inline;" src="https://assets.quantecon.org/img/qe-menubar-logo.svg" alt="QuantEcon">
        </a>
</div>
```
"""

contents = """
```{contents} Contents
:depth: 2
```
"""
chapter_meta = {
                "introductions": {
                    "name": "Introductions",
                    "subs": [
                    "two_period_job_search.jl",
                    "compute_spec_rad.jl",
                    "power_series.jl",
                    "s_approx.jl",
                    "linear_iter.jl",
                    "linear_iter_fig.jl",
                    "iid_job_search.jl"
                    ]
                },
                "operators_fixed_points": {
                    "name": "Operators and Fixed Points",
                    "subs": [
                    "lake.jl",
                    #"lake_1.jl"
                    ]
                },
                "markov_dynamics": {
                    "name": "Markov Dynamics",
                    "subs": [
                    "inventory_sim.jl",
                    "is_irreducible.jl",
#                    "inventory_sim.jl",
                    "laborer_sim.jl",
                    "markov_js.jl",
                    "markov_js_with_sep.jl"
                    ]
                },
                "optimal_stopping": {
                    "name": "Optimal Stopping",
                    "subs": [
                    "firm_exit.jl",
                    "american_option.jl"
                    ]
                },
                "markov_decision_processes": {
                    "name": "Markov Decision Processes",
                    "subs": [
                    "inventory_dp.jl",
                    "finite_opt_saving_0.jl",
                    "finite_opt_saving_1.jl",
                    "finite_opt_saving_2.jl",
                    "finite_lq.jl",
                    "firm_hiring.jl",
                    "modified_opt_savings.jl"
                    ]
                },
                "stochastic_discounting": {
                    "name": "Stochastic Discounting",
                    "subs": [
                    "plot_interest_rates.jl",
                    #"plot_interest_rates_real.jl",
                    "pd_ratio.jl",
                    "inventory_sdd.jl"
                    ]
                },
                "nonlinear_valuation": {
                    "name": "Nonlinear Valuation",
                    "subs": [
                    "rs_utility.jl",
                    "ez_utility.jl"
                    ]
                },
                "recursive_decision_processes": {
                    "name": "Recursive Decision Processes",
                    "subs": [
                    "quantile_function.jl",
                    "quantile_js.jl"
                    ]
                }
                }

pkg = """```{code-cell} julia-1.9
:tags: [\"remove-cell\"]
using Pkg;
Pkg.activate(\"../\");

using PyCall;
pygui(:tk);
```
"""

#try:
for chapter in chapter_meta.keys():
    chapter_name = chapter_meta[chapter]["name"]
    chapter_subs = chapter_meta[chapter]["subs"]

    with open(f"./juliabook/{chapter}.md", "w", encoding='utf-8') as b:
        b.write(header)
        b.write(f"# {chapter_name}\n\n")
        b.write(contents)
        b.write("\n\n")

        b.write(pkg)

        b.write("\n")

        for sub in chapter_subs:
            
            b.write(f"#### {sub}\n")
            b.write(f"```{{code-cell}} julia-1.9\n")
            b.write(":tags: [\"hide-input\"]\n")

            with open(f"./juliabook/{sub}", "r", encoding='utf-8') as g:
                text = g.read()
                b.write(text)
            
            
            b.write(f"\n```\n\n")

    b.close()
            
    #return True
#except Exception as e:
    #print("Error in create_myst_nb(): " + str(e))
    #remove_files(root_src_dir, root_dst_dir)
    #print("Failed! - Directory cleaned")
    #return False

#try:
os.system("jupyter-book build juliabook/")
remove_files(root_src_dir, root_dst_dir)
    #print("Success!")
#exit(0)
#except Exception as e:
    #print("Error in create_myst_nb(): " + str(e))
    #remove_files(root_src_dir, root_dst_dir)
    #print("Failed! - Directory cleaned")
    #exit(1)
    
shutil.copytree("./juliabook/_build/html/", "./docs/", dirs_exist_ok=True)

