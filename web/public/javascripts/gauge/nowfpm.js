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
					{strokeStyle: "rgb(0,50,255)", min: 0, max: 15, height: 1.4},
					{strokeStyle: "rgb(50,255,50)", min: 15, max: 35, height: 1.2},
					{strokeStyle: "rgb(255,255,50)", min: 35, max: 75, height: 1},
					{strokeStyle: "rgb(255,0,50)", min: 75, max: 150, height: 0.8},
					{strokeStyle: "rgb(200,200,200)", min: 108, max: 112, height: 1.3}
				],
				staticLabels: { 
				font: "10px sans-serif",  
				labels: [0, 15, 35, 75,150, 110, 150],  
				color: "#ffffff", 
				fractionDigits: 0 
				},
				};
				var target = document.getElementById('g2'); 
				var gauge = new Gauge(target).setOptions(opts);
				gauge.maxValue = 150;
				gauge.setMinValue(0);
				gauge.animationSpeed = 40;
				gauge.set(44);