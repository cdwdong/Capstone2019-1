var ChartHelper = {
            chartColors: {
							red: 'rgb(255, 99, 132)',
							orange: 'rgb(255, 159, 64)',
							yellow: 'rgb(255, 205, 86)',
							green: 'rgb(75, 192, 192)',
							blue: 'rgb(54, 162, 235)',
							purple: 'rgb(153, 102, 255)',
							grey: 'rgb(201, 203, 207)',
							white: 'rgb(255, 255, 255)'
							}
					};

//전체 잡고 초기화 한번
var color = Chart.helpers.color;
var WFD = null;
var LCData = null;

var wfdv1 = null;
var wfdv2 = null;
var wfdv3 = null;
var wfdv4 = null;
var wfdv5 = null;
var wfdv6 = null;
var wfdv7 = null;

var wfdt1 = null;
var wfdt2 = null;
var wfdt3 = null;
var wfdt4 = null;
var wfdt5 = null;
var wfdt6 = null;
var wfdv7 = null;

$.getJSON( "http://52.78.166.156:8080/sensor_json", function( data ) {
					var n = $(data).length;

					wfdv1 = (data[parseInt((n-1)/7)].data);
					wfdv2 = (data[parseInt(((n-1)/7)*2)].data);
					wfdv3 = (data[parseInt(((n-1)/7)*3)].data);
					wfdv4 = (data[parseInt(((n-1)/7)*4)].data);
					wfdv5 = (data[parseInt(((n-1)/7)*5)].data);
					wfdv6 = (data[parseInt(((n-1)/7)*6)].data);
					wfdv7 = (data[n-1].data);
					
					wfdt1 = (data[parseInt((n-1)/7)].date);
					wfdt2 = (data[parseInt(((n-1)/7)*2)].date);
					wfdt3 = (data[parseInt(((n-1)/7)*3)].date);
					wfdt4 = (data[parseInt(((n-1)/7)*4)].date);
					wfdt5 = (data[parseInt(((n-1)/7)*5)].date);
					wfdt6 = (data[parseInt(((n-1)/7)*6)].date);
					wfdt7 = (data[n-1].date);
				

WFD = [wfdv1, wfdv2, wfdv3, wfdv4, wfdv5, wfdv6, wfdv7]; // 미세먼지 량

LCData = {
			labels: [wfdt1, wfdt2, wfdt3, wfdt4, wfdt5, wfdt6, wfdt7], //밑에 라벨
			datasets: [{
						label: '장기간 미세먼지',
						backgroundColor: color(ChartHelper.chartColors.green).alpha(0.4).rgbString(),
						borderColor: ChartHelper.chartColors.green,
						borderWidth: 2,
						data: WFD
						}]
			};

var ctx = document.getElementById('WFDust');

Chart.defaults.global.defaultFontColor = 'white'; //전체 기본 폰트 색상
window.LChart = new Chart(ctx, {
									type: 'line',
									data: LCData,
									options: {
												responsive: true,
												maintainAspectRatio: false,
												legend: {position: 'top'}, //위에 네모 이름 붙은거
												scales: {

														yAxes: [{
																ticks: {
																		beginAtZero:true,
																		callback: function(value){if (0 === value % 1) {return value;}}
																		}
																}]
														}
												}
								});

var colorNames = Object.keys(ChartHelper.chartColors);

});