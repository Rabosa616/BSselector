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

HEY WAIT! what's this flow/BS stuff?

- is this a *self-help therapy*?
- do I really need a BS?
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

about this work

- part of ERNI SERVICES
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

deliverables

- large, in-depth whitepaper
- long slides demo (mimics the WP)
- short slides demo
- annotated bibliography


---

whitepaper contents

- purpose & value
- what to choose & how
- concepts & definitions
- branching strategies list
- branching strategies types
- selection examples

---

short demo contents

- purpose & value
- what to choose & how
- micro branching strategies list
- micro branching strategies types
- selection examples

---

# purpose & value

---

about workflows and strategies

* a branching strategy (B.S.)
* ... is part of a (git) workflow
* ... the most important one


---

about workflows and strategies

* conventions between developers
* rules to store, branch, merge changes
* rules to publish and deploy ...
* conventions may feel arbitrary, inappropiate ...


---

now seriously, do I need one?

* you may not (who knows)
* will **most probably** be useful
* ... and will save time & money
* **be careful**! choosing *the wrong one*
* ... will be painful

---

git log chaos

![](images/messyLog0.gif){width=70% height=70%}


---

benefits (1)

- developers *do things* the same way
- get rid of inconsistent practices
- avoid ill-defined workflows
- have a clean & sound log history (hygiene)
- no spaghetti-like / no chaos history


---

benefits (2)

- optimize productivity
- enable parallel development
- allow planned, structured releases
- clear path for SW changes through production


---

conflicts : developers nightmare

![](images/svnmergeconflict.png){width=70% height=70%}



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

* more (?) ceremony for some operations
* integration manager may be required
* ... if none already & complex workflow
* need to train developers
* developers may need to be used to it


---

git usage

![](images/gitComplicatedXKCD.png){width=70% height=70%}


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

most relevant selection parameters

* deployment frequency
* expected (main) project duration
* application type (FW, app, web, ...)
* error tolerance in production
* single version / different-custom
* number of total developers


---

branching strategies

- none (anarchy)
- simple-man workflow
- git-flow (the most complete one)
- github-flow


---

workflow items (docs)

* provide knowledge and references about branching strategies and related stuff
* define (document) workflow policies (issue handling, branch naming, etc)

---

workflow items (VCS)

* selection of the VCS (git/svn/hg...)
* wrapper layer over the VCS (i.e. TFS/perforce over git)
* remote/in-house hosting

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

# branching strategies types


---

git-flow structure

![](images/git-flow_log.png){width=70% height=70%}


---

github-flow structure

![](images/github-flow_log.png){width=92% height=92%}


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


---

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

