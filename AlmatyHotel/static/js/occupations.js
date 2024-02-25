let occupations = {};


async function CreateOccupationPost(RoomId, OccupationStart, OccupationDays, OccupationType) {
    return await PostData("/create-occupation", {
        occupation: [RoomId, OccupationStart, OccupationDays, OccupationType]
    });
}


async function GetOccupationsPost(OccupationType) {
    return await PostData("/get-occupations", {
        occupation_type: OccupationType
    });
}


async function UpdateOccupationPost(OccupationId, RoomId, OccupationStart, OccupationDays, OccupationType) {
    return await PostData("/update-occupation", {
        occupation: [OccupationId, RoomId, OccupationStart, OccupationDays, OccupationType]
    });
}


async function DeleteOccupationPost(OccupationId) {
    return await PostData("/delete-occupation", {
        occupation_id: OccupationId
    });
}


function AddOccupation(tbody, OccupationId, RoomId, OccupationStart, OccupationDays, OccupationType) {
    let rowElement = tbody.insertRow();
    
    let RoomIdElement = rowElement.insertCell();
    let OccupationStartElement = rowElement.insertCell();
    let OccupationDaysElement = rowElement.insertCell();
    let DeleteElement = rowElement.insertCell();

    rowElement.id = `occupation-${OccupationId}`;

    RoomIdElement.innerHTML = `<input type="text" value="${RoomId}" size="3">`;
    RoomIdElement.querySelector("input").onkeyup = InputKeyUpNumber;

    OccupationStartElement.innerHTML = `<input type="date" value="${OccupationStart}">`;
    OccupationStartElement.querySelector("input").onchange = DateChange;

    OccupationDaysElement.innerHTML = `<input type="text" value="${OccupationDays}" size="3">`;
    OccupationDaysElement.querySelector("input").onkeyup = InputKeyUpNumber;

    DeleteElement.innerHTML = "X";
    DeleteElement.onclick = () => DeleteOccupation(OccupationId);
    DeleteElement.classList.add("delete-element");

    occupations[OccupationId] = [
        RoomIdElement.querySelector("input"), 
        OccupationStartElement.querySelector("input"), 
        OccupationDaysElement.querySelector("input"),
        OccupationType
    ]
}


async function CreateOccupation(OccupationId) {
    let RoomIdElement = document.querySelector("#room-id > input");
    let OccupationStartElement = document.querySelector("#occupation-start > input");
    let OccupationDaysElement = document.querySelector("#occupation-days > input");

    if (RoomIdElement.value == "") {
        return ShowText("Поле с номером комнаты не может быть пустым!", 2);
    }

    if (OccupationDaysElement.value == "") {
        return ShowText("Поле с количеством дней не может быть пустым!", 2);
    }

    if (isNaN(Number(RoomIdElement.value))) {
        return ShowText("Номер комнаты должен быть числом!", 2);
    }

    if (isNaN(Number(OccupationDaysElement.value))) {
        return ShowText("Количество дней должно быть числом!", 2);
    }

    await CreateOccupationPost(
        RoomIdElement.value,
        OccupationStartElement.value,
        OccupationDaysElement.value,
        OccupationId
    ).then(data => {
        if (data.status) {
            let text;
            
            if (OccupationId == 1) {
                text = "Комната успешно забронирована!";
            }
            else if (OccupationId == 2) {
                text = "Ремонт успешно назначен!";
            }
            else if (OccupationId == 3) {
                text = "Уборка успешно назначена!";
            }

            return ShowText(text, 1);
        }
    });
}


function GetOccupation(element) {
    let tr = element.parentElement.parentElement;
    
    let OccupationId = Number(tr.id.split("-")[1]);
    let room = occupations[OccupationId]
    let RoomId = Number(room[0].value);
    let OccupationStart = room[1].value;
    let OccupationDays = Number(room[2].value);
    let OccupationType = Number(room[3]);

    return [OccupationId, RoomId, OccupationStart, OccupationDays, OccupationType];
}


function DateChange(event) {
    let element = event.target;

    UpdateOccupationPost(...GetOccupation(element)).then(data => {
        if (data.status) {
            SetChange(element);
        }
    });
}


function InputKeyUpNumber(event) {
    if (event.key == "Enter") {
        let element = event.target;
        
        let number = Number(element.value);

        if (isNaN(number)) {
            SetError(element);
        }
        else {
            UpdateOccupationPost(...GetOccupation(element)).then(data => {
                if (data.status) {
                    SetChange(element);
                }
            });
        }
    }
}


function DeleteOccupation(OccupationId) {
    let occupation = occupations[OccupationId];

    DeleteOccupationPost(OccupationId).then(data => {
        if (data.status) {
            for (let i = 0; i < 3; i++) {
                const element = occupation[i];

                SetError(element);
            }
        }
    });
}


async function LoadOccupations(tbody, OccupationType) {
    StartLoadingAnimation();

    GetOccupationsPost(OccupationType).then(data => {
        StopLoadingAnimation();

        data.occupations.forEach(occupation => {
            AddOccupation(tbody, ...occupation);
        });
    });
}
