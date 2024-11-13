class Slider{
	constructor(slider, {autoplay = true, inFrame = 1, offset = 1} = {}) {
		this.slider = slider;
		this.inFrame = inFrame;
		this.offset = offset;

		this.allaitems = slider.querySelectorAll('.carousel-item');
		this.frameCount = this.allaitems.length;
		this.frameIndex = 0;

		this.wrapper = slider.querySelector('.carousel-slides');
		this.nextButton = slider.querySelector('.carousel-next');
		this.prevButton = slider.querySelector('.carousel-prev');

		this.autoplay = autoplay;
		this.paused = null;

		this.init();

	}

	init(){
		this.dotButtons = this.dots();
		this.allItems.forEach(item => item.style.width = 100 / this.itemCount + '%');
		let wrapperWidth = this.itemCount / this.inFrame * 100;
        	this.wrapper.style.width = wrapperWidth + '%';

		this.nextButton.addEventListener('click', event => {
		event.preventDefault();
           	this.next();
		});

		this.prevButton.addEventListener('click', event => {
		event.preventDefault();
           	this.prev();
		});

		this.dotButtons.forEach(dot => {
            		dot.addEventListener('click', event => {
                		event.preventDefault();
                		const frameIndex = this.dotButtons.indexOf(event.target);
                		if (frameIndex === this.frameIndex) return;
                		this.goto(frameIndex);
            		});
        	});

		if (this.autoplay) {
			this.play();
			this.slider.addEventListener('mouseenter', () => clearInterval(this.paused));
			this.slider.addEventListener('mouseleave', () => this.play());
	}
}

	goto(index) {
        	if (index > this.frameCount - 1) {
            		this.frameIndex = 0;
        	} else if (index < 0) {
            		this.frameIndex = this.frameCount - 1;
        	} else {
            		this.frameIndex = index;
       		}
        	this.move();
    	}

	next() {
        	this.goto(this.frameIndex + 1);
    	}

	prev() {
        	this.goto(this.frameIndex - 1);
    	}

	move() {
		const offset = 100 / this.itemCount * this.allFrames[this.frameIndex];
        	this.wrapper.style.transform = `translateX(-${offset}%)`;
        	this.dotButtons.forEach(dot => dot.classList.remove('active'));
        	this.dotButtons[this.frameIndex].classList.add('active');
	}

	play() {
        	this.paused = setInterval(() => this.next(), 3000);
    	}

	dots() {
        	const ol = document.createElement('ol');
        	ol.classList.add('carousel-indicators');
        	const children = [];
        	for (let i = 0; i < this.frameCount; i++) {
            		let li = document.createElement('li');
            		if (i === 0) li.classList.add('active');
            		ol.append(li);
            		children.push(li);
       		 }
        	this.slider.prepend(ol);
        	return children;
    	}

	frames() {
		let temp = [];
        	for (let i = 0; i < this.itemCount; i++) {
            		if (this.allItems[i + this.inFrame - 1] !== undefined) {
                		temp.push(i);
            		}
		}
		let allFrames = [];
        	for (let i = 0; i < temp.length; i = i + this.offset) {
            		allFrames.push(temp[i]);
        	}
		if (allFrames[allFrames.length - 1] !== temp[temp.length - 1]) {
            		allFrames.push(temp[temp.length - 1]);
        	}
        	return allFrames;
	}

}

document.addEventListener('DOMContentLoaded', function() {
        new Slider(document.querySelector('.carousel'), {
            inFrame: 3,
            offset: 1,
        });
    });