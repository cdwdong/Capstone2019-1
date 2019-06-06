var opts = {
				angle: 0.1, 
				lineWidth: 0.3, 
				radiusScale: 1,
				pointer: {
					length: 0.6, 
					strokeWidth: 0.035,
					color: '#ffffff' 
				},
				limitMax: false, 
				limitMin: false, 
				strokeColor: '#E0E0E0', 
				generateGradient: true,
				highDpiSupport: true, 
				staticZones: [
					{strokeStyle: "rgb(0,50,255)", min: 0, max: 30, height: 1.4},
					{strokeStyle: "rgb(50,255,50)", min: 30, max: 80, height: 1.2},
					{strokeStyle: "rgb(255,255,50)", min: 80, max: 150, height: 1},
					{strokeStyle: "rgb(255,0,50)", min: 150, max: 300, height: 0.8},
					{strokeStyle: "rgb(200,200,200)", min: 198, max: 202, height: 1.3}
				],
				staticLabels: {
				font: "10px sans-serif",
				labels: [0, 30, 80, 150, 200, 250, 300], 
				color: "#ffffff", 
				fractionDigits: 0 
				},
				};
				var target = document.getElementById('g1');
				var gauge = new Gauge(target).setOptions(opts);
				gauge.maxValue = 300;
				gauge.setMinValue(0); 
				gauge.animationSpeed = 40;
				gauge.set(222);