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
var WFPM = null;
var LCData = null;

WFD = ['155.5', '120', '100', '98', '85', '66.6', '33.3']; //요일별 미세먼지
WFPM = ['88.8', '80', '70', '66.6', '40', '33.3', '20']; //요일별 초미세먼지
LCData = {
			labels: ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'], //밑에 라벨
			datasets: [{
						label: '요일별 미세먼지',
						backgroundColor: color(ChartHelper.chartColors.green).alpha(0.2).rgbString(),
						borderColor: ChartHelper.chartColors.green,
						borderWidth: 2,
						data: WFD
						},
						{
						label: '요일별 초미세먼지',
						backgroundColor: color(ChartHelper.chartColors.yellow).alpha(0.7).rgbString(),
						borderColor: ChartHelper.chartColors.yellow,
						borderWidth: 2,
						data: WFPM
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

