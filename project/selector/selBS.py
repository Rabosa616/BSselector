
class BranchingStrategy :

  BS_UNKNOWN              = -1
  BS_NONE                 = 0
  BS_SINGLEDEV            = 10
  BS_ANARCHY              = 11
  BS_GITFLOW              = 20
  BS_GITHUBFLOW           = 21
  BS_TRUNKBASED           = 22
  BS_GITLABFLOW           = 23
  BS_ONEFLOW              = 24
  BS_CONTINUOUSINTEG      = 25
  BS_SIMPLIFIEDGITFLOW1   = 30
  BS_ONEFLOWEXTENDED      = 31
  BS_FORKINGFLOW          = 32


  dictNamesBS = {
    BS_UNKNOWN              : "UNKNOWN / N.A."                  ,
    BS_NONE                 : "NONE"                            ,
    BS_SINGLEDEV            : "Single developer"                ,
    BS_ANARCHY              : "Anarchy workflow"                ,
    BS_GITFLOW              : "git-flow"                        ,
    BS_GITHUBFLOW           : "github-flow"                     ,
    BS_TRUNKBASED           : "trunk-based development"         ,
    BS_GITLABFLOW           : "gitlab-flow"                     ,
    BS_ONEFLOW              : "one-flow"                        ,
    BS_CONTINUOUSINTEG      : "Continuous Integration"          ,
    BS_SIMPLIFIEDGITFLOW1   : "Simplified git-flow"             ,
    BS_ONEFLOWEXTENDED      : "Extended one-flow"               ,
    BS_FORKINGFLOW          : "Forking workflow (git-flow)"     ,
  }



if __name__ == "__main__":

  print(BranchingStrategy.BS_SINGLEDEV)

  print(BranchingStrategy.dictNamesBS)

