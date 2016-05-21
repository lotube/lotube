from django import forms


class CrawlerForm(forms.Form):
    term = forms.CharField(label='Crawler Starting Term', max_length=50)
    max_depth = forms.IntegerField(label='Crawling Depth')
    max_breadth = forms.IntegerField(label='Crawling Breadth')
