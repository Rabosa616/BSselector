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

- branching strategy (BS)
- & a git workflow


---

HEY WAIT! what's this 'flow' stuff?

- is this a *self-help therapy*?
- do I really need a BS?
- can't I do without? (as usual)
- *how much* does this cost?
- what do I get/avoid *in return*?

---

about this work

- target audience: PMs / architects
- requested by SERVICES dpt (ERNI)
* services wants it available in github
* considering a video pill / streaming


---

about me @ERNI

- joined ERNI as senior 4 years ago
- worked for HP ever since
- helped in a Roche bid (architect)
- printer FW developer (C++, linux)
- HP multiplatform library (C++)
- likes *playing* with VCSs


---

deliverables

- long, in-depth whitepaper
- whitepaper, slides version
- annotated bibliography
- this presentation


---

presentation contents

- purpose & value
- what to choose & how
- micro BS list & types
- selection examples

---

whitepaper contents

- purpose & value
- what to choose & how
- concepts & definitions
- git workflow items
- branching strategies list
- branching strategies types
- selection examples

---

---

# purpose & value

---

about workflows and BS (1)

* a branching strategy (BS)
* ... is the most important part
* ... of a (git) workflow


---

about workflows and BS (2)

* conventions between developers
* store & track code changes
* branch (new task) & merge (join)
* publish & deploy


---


protocol branch / merge

<!-- vertical column with picture last-to-commit -->

:::::::::::::: {.columns}
::: {.column width="50%"}

![](images/protocolCheckList.png){width=75% height=75%}

:::
::: {.column width="50%"}

![](images/branch-merge.png){width=75% height=75%}

<!-- 100% of this column, that is -->

:::
::::::::::::::


---

conventions for what?

* work isolated / share work often
* publishing strategy
* versioning strategy (automatic?)

---

sharing styles

:::::::::::::: {.columns}
::: {.column width="50%"}

![](images/isolated.png){width=55% height=55%}

:::
::: {.column width="50%"}

![](images/interaction.png){width=55% height=55%}

<!-- 100% of this column, that is -->

:::
::::::::::::::

---

release frequency

:::::::::::::: {.columns}
::: {.row width="50%"}

![](images/relOften.png){width=25% height=25%}

:::
::: {.row width="50%"}

![](images/relRare.png){width=25% height=25%}

<!-- 100% of this column, that is -->

:::
::::::::::::::

---

now seriously, do I need one?

* you may not (who knows)
* will **most probably** be useful
* ... and will save time & money
* **be careful**! choosing *the wrong one*
* ... will be painful

---

benefits (project manager)

* choose a BS, reliably & effortless
* save days reading and asking
* don't pick a wrong one

---

benefits (project)

- no inconsistent practices
- all developers work *the same way*
- clean & sound log history (hygiene)
- avoid / minimize *merge conflicts*


---

git log chaos

![](images/messyLog0.gif){width=70% height=70%}


---

avoiding merge conflicts

<!-- vertical column with picture last-to-commit -->

:::::::::::::: {.columns}
::: {.column width="50%"}

![](images/avoidConflict.jpg){width=55% height=55%}

:::
::: {.column width="50%"}

been here before? sounds familiar?

<!-- 100% of this column, that is -->

:::
::::::::::::::

---

benefits (company)

* have a well-organized team
* reduce time waste / people stress
* maximize productivity
* save 20%-40% in developer time


---

cost / investment

* performed guided search & read
* ++ ceremony for some operations
* integration manager required?
* (... if complex workflow)
* need to train developers
* developers: get used


---

masterpiece plan

* finish whitepaper (2 weeks)
* cuanto cuesta implementar o desarrollar
* services le va a dar visibilidad
* involved people
* EDD, video pill / streaming
* available at github



---

---

# what to choose & how

---

what to choose (output)

* a branching strategy (BS)
* (as part of) a git workflow


---

how to choose (inputs)

* based on selection parameters
* qualitative & quantitive questions
* easy to find out answers

---

most relevant selection parameters

* deployment frequency
* expected (main) project duration
* application type (FW, app, web, ...)
* error tolerance in production
* single version / different-custom
* number of developers / teams


---

my contribution (whitepaper)

* not just copy & paste:
* encourage flexibility (change BS?)
* best tool: people communication


---

# any questions?

better ask ... ME!

---

---

# BS list & types


---

branching strategies

- none (anarchy)
- git-flow (the most complete one)
- github-flow
- trunk-based development
- one-flow
- ...


---

workflow items (docs)

* document workflow policies
* issue handling, branch naming
* join work style (merge or rebase)
* releasing policy
* many more (NOT required to use all)


---

git-flow structure

![](images/git-flow_log.png){width=70% height=70%}


---

github-flow structure

![](images/github-flow_log.png){width=92% height=92%}


---

branching strategies types

* complexity / simplicity
* continuous delivery oriented
* several products-versions / single
* test coverage


---

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

* BS #1 : git-flow
* BS #1 : one-flow (not really)
* github-flow : NO!


---

example #2

- must deliver frequently
- 3 dev / 1 team
- no existing codebase
- only 1 version
- high test coverage

---

example #2 selection

* BS #1 : github-flow
* BS #2 : gitlab-flow
* BS #3 : one-flow
* git-flow : NO!



# thank you

