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

- is this a _self-help therapy_?
- do I really need a BS?
- can't I do without? (as usual)
- _how much_ does this cost?
- what do I get/avoid _in return_?


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

about me with VCSs (Version Control Systems)

- always been interested in VCSs, even when not available (no internet)
- happy to discover SCCS (GUI in sun's solaris), disgusted about Microsoft's SS
- very happy when found out about SVN (unlike Linus Torvalds)
- lucky to have never used CVS (worse than its simple predecessor RCS)
- DVCSs: tried Ubuntu's bzr (bazaar), though never tried mercurial (hg)
- tried git in the beginning, didn't understand anything
- tried git again when hype, and liked it so much, started to use it over SVN
- using git _officially_ only since May 2021


---

about me with VCSs #2

- 2005: convinced management (and colleagues) at my former company to:
- use SVN, and ...
- replace existing inferior solutions
- despite not being a _salesman_ (quite the opposite)


---

target audience

- managers (have the last word)
- product owners
- SW architects
- project managers
- agile masters?
- NOT FOR devops engineers (know more than me :) !)
- ... and developers


---

objective:

- present ERNI-services's BS selector
- provide _beginner level_ knowledge about BS & gWF and underlying, related concepts
- understand why they are (or not) useful
- help you decide if you need one (or not!), and the MOST suited
- decide with _awareness_ (not blindly or with inertia / prejudice)
- _humbly_ provide tips on using VCSs and BSs (I am sure you know or heard of most of the covered topics)


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

# git workflows & branching strategies, patterns

---
abbreviations

* BS: Branching Strategy
* gWF: (git) WorkFlow -- not only with git!
* VCS: Version Control System (like svn, git, ...)
* D-VCS / DVCS: Distributed VCS (git, hg, bzr, ...)


---

about workflows and strategies

* a branching strategy (BS)  
* ... is part of a (git) workflow
* ... the most important one


---

branching patterns / branching strategies

* a branching pattern is a way of sharing/integrating developer changes
* a branching pattern is a way of managing the path to production / deployment
* a branching strategy is a set of branching patterns (maybe only 1)


---

git workflows and strategies

* conventions between developers
* rules to store, branch, merge changes
* rules to publish and deploy ...
* conventions may feel arbitrary, inappropiate ...


---

# benefits & costs of gWF & BS

---

now seriously, do I need one?

- are these BS just _hype_?
- you may not (who knows)
- will __most probably__ be useful
- ... and will save time & money
- __be careful!__ choosing _the wrong one_
- ... will be painful


---

git log chaos

![](images/messyLog0.gif){width=70% height=70%}


---

benefits (1)

- developers _do things_ the same way
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

benefits (merging-related)

- avoid / minimize amount of _merge conflicts_
- minimize conflicts __complexity__
- reduce time when _publishing_


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

* more ceremony/bureaucracy for some operations (maybe)
* integration / release manager may be required (if none already)
* may need to train / educate developers
* developers may need some time to be adapt to it

---

git training

- even if people use layers above git (github/bitbucket/gitlab, Teams Foundation Server, gitflow plugins ...), it's convenient that the team is decently trained on raw git usage for the basic operations (pull, fetch, push, reset, merge, rebase, reflog, etc)

![](images/gitComplicatedXKCD.png){width=70% height=70%}

---

# basic concepts

---

what is a commit?

- commits have different meanings / actions depending on the VCS
- in SVN: store + share + publish
- in git: store only
- git encourages committing often / svn not


---

what is a branch?

- different VCSs have different meanings or uses for a branch
- humans think of a branch as in a tree (bifurcation)
- in svn, a branch copies (cheaply) the files
- in git, a branch is simply a label of a history you don't want to lose, but it is not required to explicitly use them
- here, we'll use the _human_ meaning

![](images/treebranches.jpg){width=40% height=40%}

---

branching is easy

