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
var TFPM = null;
var LCData = null;

TFD = ['111', '128', '156', '181', '175', '160', '170', '145', '124', '102', '87', '66']; //시간별 미세먼지
TFPM = ['78', '88', '91', '92', '85', '77', '71', '63', '62', '53', '44', '30']; //시간별 초미세먼지
LCData = {
			labels: ['01시', '03시', '05시', '07시', '09시', '11시', '13시', '15시', '17시', '19시', '21시', '23시'], //밑에 라벨인데 2시간 간격
			datasets: [{
						label: '시간별 미세먼지',
						backgroundColor: color(ChartHelper.chartColors.blue).alpha(0.2).rgbString(),
						borderColor: ChartHelper.chartColors.blue,
						borderWidth: 2,
						data: TFD
						},
						{
						label: '시간별 초 미세먼지',
						backgroundColor: color(ChartHelper.chartColors.red).alpha(0.7).rgbString(),
						borderColor: ChartHelper.chartColors.red,
						borderWidth: 2,
						data: TFPM
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

