import requests
import json
import time
import csv
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
}

csvfile = open('知乎评论.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(['id', 'created_time', 'author', 'content'])


def GetAnswers():
    i = 0
    while True:
        url = 'https://www.zhihu.com/api/v4/questions/1342475221/answers' \
              '?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%' \
              '2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%' \
              '2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%' \
              '2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%' \
              '2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%' \
              '2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%' \
              '2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset={0}&platform=desktop&' \
              'sort_by=default'.format(i)

        state=1
        while state:
            try:
                res = requests.get(url, headers=headers, timeout=(3, 7))
                state=0
            except:
                continue

        res.encoding = 'utf-8'
        jsonAnswer = json.loads(res.text)
        print(jsonAnswer)
        is_end = jsonAnswer['paging']['is_end']

        for data in jsonAnswer['data']:
            l = list()
            answer_id = str(data['id'])
            l.append(answer_id)
            l.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['created_time'])))
            l.append(data['author']['name'])
            l.append(''.join(etree.HTML(data['content']).xpath('//p//text()')))
            writer.writerow(l)
            print(l)

            if data['admin_closed_comment'] == False and data['can_comment']['status'] and data['comment_count'] > 0:
                GetComments(answer_id)

        i += 5
        print('打印到第{0}页'.format(int(i / 5)))

        if is_end:
            break

        time.sleep(1)


def GetComments(answer_id):
    j = 0
    while True:
        url = 'https://www.zhihu.com/api/v4/answers/{0}/root_comments?order=normal&limit=20&offset={1}&status=open'.format(
            answer_id, j)

        state=1
        while state:
            try:
                res = requests.get(url, headers=headers, timeout=(3, 7))
                state=0
            except:
                continue

        res.encoding = 'utf-8'
        jsonComment = json.loads(res.text)
        is_end = jsonComment['paging']['is_end']

        for data in jsonComment['data']:
            l = list()
            comment_id = str(answer_id) + "_" + str(data['id'])
            l.append(comment_id)
            l.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['created_time'])))
            l.append(data['author']['member']['name'])
            l.append(''.join(etree.HTML(data['content']).xpath('//p//text()')))
            writer.writerow(l)
            print(l)

            for child_comments in data['child_comments']:
                l.clear()
                l.append(str(comment_id) + "_" + str(child_comments['id']))
                l.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(child_comments['created_time'])))
                l.append(child_comments['author']['member']['name'])
                l.append(''.join(etree.HTML(child_comments['content']).xpath('//p//text()')))
                writer.writerow(l)
                print(l)
        j += 20
        if is_end:
            break

        time.sleep(1)


GetAnswers()
csvfile.close()