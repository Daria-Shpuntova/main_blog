/*
 * <div class="carousel"> width: 100% (от контейнера .container 900px)
 *     <div class="carousel-window"> width: 100% (от родителя 900px); height: 500px
 *         <div class="carousel-slides"> display: flex, style.width = 300% (2700px)
 *             <div class="carousel-item">...</div> style.width = 33.33333% (900px)
 *             <div class="carousel-item">...</div> style.width = 33.33333% (900px)
 *             <div class="carousel-item">...</div> style.width = 33.33333% (900px)
 *         </div>
 *     </div>
 * </div>
 */

class Slider {
    constructor(slider, {autoplay = true, inFrame = 1, offset = 1} = {}) {
        // элемент div.carousel
        this.slider = slider;
        // кол-во элементов в одном кадре
        this.inFrame = inFrame;
        // на сколько элементов смещать
        this.offset = offset;

        // все элементы слайдера
        this.allItems = slider.querySelectorAll('.carousel-item');
        this.slidesX = document.getElementsByClassName("carousel-item");
        // сколько всего элементов
        this.itemCount = this.allItems.length;

        // все кадры слайдера
        this.allFrames = this.frames();
        // сколько всего кадров
        this.frameCount = this.allFrames.length;
        // индекс кадра в окне просмотра
        this.frameIndex = 0;

        // контейнер для элементов
        this.wrapper = slider.querySelector('.carousel-slides');
        // кнопка «вперед»
        this.nextButton = slider.querySelector('.carousel-next');
        // кнопка «назад»
        this.prevButton = slider.querySelector('.carousel-prev');

        this.autoplay = autoplay; // включить автоматическую прокрутку?
        this.paused = null; // чтобы можно было выключать автопрокрутку

        this.init(); // инициализация слайдера
    }

    init() {
        this.dotButtons = this.dots(); // создать индикатор текущего кадра

        // если всего 10 элементов, то ширина одного элемента составляет 1/10
        // ширины контейнера .carousel-slides, то есть 100/10 = 10%
     //   this.allItems.forEach(item => item.style.width = 100 / this.itemCount + '%');
     this.allItems.forEach(item => item.style.width = 100 / this.inFrame + '%');
        // ширина контейнера должна вмещать все элементы: если элементов 10,
        // в окне просмотра 3 элемента, тогда ширина контейнера равна ширине
        // трех окон просмотра (300%) плюс ширина одного элемента 33.33333%,
        let wrapperWidth = this.itemCount / this.inFrame * 100;
        console.log(wrapperWidth)
        console.log(this.itemCount)
        console.log(this.inFrame)
        this.wrapper.style.width = wrapperWidth + '%';

        this.nextButton.addEventListener('click', event => { // клик по кнопке «вперед»
            event.preventDefault();
            this.next();
        });

        this.prevButton.addEventListener('click', event => { // клик по кнопке «назад»
            event.preventDefault();
            this.prev();
        });

        // клики по кнопкам индикатора текущего кадра
        this.dotButtons.forEach(dot => {
            dot.addEventListener('click', event => {
                event.preventDefault();
                const frameIndex = this.dotButtons.indexOf(event.target);
                if (frameIndex === this.frameIndex) return;
                this.goto(frameIndex);
            });
        });

        if (this.autoplay) { // включить автоматическую прокрутку?
            this.play();
            // когда мышь над слайдером — останавливаем автоматическую прокрутку
            this.slider.addEventListener('mouseenter', () => clearInterval(this.paused));
            // когда мышь покидает пределы слайдера — опять запускаем прокрутку
            this.slider.addEventListener('mouseleave', () => this.play());
        }
    }

    // перейти к кадру с индексом index
    goto(index) {
        if (index > this.frameCount - 1) {
            this.frameIndex = 0;
        } else if (index < 0) {
            this.frameIndex = this.frameCount - 1;
        } else {
            this.frameIndex = index;
        }
        // ...и выполнить смещение
        this.move();
    }

    // перейти к следующему кадру
    next() {
        this.goto(this.frameIndex + 1);
    }

    // перейти к предыдущему кадру
    prev() {
        this.goto(this.frameIndex - 1);
    }

