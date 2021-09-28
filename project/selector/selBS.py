
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


  dictBS_1_developers = {
    BS_NONE                 : True,
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_TRUNKBASED           : True,
    BS_ONEFLOWEXTENDED      : True,

    BS_CONTINUOUSINTEG      : False,
    BS_FORKINGFLOW          : False,
  }

  dictBS_1_3_developers = {
    BS_NONE                 : True,
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_TRUNKBASED           : True,
    BS_GITHUBFLOW           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,

    BS_FORKINGFLOW          : False,
  }

  dictBS_2_8_developers = {
    BS_TRUNKBASED           : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_CONTINUOUSINTEG      : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }

  dictBS_5_13_developers = {
    BS_TRUNKBASED           : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }

  dictBS_8_21_developers = {
    BS_ONEFLOWEXTENDED      : True,
    BS_CONTINUOUSINTEG      : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITHUBFLOW           : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_21_more_developers = {
    BS_ONEFLOWEXTENDED      : True,
    BS_CONTINUOUSINTEG      : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITHUBFLOW           : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_test_coverage_low = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_CONTINUOUSINTEG      : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
  }

  dictBS_test_coverage_medium = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_GITHUBFLOW           : False,
    BS_CONTINUOUSINTEG      : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
  }

  dictBS_test_coverage_high = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,
  }

  dictBS_single_version_product = {
    BS_GITHUBFLOW           : True,
  }

  dictBS_multiple_version_product = {
    BS_GITFLOW              : True,

    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_GITHUBFLOW           : False,
    BS_NONE                 : False,
  }
  
  dictBS_continuous_delivery = {
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,

    BS_GITFLOW              : False,
    BS_ONEFLOW              : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_NONE                 : False,
    BS_FORKINGFLOW          : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }



if __name__ == "__main__":

  print(BranchingStrategy.BS_SINGLEDEV)

  print(BranchingStrategy.dictNamesBS)

