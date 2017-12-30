import scrapy
import json
import os


class GithubSpider(scrapy.Spider):
    name = "github"

    def start_requests(self):
        urls = [
            'https://api.github.com/search/repositories?q=stars:>=1&sort=stars&order=desc&page={p}&per_page=100'.format(
                p=p)
            for p in range(1, 10)
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        if 'message' in data:
            return
        json_obj = self.input_from_json()
        for obj in data['items']:
            if obj['language'] is None:
                continue
            print(obj['language'])
            language_obj = None
            if obj['language'] in json_obj:
                language_obj = json_obj[obj['language']]
            else:
                language_obj = {
                    "total_star": 0,
                    "total_fork": 0,
                    "total_watch": 0,
                    "total_sum": 0,
                    'count': 0,
                    'reposition': []
                }
            language_obj = {
                "total_star": int(obj['stargazers_count']) + int(language_obj['total_star']),
                "total_fork": int(obj['forks_count']) + int(language_obj['total_fork']),
                "total_watch": int(obj['watchers_count']) + int(language_obj['total_watch']),
                "total_sum": int(obj['size']) + int(language_obj['total_sum']),
                "count": 1 + int(language_obj['count']),
                'reposition': language_obj['reposition']
            }
            language_obj['reposition'].append({
                'url': obj['html_url'],
                'star': int(obj['stargazers_count']),
                'fork': int(obj['forks_count']),
                'watch': int(obj['watchers_count']),
                "language": obj['language'],
                'name': obj['full_name']
            })
            json_obj[obj['language']] = language_obj

        arr = []
        for key in json_obj.keys():
            arr.append(json_obj[key]['total_star'])
        arr.sort()
        arr.reverse()
        arr = arr[:10]
        obj = {}
        for key in json_obj.keys():
            if json_obj[key]['total_star'] in arr:
                obj[key] = json_obj[key]

        self.output_to_json(obj)

    def input_from_json(self):
        if os.path.exists('data.json'):
            os.remove('data.json')
        return {}

    def output_to_json(self, json_obj):
        with open("data.json", "a+") as f:
            json.dump(json_obj, f)
