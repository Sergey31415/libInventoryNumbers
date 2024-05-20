function check_inventory_numbers_exists_multiple() {
    const csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
    let startRange = document.getElementById('start_range').value;
    let endRange = document.getElementById('end_range').value;

    fetch('/check_inventory_numbers_exists_multiple/', {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            startRange: startRange,
            endRange: endRange
        })
    })
        .then(response => response.json())
        .then(data => {
            const itemList = document.getElementById('alert-place');
            itemList.innerHTML = '';  // очищает после обновления
            let newInventoryNumbers = [];
            if(data.length > 0) {
                itemList.innerHTML = '<br><h4>Эти инвентарные номера уже используются:</h4>';
                doInvalidFies();  // показываем поля красным
            } else {  // если выбранных инвентарных номеров в базе нету, выполняется блок else
               let rangeArray = [];
               for (let i = parseInt(startRange); i <= parseInt(endRange); i++) {
                   rangeArray.push(i);
               }
               itemList.innerHTML = '<br><h4>Эти инвентарные номера могут быть добавлены:</h4>';
               rangeArray.forEach(item => {
                    showAddButton();
                    const listItem = document.createElement('button');
                    listItem.classList.add('btn');
                    listItem.classList.add('btn-success');
                    listItem.classList.add('m-2');
                    listItem.textContent = `${item}`;
                    itemList.appendChild(listItem);
                });
            }
            data.forEach(item => {
                const listItem = document.createElement('button');
                listItem.classList.add('btn');
                listItem.classList.add('btn-danger');
                listItem.classList.add('m-2');
                listItem.textContent = `${item}`;
                itemList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Ошибка:', error));
}

function showCheckButton() {
    document.getElementById('check-inv-nums').classList.remove('hidden');
    document.getElementById('submit-inv-nums').classList.add('hidden');
}

function showAddButton() {
    document.getElementById('check-inv-nums').classList.add('hidden');
    document.getElementById('submit-inv-nums').classList.remove('hidden');
}

function doInvalidFies() {
    let start_range = document.getElementById('start_range');
    let end_range =  document.getElementById('end_range');
    start_range.classList.remove('is-valid');
    end_range.classList.remove('is-valid');
    start_range.classList.add('is-invalid');
    end_range.classList.add('is-invalid');

}