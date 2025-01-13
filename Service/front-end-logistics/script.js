const statusOptions = ["Formuliert", "In Bearbeitung", "In der Auslieferung befindlich", "Unter dem Weihnachtsbaum"];

async function fetchWishes() {
    try {
        const wishesResponse = await fetch('http://localhost:5000/wishes');
        const wishes = await wishesResponse.json();
        console.log("Wishes:", wishes);

        const statusResponse = await fetch('http://localhost:5002/status');
        const statusList = await statusResponse.json();
        console.log("Status:", statusList);

        const tableBody = document.getElementById('wishesTableBody');
        tableBody.innerHTML = '';

        wishes.forEach((wish, index) => {
            const statusItem = statusList[index];
            if (statusItem) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${index + 1}</td>
                    <td>${wish.wish}</td>
                    <td>${statusItem.status}</td>
                    <td>
                        <button onclick="changeStatus('${statusItem._id}', -1)">-</button>
                        <button onclick="changeStatus('${statusItem._id}', 1)">+</button>
                    </td>
                `;
                tableBody.appendChild(row);
            }
        });
    } catch (error) {
        console.error('Fehler beim Abrufen der Daten:', error);
    }
}

async function changeStatus(statusId, direction) {
    try {
        console.log("Statusänderung für ID:", statusId, "Richtung:", direction);

        const statusResponse = await fetch('http://localhost:5002/status');
        const statusList = await statusResponse.json();
        console.log("Statusliste:", statusList);

        const statusItem = statusList.find(s => s._id === statusId);
        console.log("Statusitem:", statusItem);

        let currentStatusIndex = statusOptions.indexOf(statusItem.status);
        console.log("Aktueller Statusindex:", currentStatusIndex);

        if (currentStatusIndex === -1) return;

        currentStatusIndex += direction;
        if (currentStatusIndex < 0) currentStatusIndex = 0;
        if (currentStatusIndex >= statusOptions.length) currentStatusIndex = statusOptions.length - 1;

        const newStatus = statusOptions[currentStatusIndex];
        console.log("Neuer Status:", newStatus);

        await fetch(`http://localhost:5002/status/${statusId}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ status: newStatus })
        });

        fetchWishes(); // Status aktualisieren und Tabelle neu rendern
    } catch (error) {
        console.error('Fehler beim Ändern des Status:', error);
    }
}

setInterval(fetchWishes, 30000);

document.addEventListener('DOMContentLoaded', fetchWishes);
