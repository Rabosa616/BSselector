
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


  def __init__(self) :

    self.listSelectorDicts = []

    self.dictSelectedBS = {}
    self.dictRejectedBS = {}
    self.listFinalBS = []


  def addSelector(self, addedSelectorDict) :

    self.listSelectorDicts.append(addedSelectorDict)


  def select(self) :

    for selDict in self.listSelectorDicts :
      print("select, selectDict ...")
      self.selectDict(selDict)

    print("select, check selected not rejected")
    rejected = self.dictRejectedBS
    for bs in self.dictSelectedBS :
      print("bs id = %d, selected %d times" % (bs, self.dictSelectedBS[bs]))
      if bs not in rejected :
        print("bs id = %d, never rejected -- adding to final list" % bs)
        self.listFinalBS.append(bs)
      else :
        print("bs id = %d, rejected %d times" % (bs, self.dictRejectedBS[bs]))

    print("====")
    print("select, list of final selected BS:")
    print(self.listFinalBS)
    for bs in self.listFinalBS :
      print("-- %d : %s" % (bs, BranchingStrategy.dictNamesBS[bs]))


  def selectDict(self, selDict) :

    for key in selDict :
      if selDict[key] == False :
        try :
          val = self.dictRejectedBS[key]
        except :
          val = 0
        self.dictRejectedBS[key] = val + 1

      else : # True
        try :
          val = self.dictSelectedBS[key]
        except :
          val = 0
        self.dictSelectedBS[key] = val + 1

    print("----")
    print("selectDict, dictRejectedBS:")
    print(self.dictRejectedBS)
    print("----")
    print("selectDict, dictSelectedBS:")
    print(self.dictSelectedBS)


if __name__ == "__main__":

  selector = BranchingStrategy()

  # example #0 : gitlab-flow, simplified git-flow
  selector.addSelector(BranchingStrategy.dictBS_1_developers)
  selector.addSelector(BranchingStrategy.dictBS_continuous_delivery)

  selector.select()

