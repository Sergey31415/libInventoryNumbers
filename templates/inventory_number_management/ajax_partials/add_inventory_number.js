function addInventory(id_book) {
    const csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
    let startRange = document.getElementById('start_range').value;
    let endRange = document.getElementById('end_range').value;

    fetch('/add_inventory_number/' + id_book + '/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            book_id: id_book,
            startRange: startRange,
            endRange: endRange
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                //throw new Error(data.error);
                //здесь можно добавить вывод ошибки
            });
        }
        return response.json();
    })
    .then(data => {
        get_inventory_numbers(id_book);
        document.getElementById('alert-place').innerHTML = '';  // очищает поле уведомлений после добавления
        showSuccessAlert();
        showCheckButton();
    })
    .catch(error => console.error('Ошибка:', error));
}

function showSuccessAlert() {
    let alert_place = document.getElementById('alert-place');
    alert_place.innerHTML = '<div class="alert alert-success" role="alert">Инвентарные номера добавлены</div>'
    //alert_place.firstElementChild.classList.add('fade-in-down');
    setTimeout(function() {
        alert_place.innerHTML = '';
    }, 1500);
}

