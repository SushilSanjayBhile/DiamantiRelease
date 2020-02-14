# Django packages
from django.db.models import Q
# from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse

# imports from django app
from .models import TC_INFO, TC_STATUS
from DDB.serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER

def TCAGGREGATE(Release):
        dictionary = {}

        dictionary['domain'] = {}
        dictionary['AvailableDomainOptions'] = {}
        dictionary['AvailableScenarios'] = []

        total = 0
        totalpass = 0
        totalfail = 0
        totalskipped = 0
        totalnottested = 0

        autopass = 0
        autofail = 0
        autoskipped = 0

        data = TC_STATUS.objects.using(Release).all()
        serializer = TC_STATUS_SERIALIZER(data, many=True)

        tcinfo = TC_INFO.objects.using(Release).filter(~Q(Domain = "GUI")).filter(~Q(Priority = "NA"))
        tcinfoserializer = TC_INFO_SERIALIZER(tcinfo, many=True)

        automated = tcinfo.filter(~Q(TcName = "TC NOT AUTOMATED")).count()
        nonautomated = tcinfo.filter(TcName = "TC NOT AUTOMATED").count()
        notapplicable = TC_INFO.objects.using(Release).filter(~Q(Domain = "GUI")).filter(Priority = "NA").count()

        scenario = TC_INFO.objects.using(Release).values('Scenario').distinct()
        for tc in scenario:
            dictionary['AvailableScenarios'].append(tc['Scenario'])

        domains = tcinfo.values('Domain').distinct()
        for tc in domains:
            domain = tc['Domain']
            # dictionary['AvailableDomainOptions'].append(domain) 

            subdomains = tcinfo.values('SubDomain').filter(Domain = domain).distinct()
            for sd in subdomains:
                subdomain = sd['SubDomain']

                if domain in dictionary['AvailableDomainOptions']:
                    dictionary['AvailableDomainOptions'][domain].append(subdomain)
                else:
                    dictionary['AvailableDomainOptions'][domain] = []
                    dictionary['AvailableDomainOptions'][domain].append(subdomain)

            tccount = 0

            if domain not in dictionary['domain']:
                dictionary['domain'][domain] = {}

                dictionary['domain'][domain]['Tested'] = {}

                domainallcount = TC_INFO.objects.using(Release).filter(Domain = tc['Domain']).filter(~Q(Priority = 'NA')).count()
                dictionary['domain'][tc['Domain']]['NotApplicable'] = 0

                dictionary['domain'][tc['Domain']]['Tested']['auto'] = {}
                dictionary['domain'][tc['Domain']]['Tested']['manual'] = {}

                tcinfocount = TC_INFO.objects.using(Release).filter(TcName = "TC NOT AUTOMATED").filter(Domain = tc['Domain']).count()
                tccount = TC_STATUS.objects.using(Release).filter(TcName = "TC NOT AUTOMATED").filter(Domain = tc['Domain'], Result = "Pass").count()
                dictionary['domain'][tc['Domain']]['Tested']['manual']['Pass'] = tccount
                totalpass += tccount
                domainallcount -= tccount

                tccount = TC_STATUS.objects.using(Release).filter(TcName = "TC NOT AUTOMATED").filter(Domain = tc['Domain'], Result = "Fail").count()
                dictionary['domain'][tc['Domain']]['Tested']['manual']['Fail'] = tccount
                totalfail += tccount
                domainallcount -= tccount

                tccount = TC_STATUS.objects.using(Release).filter(TcName = "TC NOT AUTOMATED").filter(Domain = tc['Domain'], Result = "NotTested").count()
                dictionary['domain'][tc['Domain']]['Tested']['manual']['Skip'] = tccount
                totalskipped += tccount

                tcinfocount = TC_INFO.objects.using(Release).filter(~Q(TcName = "TC NOT AUTOMATED")).filter(Domain = tc['Domain']).count()
                tccount = TC_STATUS.objects.using(Release).filter(~Q(TcName = "TC NOT AUTOMATED")).filter(Domain = tc['Domain'], Result = "Pass").count()
                dictionary['domain'][tc['Domain']]['Tested']['auto']['Pass'] = tccount
                totalpass += tccount
                autopass += tccount
                domainallcount -= tccount

                tccount = TC_STATUS.objects.using(Release).filter(~Q(TcName = "TC NOT AUTOMATED")).filter(Domain = tc['Domain'], Result = "Fail").count()
                dictionary['domain'][tc['Domain']]['Tested']['auto']['Fail'] = tccount
                totalfail += tccount
                autofail += tccount
                domainallcount -= tccount

                tccount = TC_STATUS.objects.using(Release).filter(~Q(TcName = "TC NOT AUTOMATED")).filter(Domain = tc['Domain'], Result = "NotTested").count()
                dictionary['domain'][tc['Domain']]['Tested']['auto']['Skip'] = tccount
                totalskipped += tccount
                autoskipped += tccount

                dictionary['domain'][tc['Domain']]['NotTested'] = domainallcount
                totalnottested += dictionary['domain'][tc['Domain']]['NotTested']

        dictionary['all'] = {}

        dictionary['all']['Tested'] = {}
#        dictionary['all']['NotTested'] = ((total - (autopass + autofail)) - (totalpass - autopass)) - (totalfail - autofail)
        dictionary['all']['NotTested'] = totalnottested
        dictionary['all']['NotApplicable'] = 0

        dictionary['all']['Tested']['auto'] = {}
        dictionary['all']['Tested']['auto']['Pass'] = autopass
        dictionary['all']['Tested']['auto']['Fail'] = autofail
        dictionary['all']['Tested']['auto']['Skip'] = autoskipped

        dictionary['all']['Tested']['manual'] = {}
        dictionary['all']['Tested']['manual']['Pass'] = totalpass - autopass
        dictionary['all']['Tested']['manual']['Fail'] = totalfail - autofail
        dictionary['all']['Tested']['manual']['Skip'] = totalskipped - autoskipped

        return dictionary
