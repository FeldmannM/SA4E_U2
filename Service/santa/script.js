async function fetchWishesForSanta() {
    try {
        const wishesResponse = await fetch('http://localhost:5000/wishes');
        const wishes = await wishesResponse.json();

        const usersResponse = await fetch('http://localhost:5001/users');
        const users = await usersResponse.json();

        const statusResponse = await fetch('http://localhost:5002/status');
        const statusList = await statusResponse.json();

        console.log("Wishes:", wishes);
        console.log("Users:", users);
        console.log("Status List:", statusList);

        const tableBody = document.getElementById('santaTableBody');
        tableBody.innerHTML = '';

        wishes.forEach((wish, index) => {
            const user = users[index];
            const statusItem = statusList[index];

            if (user && statusItem) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${index + 1}</td>
                    <td>${user.name}</td>
                    <td>${wish.wish}</td>
                    <td><input type="checkbox" onclick="deleteWish('${wish._id}', '${user._id}', '${statusItem._id}')" /></td>
                `;
                tableBody.appendChild(row);
            } else {
                console.error('Fehlerhafte Zuordnung:', { wish, user, statusItem });
            }
        });
    } catch (error) {
        console.error('Fehler beim Abrufen der Daten:', error);
    }
}

async function deleteWish(wishId, userId, statusId) {
    try {
        // Lösche den Wunsch
        await fetch(`http://localhost:5000/wishes/${wishId}`, {
            method: 'DELETE',
        });

        // Lösche den Benutzer
        await fetch(`http://localhost:5001/users/${userId}`, {
            method: 'DELETE',
        });

        // Lösche den Status
        await fetch(`http://localhost:5002/status/${statusId}`, {
            method: 'DELETE',
        });

        fetchWishesForSanta(); // Aktualisiere die Tabelle nach dem Löschen
    } catch (error) {
        console.error('Fehler beim Löschen der Daten:', error);
    }
}

setInterval(fetchWishesForSanta, 30000);

document.addEventListener('DOMContentLoaded', fetchWishesForSanta);
