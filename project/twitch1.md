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

about this work

- part of my ERNI (career path) masterpiece
- something I wanted to know about
- performed guided search & read
- this presentation +
- ... detailed, in-depth document
- ... annotated bibliography
- ... BS selector tools

---


about me @ERNI

- joined ERNI as senior 4+ years ago
- worked for HP ever since
- printer FW developer (C++, linux)
- HP multiplatform library (C++)
- HP common platform developer (DUNE)


---

about me with VCSs

- always been interested in VCSs, even when not available (no internet)
- happy to discover SCCS (GUI in sun's solaris), disgusted about Microsoft's SS
- very happy when found out about SVN (unlike Linus Torvalds)
- lucky to have never used CVS (worse than its simple predecessor RCS)
- DVCSs: tried Ubuntu's bzr (bazaar), though never tried mercurial (hg)
- tried git in the beginning, didn't understand anything
- tried git again when hype, and liked it so much, started to use it over SVN
- using git *officially* only since May 2021


---

about me with VCSs #2

- 2005: convinced management (and colleagues) at my former company to:
- use SVN, and ...
- replace existing inferior solutions
- despite not being a _salesman_ (quite the opposite)


---

objective:

- present ERNI-services's BS selector
- provide knowledge about BS & gWF and underlying concepts
- understand why they are (or not) useful
- help you decide if you need one (or not!)
- help you decide the most suited for YOUR project
- decide with awareness (not blindly or inertia or prejudice)


---

target audience

- managers (have the last word)
- product owners
- SW architects
- project managers
- devops engineers (know more than me!)
- agile masters?
- ... and developers


---

contents (general)

- ... only at introductory level (devops engineers know more than me!)
- definition of branching pattern, branching strategy, git workflow
- benefits (& costs) of gWF & BS
- list and description of some of them
- list of branching patterns
- merge conflicts, solving vs minimizing


---

contents, concepts determining which BS to choose

- about integration of developers work
- about BS strategy
- related to deployment & releasing
- CI/CD (devops only?)
- testing & - error tolerance
- etc ... (some contents are self-provided)


---

# git workflows & branching strategies

---

about workflows and strategies

* a branching strategy (B.S.)
* ... is part of a (git) workflow
* ... the most important one


---

# definitions (gWF, BS, BP)

---

about workflows and strategies

* conventions between developers
* rules to store, branch, merge changes
* rules to publish and deploy ...
* conventions may feel arbitrary, inappropiate ...


---

branching patterns / branching strategies

* a branching pattern is a way of sharing/integrating developer changes
* a branching pattern is a way of managing the path to production / deployment
* a branching strategy is a set of branching patterns


---

# benefits & costs of gWF & BS

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
- no spaghetti-like / chaotic history


---

benefits (2)

- optimize productivity
- enable parallel development
- allow planned, structured releases
- have a clear path for SW changes through production


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
* integration manager may be required (if none already)
* need to train developers
* developers may need to be used to it


---

# basic concepts

---

what is a commit?


---

merge vs rebase?


---

