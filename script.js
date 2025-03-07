document.addEventListener("DOMContentLoaded", function () {
    let calendarEl = document.getElementById("calendar");
    let eventInfoEl = document.getElementById("eventInfo");

    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",  // Full month view
        headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay"
        },
        events: [
            { title: "Orientation Day", start: "2025-03-15", description: "Block A, Room 101" },
            { title: "Tech Fest", start: "2025-04-20", description: "Block B, Auditorium" },
            { title: "Annual Sports Meet", start: "2025-05-10", description: "Sports Ground" }
        ],
        eventClick: function (info) {
            eventInfoEl.innerHTML = `
                <strong>${info.event.title}</strong><br>
                <span>Date: ${info.event.start.toLocaleDateString()}</span><br>
                <span>Location: ${info.event.extendedProps.description}</span>
            `;
        }
    });

    calendar.render();
});

// Handle Login
function handleSubmit() {
    document.getElementById("authForm").style.display = "none";
    document.getElementById("dashboard").style.display = "block";
}

// Faculty Locator
let facultyData = {
    "Computer Science": [],
    "Electrical Engineering": []
};

function displayFaculty() {
    let department = document.getElementById("departmentSelect").value;
    let facultyList = document.getElementById("facultyList");
    facultyList.innerHTML = facultyData[department].map((f, i) => 
        `<div class="faculty-card">
            <h3>${f.name}</h3>
            <p>${f.education}</p>
            <button onclick="removeFaculty('${department}', ${i})">Remove</button>
        </div>`
    ).join("");
}

function addFaculty() {
    let name = prompt("Enter Faculty Name:");
    if (name) {
        let department = document.getElementById("departmentSelect").value;
        facultyData[department].push({ name });
        displayFaculty();
    }
}

function removeFaculty(department, index) {
    facultyData[department].splice(index, 1);
    displayFaculty();
}
