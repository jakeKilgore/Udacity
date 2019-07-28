const sizePicker = document.getElementById('sizePicker');
const canvas = document.getElementById('pixelCanvas');
const colorPicker = document.getElementById('colorPicker');
let height = document.getElementById('inputHeight');
let width = document.getElementById('inputWidth');
let color = colorPicker.value;

colorPicker.addEventListener('change', function () {
    color = colorPicker.value;
});

sizePicker.addEventListener('submit', makeGrid);


function changeColor(e) {
    e.target.style.backgroundColor = color;
}

function makeGrid(e) {
    e.preventDefault();
    while(canvas.firstChild) {
        canvas.removeChild(canvas.firstChild);
    }
    for(let i = 0; i < height.value; i++) {
        let row = document.createElement('tr');
        for(let j = 0; j < width.value; j++) {
            let cell = document.createElement('td');
            cell.addEventListener('mousedown', changeColor);
            row.appendChild(cell);}
        canvas.appendChild(row);
    }
}
