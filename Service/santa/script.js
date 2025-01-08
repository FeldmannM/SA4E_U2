async function fetchWishesForSanta() {
    const wishesResponse = await fetch('http://localhost:5000/wishes');
    const wishes = await wishesResponse.json();

    const usersResponse = await fetch('http://localhost:5001/users');
    const users = await usersResponse.json();

    const tableBody = document.getElementById('santaTableBody');
    tableBody.innerHTML = '';

    wishes.forEach((wish, index) => {
        const user = users[index];
        if (user) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${user.name}</td>
                <td>${wish.wish}</td>
            `;
            tableBody.appendChild(row);
        }
    });
}

document.addEventListener('DOMContentLoaded', fetchWishesForSanta);