- in all VCSs, branching is easy
- integrating is the __tough__ part
- in SVN, _merging_ is not really efficient (design limitation)


---

merge vs rebase?

Reminder of these 2 ways of integrating changes.

![](images/mergeVSrebase.png){width=40% height=40%}

---


# merge conflicts

---

survey

- how often / when do you update/pull?
- how often / when do you commit/backup?
- how often / when do you share/publish (push)?
- answers like every week / day / twice a day / hour / several times an hour


---

updating too frequently?

![](images/updateFrequently.jpg){width=55% height=55%}


---

probability of merge conflicts

- depends on:
- integration frequency
- codebase size
- location / distribution of tasks in the code


---

integration frequency

- difficult to quantificate (what does _frequent_ mean in terms of tmie?)
- depends on several factors

---

codebase size


---

distribution of tasks in the code

- if developers work on different locations, no matter how frequent or large codebase
- new feature / module
- release manager (or the group) ensure people do not work on the same module / files

---

merge conflicts

---

sounds familiar?

![](images/svnmergeconflict.png){width=70% height=70%}

- in SVN you can't even commit if somebody has modified the same file (in a different place)
- in GIT you can't push without fetch/pull in the same branch

---

types of merge conflicts

- textual conflict
- painful textual conflict : many changes, impossible to process by diff viewers
- semantic conflict (NOT DETECTED) : VERY DANGEROUS - example: rename method, other dev adds call to old method name - it builds!

---

avoid banal merge conflicts

- enforce text style before commits (so people don't feel tempted to make unrelated changes)
- write tidy code: EOL whitespace, indentation, TAB/blanks consistency, fileformat (DOS/unix), ... there are tools for that


---

zero conflicts trick, only for you


![](images/avoidConflict.jpg){width=55% height=55%}


---

minimize merge conflicts

- the _zero conflicts trick_ should be intentionally avoided at all costs
- _high-tech_ & _revolutionary_ trick: use your _soft skills_ and TALK! before the commit, but also before developing the change: first smallest / simplest change (less probability of hard to solve merge conflicts)
- use peer review to keep colleagues informed on what you have done (not only for reviewing the code)
- use the proper branching pattern acordingly


---

# branching patterns (integration)

---

Let's take a look at the most relevant branching patterns related to integration (sharing developers work):

- mainline
- feature branch
- release branch


---

mainline integration

- work without branches
- in practice, it does not exist (every single sandbox is a branch by itself)


---

Let's take a look at the most relevant branching patterns related to integration (sharing developers work):

- mainline
- feature branch
- release branch



---

mainline

- no branches
- very simple
- everybody has used it some time


---

feature branch

- parallel, isolated development for a new feature
- variants: allow or not to update from main branch (usually not)


---

continuous integration

- highly collaborative
- simulates developers work on the same set of files / folders
- share / integrate continuously
- reduces probability of merge conflicts


---


---

# THE.BEST.ONE

---

what is the best one?

- some people just want to use the same BS always
- some people think a given BS is the best one, and suits all kind of projects
- 

---

Martin Fowler's opinion

- (I have quoted from his web page https://martinfowler.com/articles/branching-patterns.html)
- most influential developers (chief scientist at thoughtworks)
- author and board member of agile technologies
- advocated XP (eXtreme Programming) in the late '90s with Kent Beck
- he strongly recommends to use _Continous Integration_ (simulate working on same set of files, sharing work / integrating very often)
- reason: minimize merge conflicts
- I beg to disagree with him: use it some times, but depends on development phase
- depends if work related or not, how large is the codebase


---

my opinion

* play as a team, bein always consistent, without anarchy
* start with something simple (use BS selector)
* be flexible: feel free to adapt / change if required (all together)

---






---

conclusion

- (define,) agree & use a branching strategy 
- choose the proper one with awareness, or use ERNI's selector if no time
- be open & ready to change / adapt
- to minimize merge conflicts, use agile (daily) meetings to inform of upcoming refactors & commits


---


