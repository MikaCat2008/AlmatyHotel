let rooms = {};


async function CreateRoomPost(RoomType, RoomPrice) {
    return await PostData("/create-room", {
        room: [RoomType, RoomPrice]
    });
}


async function GetRoomsPost() {
    return await PostData("/get-rooms", {});
}


async function UpdateRoomPost(RoomId, RoomType, RoomPrice) {
    return await PostData("/update-room", {
        room: [RoomId, RoomType, RoomPrice]
    });
}


async function DeleteRoomPost(RoomId) {
    return await PostData("/delete-room", {
        room_id: RoomId
    });
}


function AddRoom(RoomId, RoomType, RoomPrice) {
    let tbody = document.querySelector("#rooms-table > tbody");
    let rowElement = tbody.insertRow();
    
    let RoomIdElement = rowElement.insertCell();
    let RoomTypeElement = rowElement.insertCell();
    let RoomPriceElement = rowElement.insertCell();
    let DeleteElement = rowElement.insertCell();

    rowElement.id = `room-${RoomId}`;

    RoomIdElement.innerHTML = `${RoomId}`;

    RoomTypeElement.innerHTML = `
        <select>
            <option value="0">Простая</option>
            <option value="1">Премиум</option>
            <option value="2">Премиум-Люкс</option>
            <option value="3">Люкс</option>
        </select>
    `;
    RoomTypeElement.querySelector("select").value = RoomType;
    RoomTypeElement.querySelector("select").onchange = SelectChange;

    RoomPriceElement.innerHTML = `<input type="text" value="${RoomPrice}" size="3">`;
    RoomPriceElement.querySelector("input").onkeyup = InputKeyUpNumber;

    DeleteElement.innerHTML = "X";
    DeleteElement.onclick = () => DeleteRoom(RoomId);
    DeleteElement.classList.add("delete-element");

    rooms[RoomId] = [
        RoomTypeElement.querySelector("select"), 
        RoomPriceElement.querySelector("input")
    ]
}


async function CreateRoom() {
    let RoomTypeElement = document.querySelector("#room-type > select");
    let RoomPriceElement = document.querySelector("#room-price > input");

    if (RoomPriceElement.value == "") {
        return ShowText("Поле с ценой не может быть пустым!", 2);
    }

    if (isNaN(Number(RoomPriceElement.value))) {
        return ShowText("Цена должна быть числом!", 2);
    }

    await CreateRoomPost(
        RoomTypeElement.value,
        RoomPriceElement.value
    ).then(data => {
        if (data.status) {
            return ShowText("Комната успешно добавлена!", 1);
        }
    });;
}


function GetRoom(element) {
    let tr = element.parentElement.parentElement;
    
    let RoomId = Number(tr.id.split("-")[1]);
    let room = rooms[RoomId]
    let RoomType = Number(room[0].value);
    let RoomPrice = Number(room[1].value);

    return [RoomId, RoomType, RoomPrice];
}


function SelectChange(event) {
    let element = event.target;

    UpdateRoomPost(...GetRoom(element)).then(response => {
        if (response.status) {
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
            UpdateRoomPost(...GetRoom(element)).then(data => {
                if (data.status) {
                    SetChange(element);
                }
            });
        }
    }
}


function DeleteRoom(RoomId) {
    let room = rooms[RoomId];

    DeleteRoomPost(RoomId).then(data => {
        if (data.status) {
            for (let i = 0; i < 3; i++) {
                const element = room[i];

                SetError(element);
            }
        }
    });
}


async function LoadRooms() {
    StartLoadingAnimation();

    GetRoomsPost().then(data => {
        StopLoadingAnimation();

        data.rooms.forEach(room => {
            AddRoom(...room);
        });
    });
}
