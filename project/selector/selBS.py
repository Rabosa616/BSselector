
class BranchingStrategy :

  BS_UNKNOWN              = -1
  BS_NONE                 = 0
  BS_SINGLEDEV            = 10
  BS_ANARCHY              = 11
  BS_GITFLOW              = 20
  BS_GITHUBFLOW           = 21
  BS_GITLABFLOW           = 22
  BS_ONEFLOW              = 22
  BS_SIMPLIFIEDGITFLOW1   = 30


  dictNamesBS = {
    BS_UNKNOWN              : "UNKNOWN"             ,
    BS_NONE                 : "NONE"                ,
    BS_SINGLEDEV            : "SINGLEDEV"           ,
    BS_ANARCHY              : "ANARCHY"             ,
    BS_GITFLOW              : "GITFLOW"             ,
    BS_GITHUBFLOW           : "GITHUBFLOW"          ,
    BS_GITLABFLOW           : "GITLABFLOW"          ,
    BS_ONEFLOW              : "ONEFLOW"             ,
    BS_SIMPLIFIEDGITFLOW1   : "SIMPLIFIEDGITFLOW1"  ,
  }



if __name__ == "__main__":

  print(BranchingStrategy.BS_SINGLEDEV)

  print(BranchingStrategy.dictNamesBS)

