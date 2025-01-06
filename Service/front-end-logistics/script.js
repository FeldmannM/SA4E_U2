const statusOptions = ["Formuliert", "In Bearbeitung", "In der Auslieferung befindlich", "Unter dem Weihnachtsbaum"];

async function fetchWishes() {
    const response = await fetch('http://localhost:5000/wishes');
    const wishes = await response.json();

    const tableBody = document.getElementById('wishesTableBody');
    tableBody.innerHTML = '';

    wishes.forEach((wish, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${wish.wish}</td>
            <td>${wish.status}</td>
            <td>
                <button onclick="changeStatus('${wish._id}', -1)">-</button>
                <button onclick="changeStatus('${wish._id}', 1)">+</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

async function changeStatus(wishId, direction) {
    const response = await fetch('http://localhost:5000/wishes');
    const wishes = await response.json();
    const wish = wishes.find(w => w._id === wishId);
    let currentStatusIndex = statusOptions.indexOf(wish.status);

    if (currentStatusIndex === -1) return;

    currentStatusIndex += direction;
    if (currentStatusIndex < 0) currentStatusIndex = 0;
    if (currentStatusIndex >= statusOptions.length) currentStatusIndex = statusOptions.length - 1;

    const newStatus = statusOptions[currentStatusIndex];

    await fetch(`http://localhost:5000/wishes/${wishId}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: newStatus })
    });

    fetchWishes();
}

document.addEventListener('DOMContentLoaded', fetchWishes);
