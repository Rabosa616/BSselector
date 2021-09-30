# Branching Strategy Selector project

This repo contains the code of the ERNI-services git workflow &amp; Branching Strategy Selector (BSS). It allows to choose a Branching Strategy for a project according to its peculiarities. These peculiarities are used as selection parameters of the script, providing as output 1 or more suitable BSs, while highlighting which ones are not suitable (rejected).

# the script

The BSS is currently a script that takes some command line parameters as inputs and as output suggests 1 or more BS. It also highlights which BSs are not aproppiate according to the input data.

It is expected that the script (or a port of it) is integrated as engine on a web page. But this is for the future.

## how to use it

The script is self-documented. If called without parameters, displays the available Branching Strategies as outputs. It suggests the user to use the -h option to display the usage options. Like this:

```
python3 ./selBS.py -h

Usage: selBS.py [-h|--help] [-s|--select=<list of comma-separated selectors>] [-l|--list-selectors=<pattern>]

Example: selBS.py # display the available branching strategies
Example: selBS.py --select=5_13_developers,multiple_version_product
Example: selBS.py --list-selectors=coverage]
Example: selBS.py --list-selectors=ALL
```

The `--list-selectors` option allows the user to display all the allowed selecting options. It accepts the _ALL_ keyword to display all of them, otherwise by entering a text will display all the selections options that contain it. That is useful to search.

The `--select` option is used to enter the selecting keywords (as displayed by the `--list-selectors` option) that the user wants to use. These keywords have to be comma-separated without blanks.

## examples

Follow some usage examples:

```
$ python3 ./selBS.py -l developers
list of available Branching Strategies selectors:
filtering by : developers
['1_developers',
 '1_3_developers',
 '2_8_developers',
 '5_13_developers',
 '8_21_developers',
 '21_more_developers']
total available filters = 6
$
$ python3 ./selBS.py -s 5_13_developers,test_coverage_low,2_more_subteams_or_projects,maintain_multiple_version_product,long_project_life
selector '5_13_developers' added successfully 
selector 'test_coverage_low' added successfully 
selector '2_more_subteams_or_projects' added successfully 
selector 'maintain_multiple_version_product' added successfully 
selector 'long_project_life' added successfully 
total selectors added = 5
====
list of rejected BS:
-- BS id#31 : (score=-2) Extended one-flow
-- BS id#25 : (score=-3) Continuous Integration
-- BS id#22 : (score=-3) trunk-based development
-- BS id#21 : (score=-4) github-flow
-- BS id#11 : (score=-4) Anarchy workflow
-- BS id#10 : (score=-4) Single developer
-- BS id#0 : (score=-4) NONE
list of final selected BS:
-- BS id#20 : (score=5) git-flow
-- BS id#32 : (score=5) Forking workflow (git-flow)
-- BS id#24 : (score=4) one-flow
-- BS id#23 : (score=3) gitlab-flow
-- BS id#30 : (score=2) Simplified git-flow
$
$ python3 ./selBS.py -s 1_3_developers,deploy_very_frequently,single_version_product,test_coverage_high
selector '5_13_developers' added successfully 
selector 'test_coverage_low' added successfully 
selector '2_more_subteams_or_projects' added successfully 
selector 'maintain_multiple_version_product' added successfully 
selector 'long_project_life' added successfully 
total selectors added = 5
====
list of rejected BS:
-- BS id#31 : (score=-2) Extended one-flow
-- BS id#25 : (score=-3) Continuous Integration
-- BS id#22 : (score=-3) trunk-based development
-- BS id#21 : (score=-4) github-flow
-- BS id#11 : (score=-4) Anarchy workflow
-- BS id#10 : (score=-4) Single developer
-- BS id#0 : (score=-4) NONE
list of final selected BS:
-- BS id#20 : (score=5) git-flow
-- BS id#32 : (score=5) Forking workflow (git-flow)
-- BS id#24 : (score=4) one-flow
-- BS id#23 : (score=3) gitlab-flow
-- BS id#30 : (score=2) Simplified git-flow
$
```
The output of the script is pretty understandable, listing which BSs are suitable for the selected input parameters, and which ones are not. These lists are sorted by relevance (score).