    // рассчитать и выполнить смещение
    move() {
        // на сколько нужно сместить, чтобы нужный кадр попал в окно
        const offset = 100 / this.itemCount * this.allFrames[this.frameIndex];
        this.wrapper.style.transform = `translateX(-${offset}%)`;
        this.dotButtons.forEach(dot => dot.classList.remove('active'));
        this.dotButtons[this.frameIndex].classList.add('active');
        console.log('move');
        console.log(this.frameIndex);
        console.log(this.allFrames[this.frameIndex]);
        console.log(this.allItems, 'this.allItems')

        for (let a = 0; a < this.itemCount; a++){
            console.log(a, 'a')
            if (a==0) {
                console.log(a, '1f')
                for (var b=0; b<this.inFrame; b++) {
                    this.allItems[b].style.display = "block";
                }
                for (var b=this.inFrame; b<this.itemCount; b++) {
                    this.allItems[b].style.display = "none";
                }
            };
            if (a>0 && ((a+this.inFrame)<this.itemCount)) {
                console.log(a, '2f')
                for (var b; b<a; b++) {
                    this.allItems[b].style.display = "none";
                }
                for (var b=a; b<(a+this.inFrame); b++) {
                    this.allItems[b].style.display = "block";
                }
                for (var b=(a+this.inFrame); b<this.itemCount; b++ ){
                    this.allItems[b].style.display = "none";
                }
            };
            if (a>0 && ((a+this.inFrame)>this.itemCount)) {
                console.log(a, '3f')
                var c = (a+this.inFrame)-this.itemCount;
                for (c; c<a; c++) {
                    this.allItems[c].style.display = "none";
                }
                for (var s=a; s<this.itemCount; s++){
                    this.allItems[s].style.display = "block";
                }
                for (var d; d<c; d++) {
                    this.allItems[d].style.display = "block";
                }
            };



//            console.log(this.allFrames[a], 'rr');
//            if ((this.inFrame+this.frameIndex)<this.frameCount) {
//   //         this.allFrames[a].style.display = "block";
//             console.log((this.inFrame+this.frameIndex)<this.frameCount)
//             } else {
//             console.log(this.allFrames);
//             console.log(this.frameIndex);
//             console.log(this.slidesX);
//             console.log(this.slidesX[this.frameIndex]);
//             this.slidesX[this.frameIndex].style.display = "none";
//             console.log('False');
//             }
//              console.log(this.inFrame+this.frameIndex)
        }
 //       if (n < 1) {slideIndexX = slidesX.length}
 //       for (i = 0; i < slidesX.length; i++) {
 //       slidesX[i].style.display = "none";
 //      for (let a = 0; a < this.frameCount; a++){
 //          console.log(allFrames[a], 'rr');
 //      if ((this.inFrame+this.frameIndex)<this.frameCount) {
  //     this.allFrames[a].style.display = "block";
   //     console.log((this.inFrame+this.frameIndex)<this.frameCount)
   //     } else {
  //      this.allFrames[a].style.display = "none";
   //     console.log('False');
   //     }
   //      console.log(this.inFrame+this.frameIndex)
   //     if (a+this.inFrame>frameCount){
   //          console.log('if a>')}
//          this.allFrames[a].style.display = "none";
//          console.log('if a')
//          if (a+this.inFrame>frameCount){
//              console.log('if a>')
//              for (a, a<this.inFrame, a++) {
//                  this.allFrames[a].style.display = "block";
//              }

//          }

  //        for (let b = 0; b < this.frameIndex; b++){
  //            console.log(this.allFrames[this.frameIndex], "none", this.frameIndex)
  //            this.allItems[this.frameIndex].style.display = "none";

  //            }
  //         }
  }


    // запустить автоматическую прокрутку
    play() {
        this.paused = setInterval(() => this.next(), 3000);
      //  this.move();
    }

    // создать индикатор текущего кадра
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
//        this.slider.prepend(ol);
        return children;
    }

    // индекс первого элемента каждого кадра
    frames() {
        // все наборы элементов, которые потенциально могут быть кадрами
        let temp = [];
        for (let i = 0; i < this.itemCount; i++) {
            // этот набор из this.inFrame элементов без пустого места
            if (this.allItems[i + this.inFrame - 1] !== undefined) {
                temp.push(i);
            }
        }
        // с учетом того, что смещение this.offset может быть больше 1,
        // реальных кадров будет меньше или столько же
        let allFrames = [];
        for (let i = 0; i < temp.length; i = i + this.offset) {
            allFrames.push(temp[i]);
        }
        // в конце могут быть элементы, которые не могут образовать целый кадр (без пустоты),
        // такой кадр вообще не попадает в окно просмотра; вместо него показываем последний
        // целый кадр из числа потенциальных; при этом смещение будет меньше this.offset
        if (allFrames[allFrames.length - 1] !== temp[temp.length - 1]) {
            allFrames.push(temp[temp.length - 1]);
        }

        return allFrames;
    }
}

document.addEventListener('DOMContentLoaded', function() {
        new Slider(document.querySelector('.carousel'), {
            inFrame: 3, // два элемента в кадре
            offset: 1, // смещать на один элемент
        });
    });