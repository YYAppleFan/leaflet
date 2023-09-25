var map = L.map('map').setView([31.311960,120.626314], 16);

L.tileLayer('http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',{ 
    subdomains: "1234" 
}).addTo(map);

var marker = L.marker([31.311960,120.626314]).addTo(map)
		.bindPopup('苏州玄妙观<br> 江苏省苏州市姑苏区观前街94号')
		.openPopup();
        
var marker = L.marker([31.311090,120.619128]).addTo(map)
        .bindPopup('苏州城隍庙<br> 江苏省苏州市姑苏区景德路94号')