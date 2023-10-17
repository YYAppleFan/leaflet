# 全国道观分布图
![Alt text](/images/Showcase.png)
基于[Leaflet](https://leafletjs.com)的全国道观分布图，具备基本的地图操作功能，包括缩放、拖动、识别要素等。同时支持更换底图和按省市快速定位。

[在线访问](https://yyapplefan.github.io/leaflet/)

## 项目结构
- `README.md`：项目说明文件
- `index.html`：主页面
- `Data/`：数据文件夹
  - `Distribution map of Taoist temples in China.csv`：道观分布数据
  - `Flag.js`：Unicode区域指示符，替代原项目以色块表示的国旗
  - `province-city-latlng.csv`：Excel文件转换得到的含经纬度的省市二级联动数据CSV文件
  - `province-city-latlng.xlsx`：含经纬度的省市两级联动数据Excel文件
  - `province-city.json`：省市两级联动数据JSON文件
  - `province-city.txt`：CSV文件转换得到的省市两级联动数据文本文件
  - `temples.json`: 道观分布数据JSON文件
- `images/`：图片文件夹
  - `Showcase.png`：项目展示图
  - 其他文件为 Leaflet 和 Leaflet.MarkerCluster 自带的图片文件
- `js/`：JavaScript文件夹
  - `map.js`：核心`JavaScript`代码，包括地图初始化、底图切换、要素识别、要素弹窗等
- `Leaflet/`：Leaflet文件夹
- `Leaflet.MarkerCluster/`：Leaflet.MarkerCluster文件夹
- `Tools/`：
  - `jsonToTxt.py`：JSON文件转换为文本文件的Python脚本
  - `Request.md`：格式化`temples.json`的 ChatGPT 提示词

## 页面功能
1. 地图基本操作由 Leaflet 提供，包括缩放、拖动、识别要素等
2. 针对大批量数据，采用 Leaflet.MarkerCluster 插件进行聚合，在不同缩放级别下显示不同数量的要素
3. 页面右上角提供按省市快速定位功能，点击省市按钮，即可将地图缩放至对应省市
4. 页面右下角提供底图切换功能，点击按钮，即可切换底图

## 设计思路
页面采取顶栏、地图区域和底栏设计。顶栏包含标题，地图区域包含地图、按省市快速定位功能和底图切换功能，底栏包含地图供应商标志和审图号。地图部分为批量显示数据，同时保持整洁的界面，采用了 Leaflet.MarkerCluster 插件进行聚合，以达到较快的加载速度和较好的用户体验。针对每个标签，采用了 Leaflet 自带的弹窗功能，以显示详细信息。相关信息均从[国家宗教事务局-宗教活动场所基本信息](https://www.sara.gov.cn/gjzjswj/zjjcxxcxxt/zjhdcsjbxx/index.html)直接获取，共计8330条，囊括派别、场所名称、地址、负责人姓名、省级行政区、省属地级行政区/直辖市属县区级行政区。为快速定位某地的道观，页面右上角提供了省市联动的下拉选择框，根据所选省/市即可快速缩放至指定区域，以便进一步浏览。为了更好地展示地图，页面右下角提供了底图切换功能，包括高德地图、谷歌地图、天地图、和捷泰地图，用户可根据自身需求选择合适的底图。

## 技术路线
1. 从[国家宗教事务局-宗教活动场所基本信息](https://www.sara.gov.cn/gjzjswj/zjjcxxcxxt/zjhdcsjbxx/index.html)手动拉取全国道观信息
2. 将道观地址[地理编码](https://www.piliang.tech/geocoding-amap)为经纬度
3. 向 ChatGPT 提交请求，将数据格式化为`temples.json`
4. 从 [modood/Administrative-divisions-of-China](https://github.com/modood/Administrative-divisions-of-China) 下载省市两级联动行政区划数据，并[地理编码](https://www.piliang.tech/geocoding-amap)为经纬度
5. 下载 [Leaflet](https://leafletjs.com) 和 [Leaflet.MarkerCluster](https://github.com/Leaflet/Leaflet.markercluster) 库，并在 `index.html` 中引用
6. 在 `index.html` 和 `style.css`中构建网页框架，分顶栏、地图区域和底栏
7. 在 `map.js` 中构建地图，包括数据导入、MarkerCluster 应用、要素弹窗和底图切换等
   - 数据导入采取直接写入的方法，如下所示：
   ```javascript
   let temples=[
    {
        "派别": "全真",
        "场所名称": "北京白云观",
        "地址": "北京市西城区西便门外白云观",
        "负责人姓名": "李信军",
        "省级行政区": "北京",
        "地级行政区": "西城区",
        "lon": 116.343781,
        "lat": 39.901235
    },...
    ]
    ```
    - 设计地图底图切换功能，采用`L.tileLayer`方法，并在右下角添加按钮，如下所示：
    ```javascript
    var baseLayers = {
    "高德地图": L.tileLayer('http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}', { subdomains: "1234" }).addTo(map),...
    }
    L.control.layers(baseLayers, {}, { position: "bottomright" }).addTo(map);
    ```
    - 通过 `L.markerClusterGroup` 方法，将数据导入 MarkerCluster 中并设计要素弹窗，如下所示：
    ```javascript
    var markers = L.markerClusterGroup();	
		for (var i = 0; i < temples.length; i++) {
			var temple = temples[i];
            var sect = temple.派别.replace(/"/g, '');
            ...
            var lon = temple.lon;
            var lat = temple.lat;
			var marker = L.marker(L.latLng(lat, lon), { 
                sect: sect,
                ...
             });
            var popupContent = `<b>${place}</b><br>
                                <b>派别：</b>${sect}<br>
                                <b>地址：</b>${address}<br>
                                <b>负责人：</b>${leader}<br>
                                <b>所属省级行政区：</b>${province}<br>
                                <b>所属地级行政区：</b>${city}<br>`
			marker.bindPopup(popupContent);
			markers.addLayer(marker);
		}
    ```
    - 完善 `L.markerClusterGroup` 方法，添加缩放功能并设置显示范围，如下所示：
    ```javascript
    markers.on('clusterclick', function (a) {
	a.layer.zoomToBounds();
    });
    map.addLayer(markers);
    map.fitBounds(markers.getBounds())
    ```
    - 设计按省市快速定位功能，采用下拉列表形式实现，如下所示：
    ```javascript
    // 创建两个下拉列表
    var selectControl = L.control({position: 'topright'});

    selectControl.onAdd = function (map) {...}

    selectControl.addTo(map);

    // 中国各省级行政区及其地级行政区的对象
    var data = {...}

    // 填充省份下拉列表
    var provinceSelect = document.getElementById("provinceSelect");
    for (var province in data) {...}

    // 当省份下拉列表的选项改变时，更新城市下拉列表
    provinceSelect.addEventListener("change", function(){...});

    // 当城市下拉列表的选项改变时，前往指定地点
    citySelect.addEventListener("change", function(){...});
    ```
8. 采用 GitHub Pages 进行部署，实现在线访问

## 数据来源
- 道观数据：[国家宗教事务局-宗教活动场所基本信息](https://www.sara.gov.cn/gjzjswj/zjjcxxcxxt/zjhdcsjbxx/index.html)
- 行政区划数据：[modood/Administrative-divisions-of-China](https://github.com/modood/Administrative-divisions-of-China)
- 行政区划经纬度数据：[地理编码 (高德) ](https://www.piliang.tech/geocoding-amap)
- 底图参考：[muyao1987/leaflet-tileLayer-baidugaode](https://github.com/muyao1987/leaflet-tileLayer-baidugaode)