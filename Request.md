Write me a program that transform excel data to javascript data like this:
Input Excel table:
|派别|场所名称|地址|负责人姓名|省级行政区|省属地级行政区/直辖市属县区级行政区|经纬度|
|-|-|-|-|-|-|-|
|正一|苏州玄妙观|江苏省苏州市姑苏区观前街94号|员金胜|江苏|苏州市|120,31|

In this case, latitude and longitude should be separated.Example Output:
```JavaScript
{
		'派别':'正一',
		'场所名称': 苏州玄妙观,
        '负责人姓名': 员金胜,
        '省级行政区': 江苏,
        '省属地级行政区/直辖市属县区级行政区': 苏州市,
        'lon':120,
        'lat':31
	},
```				