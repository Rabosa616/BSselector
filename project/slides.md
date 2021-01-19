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

objective (BQ)

>  Help YOU & your TEAM CHOOSE for your project a proper:

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

<!--
  Pandoc uses fenced div for multiple columns in slide shows.
  I get the impression that DZslides is designed to create
  a slide show with a very simple, uncluttered look.
  If you are using a lot of columns, you might consider
  a different slide format.
-->

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

slide with blockquote

> a very nice blockquote

---

<!-- 2 columns

2 Columns

:::::::::::::: {.columns}
::: {.column width="50%"}

![](images/bench.jpg){width=100% height=100%}

:::
::: {.column width="50%"}

- Bullet
- Bullet
- Bullet

-->

<!-- 100% of this column, that is

:::
::::::::::::::

-->


<!--
  Pandoc uses fenced div for multiple columns in slide shows.
  I get the impression that DZslides is designed to create
  a slide show with a very simple, uncluttered look.
  If you are using a lot of columns, you might consider
  a different slide format.
-->





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


