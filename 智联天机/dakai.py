import requests
import json
cookies = ['INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamMxTVNJc0ltVjRjQ0k2TVRZME5qSTRNREU0TW4wLlF6V0x6NU1rVHVvQllLampJQko2dnVON2JoN0JOSllELXBHcGhqQUdnNDRDS0c5Mm5WNnZuWGhqb1BVNkxpSDQ2S2QwRmdGSkJJTnA3aGczWlFObUtB; ZPSSO_USER_EMPID=13362751; ZPSSO_USER_NAME=lygsp.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp.daili%22%2C%22empId%22%3A%2213362751%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221002%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D;',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamMyTVNJc0ltVjRjQ0k2TVRZME5qSTRNRE01TW4wLnNHYXFlLTllbDhQRnJxQ2tPQmRLLVY3eFBhWDFCdUNjUTVrQi1BUmpVb0pWN2Y3TUM2YjhCNlBfOTluNGFLUGhwZU8zcHUzNGxic25HcURBeEdFN2pR; ZPSSO_USER_EMPID=13362761; ZPSSO_USER_NAME=lygsp01.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp01.daili%22%2C%22empId%22%3A%2213362761%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamMzTVNJc0ltVjRjQ0k2TVRZME5qSTRNRFEzTVgwLmxhSUFyd2RyNS00UWtQY1ZWd29oTV9TeVpDSEFjanJtRDI3M1h1c3ROd195V3Awc1l1TFgzSk44aEZtUzl4QVNHZ0hmTXR6VXI0eXBRY0FLTTZFeExR;ZPSSO_USER_EMPID=13362771; ZPSSO_USER_NAME=lygsp02.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp02.daili%22%2C%22empId%22%3A%2213362771%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamM0TVNJc0ltVjRjQ0k2TVRZME5qSTRNREl6TjMwLkN1U2hfLTVzbHNNcHYyb3Vjc2tkNFZCckE3YmEzdTJNc1NZUTc1dnMtT3lKSEtQNE1vMkd4Y0xyMGtacFBHQzgybnRZWVFPaThFZVJmOE1kQmFVd3VR;ZPSSO_USER_EMPID=13362781; ZPSSO_USER_NAME=lygsp03.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp03.daili%22%2C%22empId%22%3A%2213362781%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamM1TVNJc0ltVjRjQ0k2TVRZME5qSTRNREkxTm4wLm81M3FfYkVDd25UUXQtTU42WVdCQWdtU0ppaU1FTFFabDlsRTdLMG9WRVRBeHlBdWhKbTl5b09oenNHaHFTZzVpWkQ2YXJ2c3FrSF9CXzgwdkRzcV9B; ZPSSO_USER_EMPID=13362791; ZPSSO_USER_NAME=lygsp04.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp04.daili%22%2C%22empId%22%3A%2213362791%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGMzTVNJc0ltVjRjQ0k2TVRZME5qSTRNREkyT1gwLlgzQkxvVU9Cd2NneURENFg3N2kzYkdMdkZwc3dfY2FSeV8yUFRwcVR1VVZSNnpvdWR4Rk93SkhXamFmMHJjeFBwUFRuV0Rwci16bVVRNGprbW1WYmhB; ZPSSO_USER_EMPID=13364771; ZPSSO_USER_NAME=lygsp05.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp05.daili%22%2C%22empId%22%3A%2213364771%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGM0TVNJc0ltVjRjQ0k2TVRZME5qSTRNREk0TVgwLmlEc0RRTHFFaE9WU1ZuelhZSno2REw4ZmJxWFlqN3lLVE5sMEdXd3dack50VHg2ZkFKd2p4b1VNT2FKZWI1LTVvLThJX3dNb3VHSDdON0tmRGVsQmlB; ZPSSO_USER_EMPID=13364781; ZPSSO_USER_NAME=lygsp06.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp06.daili%22%2C%22empId%22%3A%2213364781%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGM1TVNJc0ltVjRjQ0k2TVRZME5qSXlOVGd3TW4wLjVfRDZJWU96ajZ0VWs1UUpTbnQ4TjJBVjEydUpOWjl5WmVYT2U1c0lFSDVxN3QwQ0s4YXZZaWpWM25PcnhFR1JJaVd5aG9xZkNRWFdYcDVGazBtOHhR;ZPSSO_USER_EMPID=13364791; ZPSSO_USER_NAME=lygsp07.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp07.daili%22%2C%22empId%22%3A%2213364791%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGd3TVNJc0ltVjRjQ0k2TVRZME5qSTRNRFV4TlgwLm9uT3lQeHY4Nm5BUTh0Sjk1UTZYQ0pGR0tpV2N6ZTFNSjYxU2RuRFJ4QkFzaGIwbHpma2ZCblNqb0RDY3BGaU9mWENTNzNRLTl2RWdoOHNwUTlaZWtn;  ZPSSO_USER_EMPID=13364801; ZPSSO_USER_NAME=lygsp08.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp08.daili%22%2C%22empId%22%3A%2213364801%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D',
          'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGd4TVNJc0ltVjRjQ0k2TVRZME5qSTRNRE15TlgwLm5kUW1TTEpqdFBsb1czSFZaam45bzYzSWZ3WlFpa01HVk9rNEMtT3Z5RWdGeEdUblI5RmZZb1pnMWFRMjR5N2poVVpBZ3dWNzc0U25QV0Z4enh0RkZR; ZPSSO_USER_EMPID=13364811; ZPSSO_USER_NAME=lygsp09.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp09.daili%22%2C%22empId%22%3A%2213364811%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D'
          ]
headers1 = {'Cookie': cookies[7]}
payload = {'custName': '海州区苍梧社区茉兰美容院'}
a = json.loads(requests.post('https://customeraudit.zhaopin.com/customeraudit/service/custIdentify/getIdentifyInfoByName', headers=headers1, data=payload).text)
payload = {'custName': '海州区苍梧社区茉兰美容院',
           'toEmpName': 'lygsp07.daili',
           'address': a['info']['data']['DOM'],
           'tagOne':None,
           'tagTwo':None,
           'attachmentListString':[],
           'country':1010,
           'province':1010,
           'city':1087,
           'friendId':None,
           'contactsName':a['info']['data']['FRNAME'],
           'contactsSex':1,
           'contactsEmail':'',
           'phoneNumber':'',
           'phoneArea':'',
           'phoneExt':'',
           'remark':'',
           'modifyCount':1
           }
a = json.loads(requests.post('https://customeraudit.zhaopin.com/customeraudit/service/inputCustomer/saveOrUpdate?isModify=false', headers=headers1, data=payload).text)
print(['提交', a])