% branching strategy selector
% Marc Gonzalez-Carnicer
% February 2021

---

objective

```
    Help YOU & your TEAM
    CHOOSE for your project
    a proper:
```

- (git?) workflow &
- branching strategy


---

HEY WAIT! what's this flow BS stuff?

- is this a *self-help therapy*?
- do I really need BS?
- can't I do without? (as usual)
- *how much* does this cost?
- what do I get/avoid *in return*?

---

been here before?

<!-- vertical column with picture last-to-commit -->

:::::::::::::: {.columns}
::: {.column width="50%"}

![](images/avoidConflict.jpg){width=55% height=55%}

:::
::: {.column width="50%"}

avoiding merge conflicts

<!-- 100% of this column, that is -->

:::
::::::::::::::

---

contents

- purpose & value
- what to choose & how
- concepts & definitions
- branching strategies list
- branching strategies types
- selection examples

---

about this work

- something I wanted to know about
- performed guided search & read
- this presentation +
- ... detailed, in-depth document
- ... annotated bibliography

---

about me @ERNI

- joined ERNI as senior 4 years ago
- worked for HP ever since
- printer FW developer (C++, linux)
- HP multiplatform library (C++)
- likes *playing* with VCSs
- mostly used svn (git over svn)

---

# purpose & value

---

about workflows and strategies

* conventions between developers
* how to store, branch, merge changes
* how to publish and deploy ...
* a B.S. is part of a (git) workflow
* the most important one


---

now seriously, do I need one?

* you may not (who knows)
* will **most probably** be helpful
* ... and will save time & money
* **be careful**! choosing *the wrong one*
* ... will be painful

---

git log chaos

![](images/messyLog0.gif){width=70% height=70%}


---

benefits

- developers *do things* the same way
- get rid of inconsistent practices
- avoid ill-defined workflows
- have a clean & sound log history
- no spaghetti-like / chaos history

---

benefits (merging)

- avoid / minimize *merge conflicts*
- minimize conflicts **complexity**
- reduce time when *publishing*

---

benefits (general)

```
    having a proper branching strategy
    => save 20%-40% in developer time

    choose a proper one
      in less than 1 hour
    (with this work)
```

---


cost

* more ceremony for some operations
* integration manager may be required (if none already)
* need to train developers
* developers may need time to be used to new workflow


---



# what to choose & how

---

what to choose

* a branching strategy
* (as part of) a git workflow


---

how to choose

* based on selection parameters
* listed by type (presentation - here)
* listed by relevance order (doc)

---

selection parameters (quantitative)

* expected (main) project duration
* number of long-lived branches
* number of total developers
* number of teams
* number of projects

---

selection parameters (code type)

* application type (FW, app, web, ...)
* existing code base size (0?)
* existing code repos
* single version / different-custom

---

selection parameters (deployment)

* deployment frequency
* CI/CD: integration strategy(ies)
* CI/CD: deployment strategy(ies)
* releasing strategy(ies)
* testing strategy / testing coverage
* error tolerance in production

---

selection parameters (people)

* remote team? part time?
* overall git team experience
* team collaboration style
* personal habits (and prejudices)
* corporate policies (and managers/"gurus" prejudices)

---

most relevant selection parameters

* deployment frequency
* expected (main) project duration
* application type (FW, app, web, ...)
* error tolerance in production
* single version / different-custom
* number of total developers


---

branching strategies (1/3)

- none (anarchy)
- simple-man workflow
- git-flow (the most complete one)
- github-flow


---

branching strategies (2/3)

- gitlab-flow
- one-flow
- trunk-based development
- continuous integration (not in the CI-CD meaning)


---

branching strategies (3/3)

- simplified git-flow
- centralized workflow
- one-flow plus
- ...


---

workflow items (docs)

* provide knowledge and references about branching strategies and related stuff
* define (document) workflow policies (issue handling, branch naming, etc)

---

workflow items (VCS)

* selection of the VCS (git/svn/hg...)
* wrapper layer over the VCS (i.e. TFS over git)

---

workflow items (VCS style)

* when to merge or rebase
* when & where to squash
* commit message style and content

---

workflow items (tools/methods)

* automatic versioning tool (gitversion)
* code review method (pull request?)
* appointment (or not) of an integrator (release / branching manager)
* ...

---

workflow items

* no need to implement them all
* most of them B.S.-independent


---

VCS selection

* git almost always assumed
* but others not discarded (svn, hg...)
* possible to use _git workflows_ without git


---

# concepts & definitions

---

concepts & definitions

* VCS-related concepts
* deployment
* branching
* ...


---

VCS basics

* commit
* repository & working copy
* branch

---

branching / merging

* branching vs merging
* merging / reintegrating
* pull-request
* rebase


---

conflicts

* merging conflicts
* change frequency

---

conflicts

![](images/svnmergeconflict.png){width=70% height=70%}


---

git knowledge

* how to pull, fetch, push
* how to merge
* how to rebase
* how to reflog
* ...


---

deploy/release strategies

* deployment strategies
* release strategies


---

flexible branching strategy

* projects have different phases
* time to change B.S.?

---

types of branches

* hotfix branch
* release branch
* long-lived release branch
* environment branch
* maturity branch
* experimental branch
* future branch
* collaboration branch
* team-integration branch

---


# branching strategies list


---

NONE (no B.S.)

* simplest
* anarchy
* may be OK (or not)


---

simple-guy

* just commit
* no branches
* (almost) no pull


---

git-flow

* _complex_ reputation
* 2 stable, 2 stable long-lived branches
* releases, bugfixes ...

---

git-flow structure

![](images/git-flow_log.png){width=70% height=70%}


---

github-flow


* much simpler than git-flow
* used for continous deployment
* _master_ must be stable (deployable)

---

github-flow structure

![](images/github-flow_log.png){width=92% height=92%}


---


one-flow

* 1 stable branch
* new changes/features are rebased to the latest stable
* allows feature, hotfix, release branches
* claims to be much simpler but equally powerful as git-flow


---

gitlab-flow

* 11 rules, related to the VCS
* rules also about testing and deployment
* intermediate branches (production and staging)
* emphasizes testing & CI-CD (automatic deployment)

---

continuous-integration

* (not as in CI-CD!)
* emulates everybody works on the same files
* must commit and share at least once a day
* focus on merging conflicts minimiztion


---

trunk-based development

* similar to continuous integration
* allows short-lived feature branches
* allows release branches


---

subversion-like development

* branches/releases/tags folders
* centralized work


---

# branching strategies types


---

complex

* git-flow
* none (anarchy)
* gitlab-flow (sometimes)

---

feature-driven

* gitlab-flow
* one-flow

---

continuous delivery oriented

* github-flow
* gitlab-flow
* continuous integration
* trunk-based development


--------------------------------------------

several products/versions

* git-flow


---

only 1 product

* one-flow
* gitlab-flow
* gitlab-flow


---

low test coverage

* git-flow
* gitlab-flow

---

high test coverage

* github-flow


---

# selection examples

---

example #1

- long project duration
- 7-15 developers
- 3 teams
- existing codebase
- must maintain several products/customers
- low test coverage

---

example #1 selection

* B.S. #1 : git-flow
* B.S. #1 : one-flow (not really)
* github-flow : NO!


---

example #2

- must deliver soon
- 3 dev / 1 team
- no existing codebase
- only 1 version
- high test coverage

---

example #2 selection

* B.S. #1 : github-flow
* B.S. #2 : gitlab-flow
* B.S. #3 : one-flow
* git-flow : NO!


---

# thank you

