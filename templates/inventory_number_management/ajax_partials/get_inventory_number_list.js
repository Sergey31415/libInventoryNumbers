function get_inventory_numbers(id_book) {
    fetch('/get_inventory_number_list/' + id_book)
        .then(response => response.json())
        .then(data => {
            const itemList = document.getElementById('inventory_number_list');
            itemList.innerHTML = '';
            data.forEach(item => {
                const listItem = document.createElement('button');
                listItem.classList.add('btn');
                listItem.classList.add('btn-info');
                listItem.textContent = `${item[1]}`;
                itemList.appendChild(listItem);
            });
        })
        .catch(error => console.log('Failed to fetch items:', error));
}

