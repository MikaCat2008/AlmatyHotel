let year, month;


async function GetRoomsCheckerboardPost(year, month) {
    return await PostData("/get-rooms-checkerboard", {
        year: year,
        month: month
    });
}


function AddDay(day) {
    let tr = document.querySelector(".table-header");

    let dayElement = tr.insertCell();

    dayElement.outerHTML = `<th>${day}</th>`;
}


function AddOccupations(index, room) {
    let elements = document.querySelectorAll(
        `#rooms-checkerboard-table > tbody > tr:nth-child(${index + 1}) > td`
    );
    
    elements[0].innerHTML = room[0];

    room[1].forEach(occupation => {
        let [OccupationId, OccupationStart, OccupationEnd, OccupationType] = occupation;

        for (let i = OccupationStart; i < OccupationEnd; i++) {
            const element = elements[i + 1];
            
            if (OccupationType == 1) {
                element.classList.add("reservation-cell");
            }
            else if (OccupationType == 2) {
                element.classList.add("renovation-cell");
            }
            else if (OccupationType == 3) {
                element.classList.add("cleaning-cell");
            }

            element.id = `occupation-${OccupationId}`;
        }
    });
}


function CreateCheckerboard(rooms, days) {
    let tbody = document.querySelector("#rooms-checkerboard-table > tbody");

    for (let i = 0; i < rooms; i++) {
        let rowElement = tbody.insertRow();
        rowElement.insertCell();

        for (let j = 0; j < days; j++) {
            let cellElement = rowElement.insertCell();
    
            cellElement.classList.add("cell");
        }   
    }
}


function SetTitle(name) {
    document.querySelector(".title").innerHTML = name;
}


function MonthPrev() {
    if (month == 1) {
        year--;
        month = 12;
    }
    else
    {
        month--;
    }

    window.location.href = `/rooms-checkerboard?year=${year}&month=${month}`;
}


function MonthNext() {
    if (month == 12) {
        year++;
        month = 1;
    }
    else
    {
        month++;
    }

    window.location.href = `/rooms-checkerboard?year=${year}&month=${month}`;
}


async function LoadMonth(_year, _month) {
    year = _year;
    month = _month;

    StartLoadingAnimation();

    GetRoomsCheckerboardPost(year, month).then(data => {
        StopLoadingAnimation();

        data.days.forEach(day => {
            AddDay(day);
        });

        document.querySelector("#rooms-checkerboard-table > thead > tr:nth-child(1) > th").colSpan = data.days.length + 1;
        
        CreateCheckerboard(data.rooms.length, data.days.length);

        for (let i = 0; i < data.rooms.length; i++) {
            AddOccupations(i, data.rooms[i]);
        }
    });
}
