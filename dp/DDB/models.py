from django.db import models
from django.contrib.postgres.fields import ArrayField
# import datetime

# Table per release
class AGGREGATE_TC_STATE(models.Model):
    DomainName = models.CharField(max_length=50, blank = False, primary_key = True) #storage, networking
    TotalTcs = models.IntegerField()
    AutomatedTcs = models.IntegerField()
    TestedTcs = models.IntegerField()
    PassedTcs = models.IntegerField()
    #we can calculate % using above fields

    def __str__(self):
        return self.DomainName


# Table per release
class TC_INFO(models.Model):
    Cards = (('BOS','BOS'), ('NYNJ','NYNJ'), ('COMMON','COMMON'), ('OS','OS'))
    status = (('UNDERWORK', 'UNDERWORK'), ('ASSIGNED', 'ASSIGNED'), ('COMPLETED', 'COMPLETED'), ('NA', 'NA'))
    Platforms = (('oc-k8s', 'oc-k8s'), ('dcx-k8s', 'dcx-k8s'))
    Servers = (('Dell', 'Dell'), ('Intel', 'Intel'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('UNKNOWN', 'UNKNOWN'))

    TcID = models.CharField(max_length = 200, blank = False, primary_key=True)
    TcName = models.CharField(max_length = 2000, blank = True)
    Domain = models.CharField(max_length=50, blank = True)  #storage, nw
    SubDomain = models.CharField(max_length=50)  #remote, local, mirroring
    Scenario = models.CharField(max_length = 200, blank = True) #stress, standard, negative
    Description = models.TextField(blank=False)
    ExpectedBehaviour = models.CharField(max_length = 5000, blank = True)
    Notes = models.CharField(max_length = 1000, blank = True)
    CardType = ArrayField(models.CharField(max_length = 10, choices = Cards, blank = True, default=None))
    ServerType = ArrayField(models.CharField(max_length = 10, choices = Servers, blank = True, default=None))
    OrchestrationPlatform = ArrayField(models.CharField(max_length = 10, choices = Platforms, blank = False))
    Status = models.CharField(max_length = 9, choices = status, blank = True)

    def __str__(self):
        return self.TcID

# Universal
class USER_INFO(models.Model):
    UserId = models.IntegerField(primary_key = True) # Employee id or email
    UserName = models.CharField(max_length=50, blank = False)
    Designation = models.CharField(max_length=20) # automation / dev / UI
    Permission = models.CharField(max_length=10, blank = True) # user / admin

    def __str__(self):
        return self.UserName

# Table per release [Reason for maintaining into every release is, setups can be broken or nodes can be combined]
class SETUP_INFO(models.Model):
    State = (('Failed', 'Failed'), ('Good','Good'))
    Status = (('Idle','Idle'), ('In-use','In-Use'))

    SetupName = models.CharField(max_length = 20, primary_key = True)
    OwnerId = models.ForeignKey(USER_INFO, blank = False, on_delete = models.PROTECT, related_name = 'Owner')
    CurrentUserId = models.ForeignKey(USER_INFO, blank = True, on_delete = models.PROTECT, related_name = 'User')
    Inventory = models.CharField(max_length = 5000, blank = False)
    ClusterState = models.CharField(max_length = 6, choices = State) # in failed state to debug
    ClusterStatus = models.CharField(max_length = 6, choices = Status) # using or idle or running sanity

    def __str__(self):
        return self.SetupName

# Table per release
class TC_STATUS(models.Model):
    TcID = models.ForeignKey(TC_INFO, on_delete = models.CASCADE, related_name='tcid')
    Build = models.CharField(max_length = 20, blank = False)
    Result = models.CharField(max_length = 14, blank = True)
    Bugs = models.CharField(max_length = 10, blank = True) # we can make this as list field also
    Date = models.DateField(auto_now=False, auto_now_add=True)
    # Setup = models.ForeignKey(SETUP_INFO, on_delete = models.PROTECT)
    # Logs = models.TextField()

    def __str__(self):
        return "TCID={0}".format(self.TcID)

# table in each release
class FEATURES(models.Model):
    JiraID = models.CharField(max_length = 5, primary_key = True)
    TestedStaus = models.CharField(max_length = 3, blank = False)
    Reason = models.TextField() # if not tested proviide reason

# Table per release
class SANITY_RESULTS(models.Model):
    SanityType = (("Daily","Daily"),("Weekly","Weekly"), ("Sanity","Sanity"))
    Result = (("Pass","Pass"), ("Fail","Fail")) 

    SanityId = models.AutoField(primary_key = True) 
    Tag = models.CharField(max_length=6, choices = SanityType, default = "Daily", blank = False)
    Build = models.CharField(max_length=10, blank = False)
    Result = models.CharField(max_length=10, choices = Result, blank = False)
    Logs = models.TextField()
    Setup = models.ForeignKey(SETUP_INFO, on_delete = models.PROTECT)
    Timestamp = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "{0}{1}".format(self.SanityId, self.Timestamp)

# UNIVERSAL DATABASE ENTITY
class RELEASES(models.Model):
    ReleaseNumber = models.CharField(max_length = 10, blank = False, primary_key = True)
    BuildNumberList = ArrayField((models.CharField(max_length = 11, blank = True)))
    EngineerCount = models.IntegerField(default = 0)
    # HardwareSupport = ArrayField((models.CharField(max_length = 10 ,blank = True)))
    CardType = ArrayField(models.CharField(max_length = 10, blank = True))
    ServerType = ArrayField(models.CharField(max_length = 10, blank = True))
    SetupsUsed = ArrayField(models.CharField(max_length = 10, blank = True))
    # SetupsUsed = ArrayField(models.ForeignKey(SETUP_INFO, on_delete = models.PROTECT))
    QAStartDate = models.DateTimeField(auto_now = False, auto_now_add = False)
    TargetedReleaseDate = models.DateTimeField(auto_now = False, auto_now_add = False)
    ActualReleaseDate = models.DateTimeField(auto_now = False, auto_now_add = False)
    TargetedCodeFreezeDate = models.DateTimeField(auto_now = False, auto_now_add = False)
    UpgradeTestingStartDate = models.DateTimeField(auto_now = False, auto_now_add = False)
    UpgradeMetrics = ArrayField(models.CharField(max_length = 10), blank = True, null = True)  # 2.1.0 -> 2.3.0 && 2.2.0 -> 2.3.0
    Customers = ArrayField(models.CharField(max_length = 100, blank = True))
    FinalBuild = models.CharField(max_length = 10, blank = True)
    FinalOS =  models.CharField(max_length = 10, blank = True)
    FinalDockerCore = models.CharField(max_length = 10, blank = True)
    UbootVersion = models.CharField(max_length = 100, blank = True)
    RedFlagsRisks = models.TextField(blank = True)
    AutomationSyncUp = models.TextField(blank = True)

    def __str__(self):
        return self.ReleaseNumber


# Universal
class WORKSHEET(models.Model):
    UserID = models.ForeignKey(USER_INFO, on_delete = models.PROTECT)
    Release = models.ForeignKey(RELEASES, on_delete = models.PROTECT)
    Timestamp = models.CharField(max_length=25, blank = False)
    Work = models.TextField()


class LOGS(models.Model):
    UserID = models.ForeignKey(USER_INFO, on_delete = models.PROTECT)
    Timestamp = models.DateTimeField(auto_now = False, auto_now_add = False)
    RequestType = models.CharField(max_length = 10, blank = False)
    Logs = models.TextField()
    Link = models.ForeignKey('self', on_delete = models.PROTECT, blank=True, null=True)

    def __str__(self):
        return "{0}:-{1}".format(self.UserID, self.RequestType)

"""

need to create this below table because we cannot simply maintain a list of description 
of features in releases table.
eg.) 
row 1)  releaseNumber = 1
        featureList = ["mirroring", "snapshot", "bakup"]
        featureDescription = ["suporting mirroring upto 3 nodes", "can take snapshot of volumes", "takes backup of volumes everyday"]
row 2)  releaseNumber = 2
        featureList = ["mirroring", "snapshot", "bakup"]
        featureDescription = ["suporting mirroring upto 3 nodes", "can take snapshot of volumes", "takes backup of volumes everyday"]
row 3)  releaseNumber = 3
        featureList = ["mirroring", "snapshot", "bakup"]
        featureDescription = ["suporting mirroring upto 3 nodes", "can take snapshot of volumes", "takes backup of volumes everyday"]

INSTEAD we can save it as 
row 1)  RN = r1
        FeatureList = [f1,f2,f3] #these will be foreign keys from below table
row 2)  RN = r2
        FeatureList = [f1,f2,f3] #these will be foreign keys from below table
row 3)  RN = r3
        FeatureList = [f1,f2,f3] #these will be foreign keys from below table
row 4)  RN = r4
        FeatureList = [f1,f2,f3] #these will be foreign keys from below table
"""


"""
function which returns same schema to create multile table of same schema


def getTcStatusModel(date):
   class TC_STATUS(models.Model):

    class Meta:
        TableName = Date

    Bugs = models.IntegerField()
    LogFilePath = models.CharField(max_length=300, blank = False)

    return TC_STATUS
"""