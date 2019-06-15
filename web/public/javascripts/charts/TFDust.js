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
var TFD = null;
var LCData = null;

var tfdv1 = null;
var tfdv2 = null;
var tfdv3 = null;
var tfdv4 = null;
var tfdv5 = null;
var tfdv6 = null;
var tfdv7 = null;

var tfdt1 = null;
var tfdt2 = null;
var tfdt3 = null;
var tfdt4 = null;
var tfdt5 = null;
var tfdt6 = null;
var tfdv7 = null;


$.getJSON( "http://52.78.166.156:8080/sensor_json", function( data ) {
					var n = $(data).length;
					
					tfdv1 = (data[n-55].data);
					tfdv2 = (data[n-46].data);
					tfdv3 = (data[n-37].data);
					tfdv4 = (data[n-28].data);
					tfdv5 = (data[n-19].data);
					tfdv6 = (data[n-10].data);
					tfdv7 = (data[n-1].data);
					
					tfdt1 = (data[n-55].date);
					tfdt2 = (data[n-46].date);
					tfdt3 = (data[n-37].date);
					tfdt4 = (data[n-28].date);
					tfdt5 = (data[n-19].date);
					tfdt6 = (data[n-10].date);
					tfdt7 = (data[n-1].date);

TFD = [tfdv1, tfdv2, tfdv3, tfdv4, tfdv5, tfdv6, tfdv7]; //미세먼지 량

LCData = {
			labels: [tfdt1, tfdt2, tfdt3, tfdt4, tfdt5, tfdt6, tfdt7], //밑에 라벨인데 10틱 간격
			datasets: [{
						label: '최근 시간별 미세먼지',
						backgroundColor: color(ChartHelper.chartColors.blue).alpha(0.4).rgbString(),
						borderColor: ChartHelper.chartColors.blue,
						borderWidth: 2,
						data: TFD
						}]
			};

var ctx = document.getElementById('TFDust');

Chart.defaults.global.defaultFontColor = 'white'; //전체 기본 폰트 색상
window.LChart = new Chart(ctx, {
									type: 'line',
									data: LCData,
									options: {
												responsive: true,
												maintainAspectRatio: false,
												legend: {position: 'top'},  //위에 네모 이름 붙은거
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
