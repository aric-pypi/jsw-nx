import jsw_nx as nx


def test_html2text():
    html1 = '<a>免费<em>网站模板</em>,<em>网站模板</em>,企业<em>网站模板</em>,下载企业<em>网站模板</em></a>'
    assert nx.html2text(html1) == '免费网站模板,网站模板,企业网站模板,下载企业网站模板'

